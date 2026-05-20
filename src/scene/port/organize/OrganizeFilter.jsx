import { useCallback, useEffect, useState } from 'react';
import { Container, Sprite, Graphics } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import { ShipCard } from '@ship/ShipCard';
import { Paging } from '@common/Paging';
import { PixiButton } from '@common/PixiButton';
import { CheckboxButton } from '@/common/CheckboxButton';
import { ShipDetails } from '@ship/ShipDetails';
import { useStore } from "@common/StoreFactory"
import '@pixi/events';
import { SelectButton } from '@/common/SelectButton';

// 艦船選択Filter
export const OrganizeFilter = (props) => {
    const portData = useStore(state => state.portData)

    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const organizeFilter = AssetsFactory.getSpritesheet("kcs2/img/organize/organize_filter.json")
    const [filterDisplayAsJp, setFilterDisplayAsJp] = useState(false);
    const [filterDisplayOffset, setFilterDisplayOffset] = useState(2);
    // BB/BC 戦艦級フィルターの選択状態
    const [BBBCSelected, setBBBCSelected] = useState(true);
    // CV/CVL 航空母艦フィルターの選択状態
    const [CVCVLSelected, setCVCVLSelected] = useState(true);
    // CA 重巡級フィルターの選択状態
    const [CASelected, setCASelected] = useState(true);
    // CL 軽巡級フィルターの選択状態
    const [CLSelected, setCLSelected] = useState(true);
    // DD 駆逐艦フィルターの選択状態
    const [DDSelected, setDDSelected] = useState(true);
    // DE 海防艦フィルターの選択状態
    const [DESelected, setDESelected] = useState(true);
    // SS 潜水艦フィルターの選択状態
    const [SSSelected, setSSSelected] = useState(true);
    // AV/AO/AS 補助艦艇フィルターの選択状態
    const [AVAOASSelected, setAVAOASSelected] = useState(true);
    // filter一括ON/OFFの選択状態
    const [allFilterSelected, setAllFilterSelected] = useState(true);

    useEffect(() => {
        setFilterDisplayOffset(filterDisplayAsJp ? 0 : 2);
    }, [filterDisplayAsJp])

    useEffect(() => {
        const newValue = BBBCSelected && CVCVLSelected && CASelected && CLSelected && DDSelected && DESelected && SSSelected && AVAOASSelected;
        setAllFilterSelected(newValue);
    }, [BBBCSelected, CVCVLSelected, CASelected, CLSelected, DDSelected, DESelected, SSSelected, AVAOASSelected])

    const handleAllFilter = useCallback(() => {
        setAllFilterSelected(!allFilterSelected);
        setBBBCSelected(!allFilterSelected);
        setCVCVLSelected(!allFilterSelected);
        setCASelected(!allFilterSelected);
        setCLSelected(!allFilterSelected);
        setDDSelected(!allFilterSelected);
        setDESelected(!allFilterSelected);
        setSSSelected(!allFilterSelected);
        setAVAOASSelected(!allFilterSelected);
    }, [allFilterSelected])

    return (
        <Container eventMode={"static"} x={props.x} y={props.y}>
            {/* 背景オーバーレイ */}
            <Graphics
                eventMode={"static"}
                pointerup={() => { props.setSelectedOrganizeFilter(false) }}
                draw={(g) => {
                    g.clear();
                    g.beginFill(0x000000, 0.5);
                    g.drawRect(-470, 0, 1280, 720);
                    g.endFill();
                }}
            />
            {/* 背景 */}
            <Sprite texture={organizeFilter[6]} x={52} y={36} />
            {/* タイトル背景 */}
            <Sprite texture={organizeFilter[50]} x={52} y={0} />
            {/* タイトル（艦船選択） */}
            <Sprite texture={commonMain[1]} x={80} y={10} />
            {/* Filter Display Language */}
            <Sprite texture={organizeFilter[52]} x={108} y={72} />
            <CheckboxButton
                x={110}
                y={74}
                default={organizeFilter[53]}
                selected={organizeFilter[54]}
                isSelected={filterDisplayAsJp}
                action={() => setFilterDisplayAsJp(!filterDisplayAsJp)}
            />
            {/* BB/BC 戦艦級 */}
            <CheckboxButton
                x={130}
                y={47}
                default={organizeFilter[17 + filterDisplayOffset]}
                selected={organizeFilter[16 + filterDisplayOffset]}
                isSelected={BBBCSelected}
                action={() => setBBBCSelected(!BBBCSelected)}
            />
            {/* CV/CVL 航空母艦 */}
            <CheckboxButton
                x={196}
                y={47}
                default={organizeFilter[21 + filterDisplayOffset]}
                selected={organizeFilter[20 + filterDisplayOffset]}
                isSelected={CVCVLSelected}
                action={() => setCVCVLSelected(!CVCVLSelected)}
            />
            {/* CA 重巡級 */}
            <CheckboxButton
                x={262}
                y={47}
                default={organizeFilter[25 + filterDisplayOffset]}
                selected={organizeFilter[24 + filterDisplayOffset]}
                isSelected={CASelected}
                action={() => setCASelected(!CASelected)}
            />
            {/* CL 軽巡級 */}
            <CheckboxButton
                x={326}
                y={47}
                default={organizeFilter[29 + filterDisplayOffset]}
                selected={organizeFilter[28 + filterDisplayOffset]}
                isSelected={CLSelected}
                action={() => setCLSelected(!CLSelected)}
            />
            {/* DD 駆逐艦 */}
            <CheckboxButton
                x={390}
                y={47}
                default={organizeFilter[33 + filterDisplayOffset]}
                selected={organizeFilter[32 + filterDisplayOffset]}
                isSelected={DDSelected}
                action={() => setDDSelected(!DDSelected)}
            />
            {/* DE 海防艦 */}
            <CheckboxButton
                x={454}
                y={47}
                default={organizeFilter[37 + filterDisplayOffset]}
                selected={organizeFilter[36 + filterDisplayOffset]}
                isSelected={DESelected}
                action={() => setDESelected(!DESelected)}
            />
            {/* SS 潜水艦 */}
            <CheckboxButton
                x={518}
                y={47}
                default={organizeFilter[41 + filterDisplayOffset]}
                selected={organizeFilter[40 + filterDisplayOffset]}
                isSelected={SSSelected}
                action={() => setSSSelected(!SSSelected)}
            />
            {/* AV/AO/AS 補助艦艇 */}
            <CheckboxButton
                x={582}
                y={47}
                default={organizeFilter[45 + filterDisplayOffset]}
                selected={organizeFilter[44 + filterDisplayOffset]}
                isSelected={AVAOASSelected}
                action={() => setAVAOASSelected(!AVAOASSelected)}
            />
            {/* 一括ON/OFF */}
            <Sprite x={652} y={47} texture={organizeFilter[8]} />
            <CheckboxButton
                x={657}
                y={51}
                default={organizeFilter[7]}
                selected={organizeFilter[9]}
                isSelected={allFilterSelected}
                action={() => handleAllFilter()}
            />

            {/* リストヘッダー */}
            <Sprite texture={organizeFilter[4]} x={115} y={80} />
            {/* Sort Button */}
            <SelectButton textureList={[organizeFilter[14], organizeFilter[13], organizeFilter[12], organizeFilter[15], organizeFilter[11], organizeFilter[10]]} x={650} y={75} />

            <Paging x={165} y={560} totalPage={30} />
            {/* はずす */}
            <PixiButton default={organizeFilter[48]} hover={organizeFilter[49]} down={organizeFilter[49]} x={652} y={555} />
        </Container>
    );
};