import { useEffect, useState } from 'react';
import { Container, Sprite, Text, useTick } from '@pixi/react';
import { Assets } from 'pixi.js'
import { PixiButton } from '../../common/PixiButton';
import * as AssetsFactory from '../../common/AssetsFactory';

export const PortTopMenu = ({ panelName }) => {
    const [portSkin, setPortSkin] = useState([])
    const [topLeftRingAngle, setTopLeftRingAngle] = useState(0)
    const [topLeftTextIndex, setTopLeftTextIndex] = useState(3)
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
        AssetsFactory.loadAsFrames('assets/kcs2/img/port/port_skin_1.json', setPortSkin);
        Assets.load('assets/kcs2/resources/font/A-OTF-UDShinGoPro-Light.woff2').then((data) => {
            data.fill = 'white';
            data.fontSize = 20;
            data.fontWeight = 400;
            setFont(data)
        });

        switch (panelName) {
            case "henseiPanel":
                setTopLeftTextIndex(4)
                break;
            case "hokyuuPanel":
                setTopLeftTextIndex(5)
                break;
            case "kaisouPanel":
                setTopLeftTextIndex(6)
                break;
            case "nyuukyoPanel":
                setTopLeftTextIndex(9)
                break;
            case "koujyouPanel":
                setTopLeftTextIndex(7)
                break;
            case "kaisyuPanel":
                setTopLeftTextIndex(0)
                break;
            case "shutsugekiPanel":
                setTopLeftTextIndex(10)
                break;
            default:
                setTopLeftTextIndex(3)
                break;
        }
    }, [panelName]);

    if (portSkin.length === 0 || null === font) {
        return null
    }

    return (
        <Container x={0} y={0}>
            {/* top left ring */}
            <Sprite texture={portSkin[2]} x={68} y={61} anchor={0.5} angle={topLeftRingAngle} />
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
            <Sprite texture={portSkin[topLeftTextIndex]} x={65} y={60} anchor={0.5} angle={topLeftTextAngle} />
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
            {/* 戦績表示 */}
            <PixiButton default={portSkin[40]} hover={portSkin[41]} x={180} y={45} />
            {/* 友軍艦隊 */}
            <PixiButton default={portSkin[45]} hover={portSkin[46]} x={298} y={43} />
            {/* 図鑑表示 */}
            <PixiButton default={portSkin[47]} hover={portSkin[48]} x={418} y={45} />
            {/* アイテム */}
            <PixiButton default={portSkin[33]} hover={portSkin[34]} x={540} y={45} />
            {/* 模様替え */}
            <PixiButton default={portSkin[35]} hover={portSkin[36]} x={663} y={45} />
            {/* 任務（クエスト） */}
            <PixiButton default={portSkin[37]} hover={portSkin[38]} x={780} y={45} />
            {/* アイテム屋 */}
            <PixiButton default={portSkin[25]} hover={portSkin[26]} x={900} y={45} />
        </Container>
    );


};