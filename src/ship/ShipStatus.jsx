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
    const commonIconWeapon = AssetsFactory.getSpritesheet("kcs2/img/common/common_icon_weapon.json")
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
    }, [props.editable, remodelMain, target_ship.api_exp, commonMain])


    const renderSlot = useCallback(() => {
        return target_ship.api_slot.map((equipment, index) => {
            // 装備なし
            if (equipment === -1) {
                if (index < target_ship.api_slotnum) return <Sprite key={index} texture={commonMain[46]} x={50} y={140 + 47 * index} />;
                if (index === 4) return null
                return <Sprite key={index} texture={commonMain[47]} x={50} y={140 + 47 * index} />;
            }
            // 装備あり
            const api_slotitem_id = props.requireInfo.api_data.api_slot_item.find(item => item.api_id === equipment).api_slotitem_id;
            const equipment_info = props.getData.api_data.api_mst_slotitem.find(item => item.api_id === api_slotitem_id);
            return (
                <Container key={index}>
                    {/* 装備スロット */}
                    <Sprite texture={commonMain[46]} x={50} y={140 + 47 * index} />
                    {/* 装備アイコン */}
                    <Sprite texture={commonIconWeapon[equipment_info.api_type[3] - 1]} anchor={0.5} x={73} y={162 + 47 * index} />
                    {/* 装備名 */}
                    <Text text={equipment_info.api_name} x={100} y={152 + 47 * index} style={{ fontSize: 16 }} />
                    {/* 装備数（艦載機の場合のみ） */}
                    <Text text={target_ship.api_onslot[index]} anchor={{ x: 1, y: 0 }} x={45} y={152 + 47 * index} style={{ fontSize: 16 }} />
                </Container>
            );
        });
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
            {renderSlot()}

            {/* 詳細ステータス */}
            <Sprite texture={commonMain[16]} x={40} y={386} />
            {/* ship card */}
            <Sprite image={ship_card_img} x={360} y={60} />
            {render()}
        </Container>
    );
};