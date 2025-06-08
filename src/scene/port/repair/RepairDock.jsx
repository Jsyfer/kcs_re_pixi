import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';

export const RepairDock = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const repairMain = AssetsFactory.getSpritesheet("kcs2/img/repair/repair_main.json")
    const organizeMain = AssetsFactory.getSpritesheet("kcs2/img/organize/organize_main.json")

    return (
        <Container x={props.x} y={props.y}>
            <Sprite texture={repairMain[10]} x={0} y={0} />
        </Container>
    );
};