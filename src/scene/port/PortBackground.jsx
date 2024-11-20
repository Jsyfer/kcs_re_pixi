import { Container, Sprite } from '@pixi/react';
import resources_mapping from '../../resources_mapping.json'
import { Assets } from 'pixi.js'

export const PortBackground = (props) => {
    const flagShipId = props.portData.api_data.api_deck_port[0].api_ship[0]
    const flagShip_prefix = props.portData.api_data.api_ship.find(e => e.api_id === flagShipId).api_ship_id
    const flagShip_inner = resources_mapping.ship.find(e => e.api_id === flagShip_prefix).full
    const flagShip_suffix = props.getData.api_data.api_mst_shipgraph.find(e => e.api_id === flagShip_prefix).api_filename
    const furnitureList = props.portData.api_data.api_basic.api_furniture;
    const furniture0 = resources_mapping.furniture.find(item => item.api_id === furnitureList[0]).furniture;
    const furniture1 = resources_mapping.furniture.find(item => item.api_id === furnitureList[1]).furniture;
    const furniture2 = resources_mapping.furniture.find(item => item.api_id === furnitureList[2]).furniture;
    const furniture3 = resources_mapping.furniture.find(item => item.api_id === furnitureList[3]).furniture;
    const furniture4 = resources_mapping.furniture.find(item => item.api_id === furnitureList[4]).furniture;
    const furniture5 = resources_mapping.furniture.find(item => item.api_id === furnitureList[5]).furniture;

    return (
        <Container x={0} y={0}>
            {/* 家具 */}
            <Sprite texture={Assets.get(`kcs2/resources/furniture/normal/${furniture0}`)} y={415.5} />
            <Sprite texture={Assets.get(`kcs2/resources/furniture/normal/${furniture1}`)} />
            <Sprite texture={Assets.get('kcs2/resources/furniture/outside/window_bg_4-2.png')} x={300} />
            <Sprite texture={Assets.get(`kcs2/resources/furniture/normal/${furniture2}`)} x={300} />
            <Sprite texture={Assets.get(`kcs2/resources/furniture/normal/${furniture3}`)} />
            <Sprite texture={Assets.get(`kcs2/resources/furniture/normal/${furniture4}`)} x={870} />
            <Sprite texture={Assets.get(`kcs2/resources/furniture/normal/${furniture5}`)} y={200} />
            {/* 舰娘 */}
            <Sprite texture={Assets.get(`kcs2/resources/ship/full/0${flagShip_prefix}_${flagShip_inner}_${flagShip_suffix}.png`)} x={400} y={100} />
        </Container>
    );
};