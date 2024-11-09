import { Container, Sprite } from '@pixi/react';
import resources_mapping from '../../resources_mapping.json'

export const PortBackground = (props) => {
    const flagShipId = props.portData.api_data.api_deck_port[0].api_ship[0]
    const flagShip_prefix = props.portData.api_data.api_ship.find(e => e.api_id === flagShipId).api_ship_id
    const flagShip_inner = resources_mapping.ship.find(e => e.api_id === flagShip_prefix).full
    const flagShip_suffix = props.getData.api_data.api_mst_shipgraph.find(e => e.api_id === flagShip_prefix).api_filename

    return (
        <Container x={0} y={0}>
            {/* 家具 */}
            <Sprite image={'assets/kcs2/resources/furniture/normal/494_1648.png'} y={415.5} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/502_8118.png'} />
            <Sprite image={'assets/kcs2/resources/furniture/outside/window_bg_4-2.png'} x={300} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/491_9688.png'} x={300} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/499_8458.png'} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/493_4897.png'} y={200} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/498_8534.png'} x={870} />
            {/* 舰娘 */}
            <Sprite image={`assets/kcs2/resources/ship/full/0${flagShip_prefix}_${flagShip_inner}_${flagShip_suffix}.png`} x={400} y={100} />
        </Container>
    );
};