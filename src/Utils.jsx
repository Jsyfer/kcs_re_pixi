import { useState, useEffect } from 'react';
import { Stage, Sprite, Text } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import map_info from '../assets/kcs2/resources/map/062/02_info.json';

const resources = [
    "kcs2/resources/map/062/02_image.json",
    "kcs2/resources/map/062/01_image18.json",
    "kcs2/resources/map/062/01_image19.json",
    "kcs2/resources/map/062/01_image23.json"
]

const font = {
    fill: 'yellow',
    fontSize: 20,
    fontWeight: 400,
    stroke: 'black',         // 描边颜色（字符串或十六进制数值）
    strokeThickness: 3,      // 描边宽度
}
const fontRed = {
    fill: 'red',
    fontSize: 22,
    fontWeight: 400,
    stroke: 'black',         // 描边颜色（字符串或十六进制数值）
    strokeThickness: 3,      // 描边宽度
}

export default function Utils() {

    const [mapSprite, setMapSprite] = useState([]);

    useEffect(() => {
        AssetsFactory.loadAsFrames(resources[0], setMapSprite);
    }, []);

    // 1. 在渲染外计算已存在的坐标，避免在渲染中触发 setState
    const duplicate_coords = [];

    if (mapSprite.length === 0) {
        return <Stage width={1200} height={720} options={{ background: 0x000000 }} />;
    }

    return (
        <Stage width={1200} height={720} options={{ background: 0x000000 }}>
            <Sprite texture={mapSprite[1]} />
            <Sprite texture={mapSprite[2]} />

            {
                map_info.spots.map((spot, index) => {
                    const coordKey = `${spot.x},${spot.y}`;

                    // 2. 判断当前坐标是否已经出现过
                    if (duplicate_coords.includes(coordKey)) {
                        return <Text key={spot.no} x={spot.x + 20} y={spot.y} text={`,${spot.no}`} style={font} />
                    } else {
                        // if (spot.line !== undefined) {
                        //     return <Sprite texture={mapSprite[spot.no + 3]} x={spot.x + spot.line.x} y={spot.y + spot.line.y} />
                        // }
                        // 3. 记录已渲染的坐标
                        duplicate_coords.push(coordKey);
                        return <Text key={spot.no} x={spot.x} y={spot.y} text={spot.no} style={font} />
                    }
                })
            }

            {/* {
                map_info39.labels.map((label, index) => {
                    const coordKey = `${label.x},${label.y}`;
                    return <Text key={index} x={label.x - 30} y={label.y} text={label.img} style={fontRed} />
                })
            }

            {
                map_info39.spots.map((spot, index) => {
                    const coordKey = `${spot.x},${spot.y}`;
                    // 2. 判断当前坐标是否已经出现过
                    if (duplicate_coords.includes(coordKey)) {
                        return <Text key={spot.no} x={spot.x + 20} y={spot.y} text={`,${spot.no}`} style={font} />
                    } else {
                        // 3. 记录已渲染的坐标
                        duplicate_coords.push(coordKey);
                        return <Text key={spot.no} x={spot.x} y={spot.y} text={spot.no} style={font} />
                    }
                })
            } */}


            {/* <Text x={600} y={400} text={"Hello World!"} style={font} /> */}
        </Stage>
    );
}
