import { useEffect, useState } from 'react';
import { Container, Sprite, Text, useTick } from '@pixi/react';
import { Assets, Texture } from 'pixi.js'

export const PortTopMenu = () => {
    const [portSkin, setPortSkin] = useState([])
    const [topLeftRingAngle, setTopLeftRingAngle] = useState(0)
    const [topLeftTextAngle, setTopLeftTextAngle] = useState(0)
    const [timer, setTimer] = useState(0)
    const [font, setFont] = useState(null)


    useTick(() => {
        setTimer(timer + 1);
        if (timer > 60) {
            setTopLeftRingAngle(angle => angle += 3);
            setTimer(timer - 60);
        }
        setTopLeftTextAngle(angle => angle += 0.2)
    });

    useEffect(() => {
        Assets.load('assets/kcs2/img/port/port_skin_1.json').then((data) => {
            setPortSkin(
                Object.keys(data.textures).map(frame =>
                    Texture.from(frame)
                )
            );
        });
        Assets.load('assets/kcs2/resources/font/A-OTF-UDShinGoPro-Light.woff2').then((data) => {
            data.fill = 'white';
            data.fontSize = 20;
            data.fontWeight = 400;
            setFont(data)
        })
    }, []);

    if (portSkin.length === 0 || null === font) {
        return null
    }

    return (
        <Container x={0} y={0}>
            {/* top left ring */}
            <Sprite texture={portSkin[2]} x={65} y={60} anchor={0.5} angle={topLeftRingAngle} />
            {/* menu background */}
            <Sprite texture={portSkin[14]} />
            {/* left bar */}
            <Sprite texture={portSkin[13]} />
            {/* top bar */}
            <Sprite texture={portSkin[12]} x={415} />
            {/* buttom bar */}
            <Sprite texture={portSkin[11]} x={415} y={706} />
            {/* top left ring background*/}
            <Sprite texture={portSkin[1]} x={65} y={60} anchor={0.5} />
            {/* top left text*/}
            <Sprite texture={portSkin[3]} x={65} y={60} anchor={0.5} angle={topLeftTextAngle} />
            {/* 用户名 */}
            <Text text={"ロビン"} x={174} y={10} style={font} />
            {/* 艦隊司令部Lv */}
            <Sprite texture={portSkin[27]} x={415} y={17} />
            <Text text={"120"} x={550} y={16} style={font} />
            <Text text={"[大将]"} x={600} y={16} style={font} />
            {/* 艦娘 */}
            <Sprite texture={portSkin[28]} x={697} y={18} />
            <Text text={"285"} x={740} y={16} style={font} />
            {/* 装備 */}
            <Sprite texture={portSkin[29]} x={790} y={18} />
            <Text text={"1210"} x={833} y={16} style={font} />
            {/* 高速修復 */}
            <Sprite texture={portSkin[22]} x={900} y={16} />
            <Text text={"3000"} x={940} y={16} style={font} />
            {/* 開発資材 */}
            <Sprite texture={portSkin[23]} x={1000} y={16} />
            <Text text={"3000"} x={1040} y={16} style={font} />
            {/* 改修資材 */}
            <Sprite texture={portSkin[24]} x={1100} y={16} />
            <Text text={"3000"} x={1140} y={16} style={font} />
            {/* 燃料 */}
            <Sprite texture={portSkin[18]} x={990} y={50} />
            <Text text={"300000"} x={1020} y={49} style={font} />
            {/* 弾薬 */}
            <Sprite texture={portSkin[19]} x={990} y={79} />
            <Text text={"300000"} x={1020} y={78} style={font} />
            {/* 鋼 */}
            <Sprite texture={portSkin[20]} x={1096} y={50} />
            <Text text={"300000"} x={1126} y={49} style={font} />
            {/* ボーキサイト */}
            <Sprite texture={portSkin[21]} x={1096} y={79} />
            <Text text={"300000"} x={1126} y={78} style={font} />


        </Container>
    );


};