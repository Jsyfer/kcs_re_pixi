import { useCallback, useEffect, useState } from 'react';
import { Container, Sprite, Graphics } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import { ShipCard } from '@ship/ShipCard';
import { PixiButton } from '@common/PixiButton';
import { RadioButton } from '@common/RadioButton';
import { CheckboxButton } from '@/common/CheckboxButton';
import { ShipDetails } from '@ship/ShipDetails';
import { useStore } from "@common/StoreFactory"
import '@pixi/events';

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

    useEffect(() => {
        setFilterDisplayOffset(filterDisplayAsJp ? 0 : 2);
    }, [filterDisplayAsJp])

    return (
        <Container x={0} y={0}>
            {/* 背景オーバーレイ */}
            <Graphics
                eventMode={"static"}
                pointerup={() => { props.setSelectedOrganizeFilter(false) }}
                draw={(g) => {
                    g.clear();
                    g.beginFill(0x000000, 0.5);
                    g.drawRect(0, 0, 1280, 720);
                    g.endFill();
                }}
            />
            {/* 背景 */}
            <Sprite texture={organizeFilter[6]} x={522} y={140} />
            {/* タイトル背景 */}
            <Sprite texture={organizeFilter[48]} x={522} y={104} />
            {/* タイトル（艦船選択） */}
            <Sprite texture={commonMain[1]} x={550} y={114} />
            {/* Filter Display Language */}
            <Sprite texture={organizeFilter[50]} x={578} y={176} />
            <CheckboxButton
                x={580}
                y={178}
                default={organizeFilter[51]}
                selected={organizeFilter[52]}
                isSelected={filterDisplayAsJp}
                action={() => setFilterDisplayAsJp(!filterDisplayAsJp)}
            />
            {/* BB/BC 戦艦級 */}
            <CheckboxButton
                x={600}
                y={151}
                default={organizeFilter[15 + filterDisplayOffset]}
                selected={organizeFilter[14 + filterDisplayOffset]}
                isSelected={BBBCSelected}
                action={() => setBBBCSelected(!BBBCSelected)}
            />
            {/* CV/CVL 航空母艦 */}
            <CheckboxButton
                x={665}
                y={151}
                default={organizeFilter[19 + filterDisplayOffset]}
                selected={organizeFilter[18 + filterDisplayOffset]}
                isSelected={CVCVLSelected}
                action={() => setCVCVLSelected(!CVCVLSelected)}
            />
            {/* CA 重巡級 */}
            <CheckboxButton
                x={730}
                y={151}
                default={organizeFilter[23 + filterDisplayOffset]}
                selected={organizeFilter[22 + filterDisplayOffset]}
                isSelected={CASelected}
                action={() => setCASelected(!CASelected)}
            />
            {/* CL 軽巡級 */}
            <CheckboxButton
                x={795}
                y={151}
                default={organizeFilter[27 + filterDisplayOffset]}
                selected={organizeFilter[26 + filterDisplayOffset]}
                isSelected={CLSelected}
                action={() => setCLSelected(!CLSelected)}
            />
            {/* DD 駆逐艦 */}
            <CheckboxButton
                x={860}
                y={151}
                default={organizeFilter[31 + filterDisplayOffset]}
                selected={organizeFilter[30 + filterDisplayOffset]}
                isSelected={DDSelected}
                action={() => setDDSelected(!DDSelected)}
            />
            {/* DE 海防艦 */}
            <CheckboxButton
                x={925}
                y={151}
                default={organizeFilter[35 + filterDisplayOffset]}
                selected={organizeFilter[34 + filterDisplayOffset]}
                isSelected={DESelected}
                action={() => setDESelected(!DESelected)}
            />
            {/* SS 潜水艦 */}
            <CheckboxButton
                x={990}
                y={151}
                default={organizeFilter[39 + filterDisplayOffset]}
                selected={organizeFilter[38 + filterDisplayOffset]}
                isSelected={SSSelected}
                action={() => setSSSelected(!SSSelected)}
            />
            {/* AV/AO/AS 補助艦艇 */}
            <CheckboxButton
                x={1055}
                y={151}
                default={organizeFilter[43 + filterDisplayOffset]}
                selected={organizeFilter[42 + filterDisplayOffset]}
                isSelected={AVAOASSelected}
                action={() => setAVAOASSelected(!AVAOASSelected)}
            />

            {/* リストヘッダー */}
            <Sprite texture={organizeFilter[4]} x={585} y={184} />


        </Container>
    );
};