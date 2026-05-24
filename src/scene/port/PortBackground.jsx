import { Container, Sprite } from '@pixi/react';
import resources_mapping from '@/resources_mapping.json'
import { useStore } from "@common/StoreFactory"
import { getShipImage } from "@ship/shipCommon";

// 母港背景
export const PortBackground = () => {
    const portData = useStore(state => state.portData)

    const flagShipId = portData.api_data.api_deck_port[0].api_ship[0]
    const target_ship = portData.api_data.api_ship.find(e => e.api_id === flagShipId);
    const ship_full_img = getShipImage('full', target_ship);

    const furnitureList = portData.api_data.api_basic.api_furniture;
    const furniture0 = resources_mapping.furniture.find(item => item.api_id === furnitureList[0]).furniture;
    const furniture1 = resources_mapping.furniture.find(item => item.api_id === furnitureList[1]).furniture;
    const furniture2 = resources_mapping.furniture.find(item => item.api_id === furnitureList[2]).furniture;
    const furniture3 = resources_mapping.furniture.find(item => item.api_id === furnitureList[3]).furniture;
    const furniture4 = resources_mapping.furniture.find(item => item.api_id === furnitureList[4]).furniture;
    const furniture5 = resources_mapping.furniture.find(item => item.api_id === furnitureList[5]).furniture;

    return (
        <Container x={0} y={0}>
            {/* 家具 */}
            <Sprite image={`kcs2/resources/furniture/normal/${furniture0}`} y={415.5} />
            <Sprite image={`kcs2/resources/furniture/normal/${furniture1}`} />
            {/* TODO 早晚时间窗外背景动态变换 */}
            <Sprite image={'kcs2/resources/furniture/outside/window_bg_4-2.png'} x={300} />
            <Sprite image={`kcs2/resources/furniture/normal/${furniture2}`} x={300} />
            <Sprite image={`kcs2/resources/furniture/normal/${furniture3}`} />
            <Sprite image={`kcs2/resources/furniture/normal/${furniture4}`} x={870} />
            <Sprite image={`kcs2/resources/furniture/normal/${furniture5}`} y={200} />
            {/* 舰娘 */}
            <Sprite image={ship_full_img} x={930} y={620} anchor={{ x: 0.5, y: 0.5 }} />
        </Container>
    );
};