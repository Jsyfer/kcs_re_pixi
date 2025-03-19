import { useCallback } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import { PixiButton } from '../common/PixiButton';
import { Graphics } from 'pixi.js'
import * as AssetsFactory from '../common/AssetsFactory';
import { useStore } from '../common/StoreFactory';
import resouces_mapping from '../resources_mapping.json';
import { ShipHp } from './ShipHp';
import { ShipExp } from './ShipExp';
import { ShipPowerUpStatus } from './ShipPowerUpStatus';

export const ShipCard = (props) => {
    const getData = useStore(state => state.getData);
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const organizeMain = AssetsFactory.getSpritesheet("kcs2/img/organize/organize_main.json")

    const render_card = useCallback(() => {
        if (props.fleet[props.shipIndex] === -1) {
            return <>
                <Sprite texture={organizeMain[31]} x={0} y={0} />
                <Sprite texture={organizeMain[32]} x={246} y={0} />
            </>
        } else {
            const target_ship = props.api_ship.find(item => item.api_id === props.fleet[props.shipIndex]);
            const target_ship_base_info = getData.api_data.api_mst_ship.find(item => item.api_id === target_ship.api_ship_id);
            const ship_banner_img = 'kcs2/resources/ship/banner/' + resouces_mapping.ship.find(item => item.api_id === target_ship.api_ship_id).banner;

            const shipNameMask = new Graphics();
            shipNameMask.beginFill(0xFF3300);
            shipNameMask.drawRect(props.x, props.y, 125, 100);
            shipNameMask.endFill();

            return <>
                {/* background */}
                <Sprite texture={organizeMain[30]} x={0} y={0} />
                {/* position number */}
                <Sprite texture={commonMisc["" + 3 + props.shipIndex]} x={-15} y={0} />

                {/* name */}
                <Text text={target_ship_base_info.api_name} x={24} y={18} style={{ fill: 'white', fontSize: 34 }} mask={shipNameMask} />

                {/* Lv */}
                <Text text={target_ship.api_lv} x={235} y={20} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 22 }} />

                {/* Ship power up status */}
                <ShipPowerUpStatus texture={commonMain[53]} target_ship={target_ship} x={20} y={60} />

                {/* HP */}
                <Text text={target_ship.api_maxhp + "/" + target_ship.api_nowhp} x={230} y={64} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 16 }} />
                <ShipHp x={134} y={56} maxhp={target_ship.api_maxhp} nowhp={target_ship.api_nowhp} />

                {/* ship banner */}
                <Sprite image={ship_banner_img} x={244} y={18} />

                {/* EXP (wrap in component)*/}
                <ShipExp commonMain={commonMain} exp={target_ship.api_exp} x={241} y={87} />

                {/* 火力 */}
                <Text text={target_ship.api_karyoku[0]} x={118} y={89} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 18 }} />
                {/* 雷装 */}
                <Text text={target_ship.api_raisou[0]} x={118} y={119} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 18 }} />
                {/* 対空 */}
                <Text text={target_ship.api_taiku[0]} x={232} y={89} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 18 }} />
                {/* 装甲 */}
                <Text text={target_ship.api_soukou[0]} x={232} y={119} anchor={{ x: 1, y: 0 }} style={{ fill: 'white', fontSize: 18 }} />

                {/* 詳細 */}
                <PixiButton
                    default={organizeMain[9]}
                    hover={organizeMain[10]}
                    action={() => { props.setSelectedShipIndex(props.shipIndex) }}
                    x={250} y={103}
                />
            </>
        }
    })

    return (
        <Container x={props.x} y={props.y}>
            {render_card()}
            {
                (props.lastShipIndex === -1 || props.lastShipIndex >= props.shipIndex) ?
                    // 変更
                    <PixiButton
                        default={organizeMain[24]}
                        hover={organizeMain[25]}
                        x={378} y={103}
                    />
                    :
                    null
            }
        </Container>
    );
};