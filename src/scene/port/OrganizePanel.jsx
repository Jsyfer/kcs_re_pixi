import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../common/AssetsFactory';
import { ShipCard } from './organizePanel/ShipCard';
import { PixiButton } from '../../common/PixiButton';


export const OrganizePanel = () => {
    const [commonSpritesheets, setCommonSpritesheets] = useState([])
    const [organizeMainSpritesheets, setOrganizeMainSpritesheets] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/common/common_main.json', setCommonSpritesheets);
        AssetsFactory.loadAsFrames('assets/kcs2/img/organize/organize_main.json', setOrganizeMainSpritesheets);
    }, []);

    if (commonSpritesheets.length === 0 || organizeMainSpritesheets.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            {/* 背景 */}
            <Sprite image={'assets/kcs2/img/common/bg/011.png'} x={0} y={0} />
            {/* 背景マスク */}
            <Sprite texture={commonSpritesheets[15]} x={150} y={146} />
            {/* 艦船選択背景 */}
            <Sprite texture={commonSpritesheets[67]} x={0} y={104} />
            {/* 艦船選択 */}
            <Sprite texture={commonSpritesheets[1]} x={195} y={114} />
            {/* 給 */}
            <PixiButton default={organizeMainSpritesheets[17]} x={465} y={157} />
            {/* 随伴艦一括解除 */}
            <PixiButton default={organizeMainSpritesheets[56]} hover={organizeMainSpritesheets[57]} x={570} y={162} />
            {/* 艦隊名 */}
            <Sprite texture={organizeMainSpritesheets[27]} x={694} y={150} />
            {/* 編集 */}
            <PixiButton default={organizeMainSpritesheets[60]} x={1112} y={151} />
            {/* 艦船リスト */}
            <ShipCard x={180} y={198} />
            <ShipCard x={693} y={198} />
            <ShipCard x={180} y={366} />
            <ShipCard x={693} y={366} />
            <ShipCard x={180} y={534} />
            <ShipCard x={693} y={534} />
        </Container>
    );
};