import { useCallback, useEffect, useRef, useState } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import { useStore } from '@common/StoreFactory';
import resouces_mapping from '@/resources_mapping.json';
import * as PIXI from 'pixi.js';
import { ShipHp } from '@ship/ShipHp';
import { getShipType, getShipSpeed } from '@ship/shipCommon';
import { CheckboxButton } from '@/common/CheckboxButton';

// 戒指
export const Ring = (props) => {
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")

    return (
        <Container x={props.x} y={props.y}>
            {/* TODO Ring animation effect */}
            <Sprite texture={commonMisc[181]} scale={0.6} />
        </Container>
    );
};