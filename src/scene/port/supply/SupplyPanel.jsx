import { useState } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { RadioButton } from '../../../common/RadioButton';
import { PixiButton } from '../../../common/PixiButton';
import { SupplyCard } from './ShipCard';

export const SupplyPanel = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const supplyMain = AssetsFactory.getSpritesheet("kcs2/img/supply/supply_main.json")
    const [currentFleet, setCurrentFleet] = useState(0);
    if (currentFleet === -1) {
        // TODO get other sheep
    } else {
        // get sheet from fleet 1~4
        const fleet = props.portData.api_data.api_deck_port[currentFleet].api_ship;
    }
    const api_ship = props.portData.api_data.api_ship;

    return (
        <Container x={0} y={0}>
            {/* 背景 */}
            <Sprite image={'kcs2/img/common/bg/012.png'} x={0} y={0} />
            <Sprite texture={commonMain[67]} x={0} y={104} />
            <Sprite texture={commonMain[1]} x={195} y={114} />
            {/* 全補給 */}
            <Sprite texture={supplyMain[32]} x={165} y={164} />
            {/* 艦隊1 */}
            <RadioButton x={203} y={164} default={commonMisc[78]} selected={commonMisc[79]} isSelected={currentFleet === 0} action={() => { setCurrentFleet(0) }} />
            {/* 艦隊2 */}
            <RadioButton x={248} y={164} default={commonMisc[81]} selected={commonMisc[82]} isSelected={currentFleet === 1} action={() => { setCurrentFleet(1) }} />
            {/* 艦隊3 */}
            <RadioButton x={293} y={164} default={commonMisc[84]} selected={commonMisc[85]} isSelected={currentFleet === 2} action={() => { setCurrentFleet(2) }} />
            {/* 艦隊4 */}
            <RadioButton x={338} y={164} default={commonMisc[87]} selected={commonMisc[88]} isSelected={currentFleet === 3} action={() => { setCurrentFleet(3) }} />
            {/* TODO 他 */}
            <RadioButton x={383} y={164} default={commonMisc[89]} selected={commonMisc[90]} isSelected={currentFleet === 4} action={() => { setCurrentFleet(4) }} />
            {/* 燃料総数 */}
            <Sprite texture={supplyMain[28]} x={595} y={158} />
            <Text text={"300000"} x={640} y={164} style={{ fill: 'black', fontSize: 28 }} />
            {/* 弾薬総数 */}
            <Sprite texture={supplyMain[29]} x={753} y={158} />
            <Text text={"300000"} x={800} y={164} style={{ fill: 'black', fontSize: 28 }} />
            {/* ships */}
            <SupplyCard x={203} y={214} />

            {/* 燃料・弾薬の補給 */}
            <Sprite texture={supplyMain[23]} x={900} y={135} />
            <Sprite texture={commonMain[67]} x={900} y={104} />
            <Sprite texture={supplyMain[0]} x={923} y={113} />
            {/* 補給する資材数 */}
            <Sprite texture={supplyMain[34]} x={918} y={158} />
            {/* 補給の燃料 */}
            <Sprite texture={supplyMain[2]} x={918} y={218} />
            <Sprite texture={commonMisc[23]} x={986} y={570} angle={180} />
            <Sprite texture={commonMisc[23]} x={985} y={510} />
            <Sprite texture={commonMisc[17]} x={918} y={346} />
            <Sprite texture={commonMisc[16]} x={918} y={513} />
            <Sprite texture={commonMisc[22]} x={918} y={345} />
            <Text text={"0"} x={1045} y={300} anchor={{ x: 1, y: 0 }} style={{ fill: 'black', fontSize: 32 }} />
            {/* 補給の弾薬 */}
            <Sprite texture={supplyMain[1]} x={1060} y={218} />
            <Sprite texture={commonMisc[23]} x={1128} y={570} angle={180} />
            <Sprite texture={commonMisc[23]} x={1127} y={510} />
            <Sprite texture={commonMisc[7]} x={1060} y={346} />
            <Sprite texture={commonMisc[16]} x={1060} y={514} />
            <Sprite texture={commonMisc[22]} x={1060} y={345} />
            <Text text={"0"} x={1185} y={300} anchor={{ x: 1, y: 0 }} style={{ fill: 'black', fontSize: 32 }} />
            {/* 艦載機補充 */}
            <PixiButton default={supplyMain[16]} x={915} y={597} />
            {/* 艦隊全補給 */}
            <PixiButton default={supplyMain[13]} x={1060} y={597} />
            {/* 燃料補給 */}
            <PixiButton default={supplyMain[10]} x={918} y={641} />
            {/* まとめて補給 */}
            <PixiButton default={supplyMain[4]} x={979} y={641} />
            {/* 弾薬補給 */}
            <PixiButton default={supplyMain[7]} x={1135} y={641} />
        </Container>
    );
};