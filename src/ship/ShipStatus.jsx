import { Container, Sprite, Text } from '@pixi/react';
import { useCallback } from 'react';
import { Graphics } from 'pixi.js'
import * as AssetsFactory from '../common/AssetsFactory';
import { PixiButton } from '../common/PixiButton';
import { useStore } from '../common/StoreFactory';
import resouces_mapping from '../resources_mapping.json';
import { ShipHp } from './ShipHp';
import { ShipExp } from './ShipExp';
import { ShipPowerUpStatus } from './ShipPowerUpStatus';

export const ShipStatus = (props) => {
    const getData = useStore(state => state.getData);
    const requireInfo = useStore((state) => state.requireInfo)

    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const commonIconWeapon = AssetsFactory.getSpritesheet("kcs2/img/common/common_icon_weapon.json")
    const remodelMain = AssetsFactory.getSpritesheet("kcs2/img/remodel/remodel_main.json")

    const target_ship = props.api_ship.find(item => item.api_id === props.fleet[props.shipIndex]);
    const target_ship_base_info = getData.api_data.api_mst_ship.find(item => item.api_id === target_ship.api_ship_id);
    const ship_card_img = 'kcs2/resources/ship/card/' + resouces_mapping.ship.find(item => item.api_id === target_ship.api_ship_id).card;

    const shipNameMask = new Graphics();
    shipNameMask.beginFill(0xFF3300);
    shipNameMask.drawRect(props.x, props.y, 225, 100);
    shipNameMask.endFill();

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
                {/* 次のLv.まで EXP*/}
                <Sprite texture={commonMain[68]} x={354} y={512} />
                <ShipExp exp={target_ship.api_exp} x={442} y={517} />
                <Text text={target_ship.api_exp[1]} x={400} y={528} style={{ fontSize: 18 }} />
                {/* TODO 補給/補強/緊急用装備 */}
                {target_ship.api_slot_ex === 0 ? null : <>
                    <Sprite texture={commonMain[69]} x={520} y={535} />
                    <Sprite texture={commonMain[47]} x={395} y={550} />
                </>
                }
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
            const equipment_info = requireInfo.api_data.api_slot_item.find(item => item.api_id === equipment);
            const equipment_base_info = getData.api_data.api_mst_slotitem.find(item => item.api_id === equipment_info.api_slotitem_id);

            return (
                <Container key={index}>
                    {/* 装備スロット */}
                    <Sprite texture={commonMain[46]} x={50} y={140 + 47 * index} />
                    {/* 装備アイコン */}
                    <Sprite texture={commonIconWeapon[equipment_base_info.api_type[3] - 1]} anchor={0.5} x={73} y={162 + 47 * index} />
                    {/* 装備名 */}
                    <Text text={equipment_base_info.api_name} x={100} y={152 + 47 * index} style={{ fontSize: 18 }} />
                    <Sprite texture={commonMain[45]} x={222} y={147 + 47 * index} />
                    {/* 装備数（艦載機の場合のみ） */}
                    <Text text={target_ship.api_onslot[index]} anchor={{ x: 1, y: 0 }} x={45} y={152 + 47 * index} style={{ fontSize: 16 }} />
                    {/* 艦載機熟練度 */}
                    {equipment_info.api_alv && equipment_info.api_alv > 0 ? <Sprite texture={commonMisc[172 + equipment_info.api_alv]} x={260} y={142 + 47 * index} /> : null}
                    {/* 改修レベル */}
                    {equipment_info.api_level > 0 ?
                        equipment_info.api_level === 10 ?
                            <Sprite texture={commonMain[32]} x={305} y={148 + 47 * index} />
                            :
                            <>
                                <Sprite texture={commonMain[31]} x={298} y={153 + 47 * index} scale={1.4} />
                                <Sprite texture={commonMain[30]} x={315} y={156 + 47 * index} />
                                <Text text={equipment_info.api_level} style={{ fontSize: 22, fill: 0x45a9a5 }} x={328} y={150 + 47 * index} />
                            </>
                        : null}
                    {/* ロック状態 */}
                    {equipment_info.api_locked === 1 ? <Sprite texture={commonMain[42]} x={343} y={142 + 47 * index} /> : null}
                    {/* クリアボタン */}
                    {props.editable ? <Sprite texture={remodelMain[51]} x={342} y={155 + 47 * index} /> : null}
                </Container>
            );
        });
    })

    const renderSoku = useCallback(() => {
        switch (target_ship.api_soku) {
            case 20:
                // 最速
                return <Sprite texture={commonMain[62]} anchor={0.5} x={155} y={538} />
            case 15:
                // 高速+
                return <Sprite texture={commonMain[57]} anchor={0.5} x={155} y={538} />
            case 10:
                // 高速
                return <Sprite texture={commonMain[56]} anchor={0.5} x={155} y={538} />
            default:
                // 低速
                return <Sprite texture={commonMain[59]} anchor={0.5} x={155} y={538} />
        }
    })

    const renderLeng = useCallback(() => {
        switch (target_ship.api_leng) {
            case 4:
                // 超長
                return <Sprite texture={commonMain[65]} anchor={0.5} x={155} y={572} />
            case 3:
                // 長
                return <Sprite texture={commonMain[58]} anchor={0.5} x={155} y={572} />
            case 2:
                // 中
                return <Sprite texture={commonMain[60]} anchor={0.5} x={155} y={572} />
            default:
                // 短
                return <Sprite texture={commonMain[64]} anchor={0.5} x={155} y={572} />
        }
    })

    return (
        <Container x={props.x} y={props.y}>
            {/* 艦船ステータス */}
            <Sprite texture={commonMain[67]} x={0} y={0} />
            <Sprite texture={commonMain[13]} x={0} y={36} />
            <Sprite texture={commonMain[2]} x={32} y={8} />

            {/* name */}
            <Text text={target_ship_base_info.api_name} x={50} y={55} style={{ fontSize: 28 }} mask={shipNameMask} />
            {/* Lv */}
            <Sprite texture={commonMisc[186]} x={230} y={60} />
            <Text text={target_ship.api_lv} x={255} y={52} style={{ fontSize: 32 }} />
            {/* 改修MAXアイコン */}
            {target_ship.api_karyoku[0] >= target_ship.api_karyoku[1] && target_ship.api_raisou[0] >= target_ship.api_raisou[1] && target_ship.api_taiku[0] >= target_ship.api_taiku[1] && target_ship.api_soukou[0] >= target_ship.api_soukou[1] ?
                <Sprite texture={commonMain[29]} x={310} y={50} />
                : null}

            {/* HP */}
            <ShipHp maxhp={target_ship.api_maxhp} nowhp={target_ship.api_nowhp} x={50} y={110} />
            <Text text={target_ship.api_maxhp + "/" + target_ship.api_nowhp} x={210} y={102} anchor={{ x: 1, y: 0 }} style={{ fontSize: 16 }} />
            {/* Ship power up status */}
            <ShipPowerUpStatus texture={commonMain[53]} target_ship={target_ship} x={220} y={102} />

            {/* 装備 */}
            {renderSlot()}

            {/* 詳細ステータス */}
            <Sprite texture={commonMain[16]} x={40} y={386} />
            {/* 耐久 */}
            <Text text={target_ship.api_maxhp} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={180} y={390} />
            {/* 装甲 */}
            <Text text={target_ship.api_soukou[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={180} y={424} />
            {/* 回避 */}
            <Text text={target_ship.api_kaihi[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={180} y={458} />
            {/* 搭載 */}
            <Text text={target_ship_base_info.api_maxeq.reduce((partialSum, a) => partialSum + a, 0)} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={180} y={492} />
            {/* 速力 */}
            {renderSoku()}
            {/* 射程 */}
            {renderLeng()}
            {/* 火力 */}
            <Text text={target_ship.api_karyoku[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={330} y={390} />
            {/* 雷装 */}
            <Text text={target_ship.api_raisou[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={330} y={424} />
            {/* 対空 */}
            <Text text={target_ship.api_taiku[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={330} y={458} />
            {/* 対潜 */}
            <Text text={target_ship.api_taisen[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={330} y={492} />
            {/* 索敵 */}
            <Text text={target_ship.api_sakuteki[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={330} y={526} />
            {/* 運 */}
            <Text text={target_ship.api_lucky[0]} anchor={{ x: 1, y: 0 }} style={{ fontSize: 22 }} x={330} y={560} />
            {/* ship card */}
            <Sprite image={ship_card_img} x={360} y={60} />
            {render()}
        </Container>
    );
};