import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { RadioButton } from '../../../common/RadioButton';
import { RemodelShip } from './RemodelShip';
import { ShipDetails } from '../../../ship/ShipDetails';
import { useStore } from "../../../common/StoreFactory"

// 改装
export const RemodelPanel = () => {
    const portData = useStore(state => state.portData)

    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const remodelMain = AssetsFactory.getSpritesheet("kcs2/img/remodel/remodel_main.json")
    const [currentFleet, setCurrentFleet] = useState(0);
    const [selectedShipIndex, setSelectedShipIndex] = useState(0);
    const fleet = portData.api_data.api_deck_port[currentFleet].api_ship;
    const lastShipIndex = fleet.findIndex(num => num === -1);

    return (
        <Container x={0} y={0}>
            <Sprite image={'kcs2/img/common/bg/013.png'} x={0} y={0} />
            <Sprite texture={commonMain[67]} x={0} y={104} />

            {/* 艦隊1 */}
            <RadioButton x={203} y={164} default={commonMisc[78]} selected={commonMisc[79]} isSelected={currentFleet === 0} action={() => { setCurrentFleet(0); setSelectedShipIndex(0) }} />
            {/* 艦隊2 */}
            <RadioButton x={248} y={164} default={commonMisc[81]} selected={commonMisc[82]} isSelected={currentFleet === 1} action={() => { setCurrentFleet(1); setSelectedShipIndex(0) }} />
            {/* 艦隊3 */}
            <RadioButton x={293} y={164} default={commonMisc[84]} selected={commonMisc[85]} isSelected={currentFleet === 2} action={() => { setCurrentFleet(2); setSelectedShipIndex(0) }} />
            {/* 艦隊4 */}
            <RadioButton x={338} y={164} default={commonMisc[87]} selected={commonMisc[88]} isSelected={currentFleet === 3} action={() => { setCurrentFleet(3); setSelectedShipIndex(0) }} />
            {/* TODO 他 */}
            <RadioButton x={383} y={164} default={commonMisc[89]} selected={commonMisc[90]} isSelected={currentFleet === -1} action={() => { setCurrentFleet(-1); setSelectedShipIndex(0) }} />

            {/* 艦船リスト */}
            <Sprite texture={remodelMain[45]} x={175} y={145} />
            {[0, 1, 2, 3, 4, 5].map(
                i => <RemodelShip
                    key={i}
                    fleet={fleet}
                    shipIndex={i}
                    selectedShipIndex={selectedShipIndex}
                    setSelectedShipIndex={setSelectedShipIndex}
                    x={182} y={210 + 80 * i}
                />
            )}

            <Sprite texture={remodelMain[44]} x={450} y={140} />

            <ShipDetails
                editable={true}
                fleet={fleet}
                shipIndex={selectedShipIndex}
                lastShipIndex={lastShipIndex}
                x={470} y={104}
            />

        </Container>
    );
};