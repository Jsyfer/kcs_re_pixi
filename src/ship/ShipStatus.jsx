import { Container, Sprite, Text } from '@pixi/react';
import { useCallback } from 'react';
import * as AssetsFactory from '../common/AssetsFactory';
import { PixiButton } from '../common/PixiButton';
import resouces_mapping from '../resources_mapping.json';
import { ShipHp } from './ShipHp';
import { ShipExp } from './ShipExp';
import { ShipPowerUpStatus } from './ShipPowerUpStatus';

export const ShipStatus = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const remodelMain = AssetsFactory.getSpritesheet("kcs2/img/remodel/remodel_main.json")

    const target_ship = props.api_ship.find(item => item.api_id === props.fleet[props.shipIndex]);
    const target_ship_base_info = props.getData.api_data.api_mst_ship.find(item => item.api_id === target_ship.api_ship_id);
    const ship_card_img = 'kcs2/resources/ship/card/' + resouces_mapping.ship.find(item => item.api_id === target_ship.api_ship_id).card;


    const render = useCallback(() => {
        if (props.editable) {
            return <>
                <Sprite texture={remodelMain[32]} x={10} y={130} />
                <Sprite texture={remodelMain[51]} x={13} y={374} />
                <PixiButton default={remodelMain[4]} hover={remodelMain[5]} x={360} y={520} />
                <PixiButton default={remodelMain[8]} hover={remodelMain[9]} disabled={remodelMain[7]} isDisabled={false} x={540} y={520} />
            </>
        } else {
            return <>
                {/* EXP (wrap in component)*/}
                <ShipExp commonMain={commonMain} exp={target_ship.api_exp} x={241} y={87} />
            </>
        }
    })
    return (
        <Container x={props.x} y={props.y}>
            {/* 艦船ステータス */}
            <Sprite texture={commonMain[67]} x={0} y={0} />
            <Sprite texture={commonMain[13]} x={0} y={36} />
            <Sprite texture={commonMain[2]} x={32} y={8} />

            {/* name */}
            <Text text={target_ship_base_info.api_name} x={50} y={55} style={{ fontSize: 28 }} />
            {/* Lv */}
            <Sprite texture={commonMisc[186]} x={230} y={60} />
            <Text text={target_ship.api_lv} x={260} y={52} style={{ fontSize: 32 }} />
            {/* HP */}
            <ShipHp maxhp={target_ship.api_maxhp} nowhp={target_ship.api_nowhp} x={50} y={110} />
            <Text text={target_ship.api_maxhp + "/" + target_ship.api_nowhp} x={210} y={102} anchor={{ x: 1, y: 0 }} style={{ fontSize: 16 }} />
            {/* Ship power up status */}
            <ShipPowerUpStatus texture={commonMain[53]} target_ship={target_ship} x={220} y={102} />

            {/* 装備 */}
            <Sprite texture={commonMain[46]} x={50} y={140} />

            {/* 詳細ステータス */}
            <Sprite texture={commonMain[16]} x={40} y={386} />
            {/* ship card */}
            <Sprite image={ship_card_img} x={360} y={60} />
            {render()}
        </Container>
    );
};