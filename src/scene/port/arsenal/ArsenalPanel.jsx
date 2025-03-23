import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { PixiButton } from '../../../common/PixiButton';
import { ArsenalDock } from './ArsenalDock';

// 工廠
export const ArsenalPanel = () => {
    const [commonMain, setCommonMain] = useState([])
    const [arsenalAnimation, setArsenalAnimation] = useState([])
    const [arsenalMain, setArsenalMain] = useState([])
    const [arsenalSkin, setArsenalSkin] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames("kcs2/img/common/common_main.json", setCommonMain);
        AssetsFactory.loadAsFrames("kcs2/img/arsenal/arsenal_animation.json", setArsenalMain);
        AssetsFactory.loadAsFrames("kcs2/img/arsenal/arsenal_main.json", setArsenalMain);
        AssetsFactory.loadAsFrames("kcs2/img/arsenal/arsenal_skin_1.json", setArsenalSkin);
    }, []);

    if (commonMain.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            <Sprite image={"kcs2/img/common/bg/015.png"} x={0} y={0} />

            {/* ドック用途選択 */}
            <Sprite texture={commonMain[67]} x={0} y={104} />
            <Sprite texture={arsenalMain[8]} x={195} y={114} />
            {/* 現在の建造状況 */}
            <Sprite texture={commonMain[67]} x={530} y={104} />
            <Sprite texture={arsenalMain[4]} x={550} y={114} />


            {/* 建造 */}
            <PixiButton default={arsenalMain[95]} hover={arsenalMain[96]} x={180} y={200} />
            {/* 解体 */}
            <PixiButton default={arsenalMain[93]} hover={arsenalMain[94]} x={210} y={320} />
            {/* 開発 */}
            <PixiButton default={arsenalMain[91]} hover={arsenalMain[92]} x={180} y={440} />
            {/* 廃棄 */}
            <PixiButton default={arsenalMain[89]} hover={arsenalMain[90]} x={210} y={560} />

            {/* ドック */}
            <Sprite texture={arsenalSkin[1]} x={530} y={145} />
            <Sprite texture={arsenalSkin[0]} x={552} y={214} />
            <Sprite texture={arsenalSkin[2]} x={1167} y={220} />

            <ArsenalDock x={605} y={190} />
        </Container>
    );
};