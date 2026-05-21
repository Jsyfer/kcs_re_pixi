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
import { getShipType, getShipSpeed } from '@ship/shipCommon';

// 艦船Info（編成Filter）
export const ShipInfo = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const getData = useStore(state => state.getData)



    const target_ship_base_info = getData.api_data.api_mst_ship.find(item => item.api_id === props.shipId);

    return (
        <Container x={props.x} y={props.y}>
            {/* 艦種／艦船名 */}
            <Text
                x={8} y={0}
                text={getShipType(target_ship_base_info.api_stype) + ' ' + target_ship_base_info.api_name}
                style={{ fill: 'black', fontSize: 20 }}
            />
            {/* 練度(Lv) */}
            <Text
                x={280} y={0}
                text={props.shipLv}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 20 }}
            />
            {/* 耐久 */}
            <Text
                x={340} y={0}
                text={props.shipNowHp}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            {/* 火力 */}
            <Text
                x={385} y={0}
                text={props.shipKaryoku}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            {/* 雷装 */}
            <Text
                x={435} y={0}
                text={props.shipRaisou}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            {/* 対空 */}
            <Text
                x={480} y={0}
                text={props.shipTaiku}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            <Sprite texture={commonMain[getShipSpeed(props.shipSoku)]} anchor={{ x: 1, y: 0 }} x={535} y={0} />
        </Container>
    );
};