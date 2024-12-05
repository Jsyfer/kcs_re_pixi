import { useCallback } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
// import { PixiButton } from '../../../common/PixiButton';
import { Graphics } from 'pixi.js'
import * as AssetsFactory from '../../../common/AssetsFactory';
import resouces_mapping from '../../../resources_mapping.json';
import { ShipHp } from '../../../ship/ShipHp';
import { ShipPowerUpStatus } from '../../../ship/ShipPowerUpStatus';

export const SupplyCard = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const supplyMain = AssetsFactory.getSpritesheet("kcs2/img/supply/supply_main.json")

    const render_card = useCallback(() => {
        if (props.fleet[props.shipIndex] === -1) {
            return <Sprite texture={commonMain[20]} x={0} y={0} />
        } else {
            const target_ship = props.api_ship.find(item => item.api_id === props.fleet[props.shipIndex]);
            const target_ship_base_info = props.getData.api_data.api_mst_ship.find(item => item.api_id === target_ship.api_ship_id);
            const ship_supply_img = 'kcs2/resources/ship/supply_character/' + resouces_mapping.ship.find(item => item.api_id === target_ship.api_ship_id).supply_character;

            const shipNameMask = new Graphics();
            shipNameMask.beginFill(0xFF3300);
            shipNameMask.drawRect(props.x, props.y, 370, 50);
            shipNameMask.endFill();

            return <>
                {/* ship supply image */}
                <Sprite image={ship_supply_img} x={0} y={0} />
                {/* position number */}
                <Sprite texture={commonMisc["" + 3 + props.shipIndex]} x={15} y={18} />
                {/* 船基本情報 */}
                <Sprite texture={commonMain[19]} x={252} y={8} />
                {/* name */}
                <Text text={target_ship_base_info.api_name} x={262} y={16} style={{ fill: 'white', fontSize: 28 }} mask={shipNameMask} />
                {/* Lv */}
                <Text text={target_ship.api_lv} x={458} y={16} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 28 }} />
                {/* HP */}
                <ShipHp x={268} y={53} maxhp={target_ship.api_maxhp} nowhp={target_ship.api_nowhp} />
                {/* Ship power up status */}
                <ShipPowerUpStatus texture={commonMain[53]} target_ship={target_ship} x={374} y={46} />

                {/* 燃料・弾薬 */}
                <Sprite texture={supplyMain[25]} x={478} y={8} />
                <Sprite texture={commonMisc[130]} x={490} y={15} />
                <Sprite texture={commonMisc[130]} x={596} y={15} />

            </>
        }
    })

    return (
        <Container x={props.x} y={props.y}>
            {render_card()}
        </Container>
    );
};