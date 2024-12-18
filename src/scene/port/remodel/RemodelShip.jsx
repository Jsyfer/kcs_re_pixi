import { useCallback, useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import resouces_mapping from '../../../resources_mapping.json';
import * as AssetsFactory from '../../../common/AssetsFactory';

export const RemodelShip = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const remodelMain = AssetsFactory.getSpritesheet("kcs2/img/remodel/remodel_main.json")

    const render = useCallback(() => {
        if (props.fleet[props.shipIndex] === -1) {
            return <Sprite texture={remodelMain[18]} x={28} y={18} />
        } else {
            const target_ship = props.api_ship.find(item => item.api_id === props.fleet[props.shipIndex]);
            const target_ship_base_info = props.getData.api_data.api_mst_ship.find(item => item.api_id === target_ship.api_ship_id);
            const ship_banner_img = 'kcs2/resources/ship/banner/' + resouces_mapping.ship.find(item => item.api_id === target_ship.api_ship_id).banner;
            return <>
                {/* position number */}
                <Sprite texture={commonMisc["" + 3 + props.shipIndex]} x={-22} y={25} />
                <Sprite image={ship_banner_img} x={28} y={18} />
                {props.selectedShipIndex === props.shipIndex ? <Sprite texture={remodelMain[22]} x={28} y={13} /> : null}
            </>
        }
    })

    return (
        <Container x={props.x} y={props.y}>
            {render()}
            <Sprite texture={remodelMain[46]} x={0} y={0} />
        </Container>
    );
};