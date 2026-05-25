import { Fragment, useCallback, useEffect, useState } from 'react';
import { Container, Sprite, Graphics } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import { Paging } from '@common/Paging';
import { PixiButton } from '@common/PixiButton';
import { CheckboxButton } from '@/common/CheckboxButton';
import { useStore } from "@common/StoreFactory"
import '@pixi/events';
import { SelectButton } from '@/common/SelectButton';
import { ShipInfo } from '@/ship/ShipInfo';

// 艦船選択Filter
export const OrganizeFilter = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const organizeFilter = AssetsFactory.getSpritesheet("kcs2/img/organize/organize_filter.json")

    const getData = useStore(state => state.getData)
    const portData = useStore(state => state.portData);

    // 艦種順（デフォルト）でソートされた艦船リスト
    const [sortedShipList, setSortedShipList] = useState(portData.api_data.api_ship.sort((a, b) => getData.api_data.api_mst_ship.find(item => item.api_id === b.api_ship_id).api_stype - getData.api_data.api_mst_ship.find(item => item.api_id === a.api_ship_id).api_stype));
    // 艦船リスト
    const [totalShipList, setTotalShipList] = useState(sortedShipList);
    const [currentPageList, setCurrentPageList] = useState(totalShipList.slice(0, 10));
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
        const newList = sortedShipList.filter((target_ship) => {
            const target_ship_base_info = getData.api_data.api_mst_ship.find(item => item.api_id === target_ship.api_ship_id);
            if (BBBCSelected && [8, 9, 10].includes(target_ship_base_info.api_stype)) return true;
            if (CVCVLSelected && [7, 11, 18].includes(target_ship_base_info.api_stype)) return true;
            if (CASelected && [5, 6].includes(target_ship_base_info.api_stype)) return true;
            if (CLSelected && [3, 4, 21].includes(target_ship_base_info.api_stype)) return true;
            if (DDSelected && [2].includes(target_ship_base_info.api_stype)) return true;
            if (DESelected && [1].includes(target_ship_base_info.api_stype)) return true;
            if (SSSelected && [13, 14].includes(target_ship_base_info.api_stype)) return true;
            if (AVAOASSelected && [16, 17, 19, 20, 22].includes(target_ship_base_info.api_stype)) return true;
        })
        setTotalShipList(newList);
        setCurrentPageList(newList.slice(0, 10));
    }, [sortedShipList, BBBCSelected, CVCVLSelected, CASelected, CLSelected, DDSelected, DESelected, SSSelected, AVAOASSelected])

    // 艦種フィルターの選択状態に応じて、言語表示のオフセットを更新
    useEffect(() => {
        setFilterDisplayOffset(filterDisplayAsJp ? 0 : 2);
    }, [filterDisplayAsJp])

    // 艦種フィルターの選択状態に応じて、filter一括ON/OFFの状態を更新
    useEffect(() => {
        const newValue = BBBCSelected && CVCVLSelected && CASelected && CLSelected && DDSelected && DESelected && SSSelected && AVAOASSelected;
        setAllFilterSelected(newValue);
    }, [BBBCSelected, CVCVLSelected, CASelected, CLSelected, DDSelected, DESelected, SSSelected, AVAOASSelected])

    // filter一括ON/OFFの選択状態に応じて、艦種フィルターの選択状態を更新
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

    // sort
    const handleSort = useCallback((currentValue) => {
        console.log("Selected sort option:", currentValue);
        switch (currentValue) {
            case 1:
                // 入手順
                setSortedShipList(prevValue => [...prevValue].sort((a, b) => b.api_id - a.api_id));
                break;
            case 2:
                // HP残量順
                setSortedShipList(prevValue => [...prevValue].sort((a, b) => (a.api_nowhp / a.api_maxhp) - (b.api_nowhp / b.api_maxhp)));
                break;
            case 3:
                // 修理時間順
                setSortedShipList(prevValue => [...prevValue].sort((a, b) => b.api_ndock_time - a.api_ndock_time));
                break;
            case 4:
                // TODO 闪　ステータス順
                setSortedShipList(prevValue => [...prevValue].sort((a, b) => a.api_cond - b.api_cond));
            case 5:
                // TODO レベル順
                setSortedShipList(prevValue => [...prevValue].sort((a, b) => b.api_lv - a.api_lv));
            default:
                // TODO 艦種順（デフォルト）
                setSortedShipList(prevValue => [...prevValue].sort((a, b) => getData.api_data.api_mst_ship.find(item => item.api_id === b.api_ship_id).api_stype - getData.api_data.api_mst_ship.find(item => item.api_id === a.api_ship_id).api_stype));
                break;
        }
    }, [])

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
            <SelectButton
                x={650} y={75}
                textureList={[organizeFilter[14], organizeFilter[13], organizeFilter[12], organizeFilter[15], organizeFilter[11], organizeFilter[10]]}
                action={(currentValue) => handleSort(currentValue)}
            />

            {/* ship list */}
            {
                currentPageList.map((ship, index) => {
                    return <Fragment key={ship.api_id ?? index}>
                        <ShipInfo ship={ship} x={115} y={125 + index * 43} />
                        <Sprite texture={organizeFilter[5]} x={115} y={158 + index * 43} />
                    </Fragment>
                })
            }
            {/* 選択候補はありません */}
            {
                currentPageList.length === 0 &&
                <Sprite texture={organizeFilter[51]} x={290} y={310} />
            }

            <Paging x={165} y={560} setCurrentPageList={setCurrentPageList} dataList={totalShipList} />
            {/* はずす */}
            <PixiButton default={organizeFilter[48]} hover={organizeFilter[49]} down={organizeFilter[49]} x={652} y={555} />
        </Container>
    );
};
