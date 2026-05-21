import { useCallback } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import { PixiButton } from '@common/PixiButton';
import { Graphics } from 'pixi.js'
import * as AssetsFactory from '@common/AssetsFactory';
import { useStore } from '@common/StoreFactory';
import resouces_mapping from '@/resources_mapping.json';
import { ShipHp } from './ShipHp';
import { ShipExp } from './ShipExp';
import { ShipPowerUpStatus } from './ShipPowerUpStatus';
import { getShipType } from '@ship/shipCommon';

// 艦船Info（編成Filter）
export const ShipInfo = (props) => {
    const getData = useStore(state => state.getData)

    const target_ship_base_info = getData.api_data.api_mst_ship.find(item => item.api_id === props.shipId);
    return (
        <Container x={props.x} y={props.y}>
            <Text text={getShipType(target_ship_base_info.api_stype) + ' ' + target_ship_base_info.api_name} x={8} y={0} style={{ fill: 'black', fontSize: 20 }} />
        </Container>
    );
};