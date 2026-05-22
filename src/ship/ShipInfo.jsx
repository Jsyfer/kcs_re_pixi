import { useCallback } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import { useStore } from '@common/StoreFactory';
import resouces_mapping from '@/resources_mapping.json';
import * as PIXI from 'pixi.js';
import { ShipHp } from '@ship/ShipHp';
import { getShipType, getShipSpeed } from '@ship/shipCommon';
import { CheckboxButton } from '@/common/CheckboxButton';

// 艦船Info（編成Filter）
export const ShipInfo = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const organizeMain = AssetsFactory.getSpritesheet("kcs2/img/organize/organize_main.json")
    const getData = useStore(state => state.getData)

    const target_ship_base_info = getData.api_data.api_mst_ship.find(item => item.api_id === props.ship.api_ship_id);

    const shipNameMask = new PIXI.Graphics();
    shipNameMask.beginTextureFill({ texture: commonMain[43] });
    shipNameMask.drawRect(props.x, props.y, 141, 43);
    shipNameMask.endFill();

    return (
        <Container x={props.x} y={props.y}>
            {/* 艦種／艦船名 */}
            <Text
                x={8} y={0}
                text={getShipType(target_ship_base_info.api_stype) + ' ' + target_ship_base_info.api_name}
                style={{ fill: 'black', fontSize: 20 }}
                mask={shipNameMask}
            />
            {/* 練度(Lv) */}
            <Text
                x={280} y={0}
                text={props.ship.api_lv}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 20 }}
            />
            {/* 耐久 */}
            <Text
                x={340} y={0}
                text={props.ship.api_nowhp}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            {/* 火力 */}
            <Text
                x={385} y={0}
                text={props.ship.api_karyoku[0]}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            {/* 雷装 */}
            <Text
                x={435} y={0}
                text={props.ship.api_raisou[0]}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            {/* 対空 */}
            <Text
                x={480} y={0}
                text={props.ship.api_taiku[0]}
                anchor={{ x: 1, y: 0 }}
                style={{ fill: 'black', fontSize: 18 }}
            />
            <Sprite texture={commonMain[getShipSpeed(props.ship.api_soku)]} anchor={{ x: 1, y: 0 }} x={535} y={0} />
            {/* HP bar */}
            <ShipHp nowhp={props.ship.api_nowhp} maxhp={props.ship.api_maxhp} x={493} y={25} />
            <CheckboxButton
                x={535} y={-13}
                default={organizeMain[45]}
                selected={organizeMain[45]}
                hover={organizeMain[44]}
                isDefaultTextureTransparent={true}
                isSelected={props.ship.api_locked === 1}
            />

        </Container>
    );
};