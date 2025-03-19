import { useCallback, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { ShipCard } from '../../../ship/ShipCard';
import { PixiButton } from '../../../common/PixiButton';
import { RadioButton } from '../../../common/RadioButton';
import { ShipStatus } from '../../../ship/ShipStatus';
import { useStore } from "../../../common/StoreFactory"
import '@pixi/events';

// 編成
export const OrganizePanel = () => {
    const portData = useStore(state => state.portData)

    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const organizeMain = AssetsFactory.getSpritesheet("kcs2/img/organize/organize_main.json")
    const [currentFleet, setCurrentFleet] = useState(0);
    const [selectedShipIndex, setSelectedShipIndex] = useState(-1);
    const fleet = portData.api_data.api_deck_port[currentFleet].api_ship;
    const api_ship = portData.api_data.api_ship;
    const lastShipIndex = fleet.findIndex(num => num === -1);

    const render_ship_detail = useCallback(() => {
        if (selectedShipIndex === -1) return null;
        return <ShipStatus
            editable={false}
            fleet={fleet}
            shipIndex={selectedShipIndex}
            api_ship={api_ship}
            lastShipIndex={lastShipIndex}
            x={470} y={104}
        />
    }, [selectedShipIndex])

    return (
        <Container eventMode={"static"} pointerup={() => { if (selectedShipIndex !== -1) setSelectedShipIndex(-1) }} x={0} y={0}>
            {/* 背景 */}
            <Sprite image={'kcs2/img/common/bg/011.png'} x={0} y={0} />
            {/* 背景マスク */}
            <Sprite texture={commonMain[15]} x={150} y={146} />
            {/* 艦船選択背景 */}
            <Sprite texture={commonMain[67]} x={0} y={104} />
            {/* 艦船選択 */}
            <Sprite texture={commonMain[1]} x={195} y={114} />
            {/* 艦隊1 */}
            <RadioButton x={177} y={165} default={commonMisc[78]} selected={commonMisc[79]} isSelected={currentFleet === 0} action={() => { setCurrentFleet(0) }} />
            {/* 艦隊2 */}
            <RadioButton x={222} y={165} default={commonMisc[81]} selected={commonMisc[82]} isSelected={currentFleet === 1} action={() => { setCurrentFleet(1) }} />
            {/* 艦隊3 */}
            <RadioButton x={267} y={165} default={commonMisc[84]} selected={commonMisc[85]} isSelected={currentFleet === 2} action={() => { setCurrentFleet(2) }} />
            {/* 艦隊4 */}
            <RadioButton x={312} y={165} default={commonMisc[87]} selected={commonMisc[88]} isSelected={currentFleet === 3} action={() => { setCurrentFleet(3) }} />
            {/* 給 */}
            <PixiButton default={organizeMain[17]} x={465} y={157} />
            {/* 随伴艦一括解除 */}
            <PixiButton default={organizeMain[56]} hover={organizeMain[57]} x={570} y={162} />
            {/* 艦隊名 */}
            <Sprite texture={organizeMain[27]} x={694} y={150} />
            {/* 編集 */}
            <PixiButton default={organizeMain[60]} x={1112} y={151} />
            {/* 艦船リスト */}
            <ShipCard fleet={fleet} shipIndex={0} api_ship={api_ship} lastShipIndex={lastShipIndex} setSelectedShipIndex={setSelectedShipIndex} x={180} y={198} />
            <ShipCard fleet={fleet} shipIndex={1} api_ship={api_ship} lastShipIndex={lastShipIndex} setSelectedShipIndex={setSelectedShipIndex} x={693} y={198} />
            <ShipCard fleet={fleet} shipIndex={2} api_ship={api_ship} lastShipIndex={lastShipIndex} setSelectedShipIndex={setSelectedShipIndex} x={180} y={366} />
            <ShipCard fleet={fleet} shipIndex={3} api_ship={api_ship} lastShipIndex={lastShipIndex} setSelectedShipIndex={setSelectedShipIndex} x={693} y={366} />
            <ShipCard fleet={fleet} shipIndex={4} api_ship={api_ship} lastShipIndex={lastShipIndex} setSelectedShipIndex={setSelectedShipIndex} x={180} y={534} />
            <ShipCard fleet={fleet} shipIndex={5} api_ship={api_ship} lastShipIndex={lastShipIndex} setSelectedShipIndex={setSelectedShipIndex} x={693} y={534} />
            {/* 艦船詳細 */}
            {render_ship_detail()}
        </Container>
    );
};