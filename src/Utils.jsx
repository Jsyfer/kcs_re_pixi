import { useState, useCallback, useEffect } from 'react';
import { Stage, Container, Sprite, Text, useTick } from '@pixi/react';
import { Assets } from 'pixi.js'
import * as AssetsFactory from '@common/AssetsFactory';
import map_info from '../assets/kcs2/resources/map/062/01_info18.json';

const spritesheet = "kcs2/resources/map/062/01_image.json"
const font = {
    fill: 'yellow',
    fontSize: 22,
    fontWeight: 400,
    stroke: 'black',         // 描边颜色（字符串或十六进制数值）
    strokeThickness: 3,      // 描边宽度
}

export default function Utils() {
    // const [duplicate_list, setDuplicate_list] = useState([]);
    Assets.load(spritesheet);

    const mapSprite = AssetsFactory.getSpritesheet(spritesheet)
    // 1. 在渲染外计算已存在的坐标，避免在渲染中触发 setState
    const duplicate_coords = [];
    const rendered_spots = map_info.spots.map(spot => `${spot.x},${spot.y}`);

    return (
        <Stage width={1200} height={720} options={{ background: 0x000000 }}>
            <Sprite texture={mapSprite[1]} />
            <Sprite texture={mapSprite[2]} />
            {
                map_info.spots.map((spot, index) => {
                    const coordKey = `${spot.x},${spot.y}`;

                    // 2. 判断当前坐标是否已经出现过
                    if (duplicate_coords.includes(coordKey)) {
                        return <Text key={index} x={spot.x + 20} y={spot.y} text={`,${spot.no}`} style={font} />
                    } else {
                        // 3. 记录已渲染的坐标
                        duplicate_coords.push(coordKey);
                        return <Text key={index} x={spot.x} y={spot.y} text={spot.no} style={font} />
                    }
                })
            }
            {/* <Text x={600} y={400} text={"Hello World!"} style={font} /> */}
        </Stage>
    );
}
