import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { RepairDock } from './RepairDock';
import { useStore } from "../../../common/StoreFactory"

export const RepairPanel = () => {
    const portData = useStore((state) => state.portData)
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const repairMain = AssetsFactory.getSpritesheet("kcs2/img/repair/repair_main.json")

    return (
        <Container x={0} y={0}>
            <Sprite image={'kcs2/img/common/bg/014.png'} x={0} y={0} />
            {/* ドック選択背景 */}
            <Sprite texture={commonMain[67]} x={0} y={104} />
            {/* ドック選択 */}
            <Sprite texture={repairMain[0]} x={195} y={114} />
            {/* ドック */}
            {[0, 1, 2, 3].map(i => <RepairDock key={i} x={195} y={180 + 125 * i} />)}
        </Container>
    );
};