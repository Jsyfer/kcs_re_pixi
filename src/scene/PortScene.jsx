import { useState, useCallback, useEffect } from 'react';
import { Container, Graphics } from '@pixi/react';
import { Loading } from '../loading/Loading'
import { PortBackground } from './port/PortBackground';
import { PortTopMenu } from './port/PortTopMenu';
import { PortSideMenu } from './port/PortSideMenu';
import { PortMainMenu } from './port/PortMainMenu';
import { OrganizePanel } from './port/organize/OrganizePanel';
import { SupplyPanel } from './port/supply/SupplyPanel';
import { RemodelPanel } from './port/remodel/RemodelPanel';
import { RepairPanel } from './port/repair/RepairPanel';
import { ArsenalPanel } from './port/arsenal/ArsenalPanel';
import { RevampPanel } from './port/revamp/RevampPanel';
import { SallyPanel } from './port/SallyPanel';
import * as ApiFactory from '../common/ApiFactory';
import { useStore } from "../common/StoreFactory"

export const PortScene = () => {
    const [panelName, setPanelName] = useState("default");
    const portData = useStore((state) => state.portData)
    const setPortData = useStore((state) => state.setPortData)
    const [fadeAlpha, setFadeAlpha] = useState(1);

    useEffect(() => {
        ApiFactory.get("kcsapi/api_port/port", setPortData)
    }, []);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setFadeAlpha(preAlpha => Math.max(preAlpha - 0.02, 0))
        }, 10)
        return () => { clearInterval(intervalId) };
    }, [fadeAlpha]);

    const renderBackground = useCallback(() => {
        if (portData === null) {
            return <Loading />
        } else {
            switch (panelName) {
                case "organize":
                    return <OrganizePanel />
                case "supply":
                    return <SupplyPanel />
                case "remodel":
                    return <RemodelPanel />
                case "repair":
                    return <RepairPanel />
                case "arsenal":
                    return <ArsenalPanel />
                case "revamp":
                    return <RevampPanel />
                case "sally":
                    return <SallyPanel />
                default:
                    return <PortBackground />
            }
        }
    }, [panelName, portData])

    const renderSideMainMenu = useCallback(() => {
        if (panelName === "default") {
            return <PortMainMenu setPanelName={setPanelName} />
        } else {
            return <PortSideMenu panelName={panelName} setPanelName={setPanelName} />
        }
    }, [panelName])

    return (
        <Container x={0} y={0}>
            {renderBackground()}
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.beginFill(0x000000);
                    g.drawRect(0, 0, 1200, 720);
                    g.endFill();
                }}
                alpha={fadeAlpha}
            />
            <PortTopMenu panelName={panelName} setPanelName={setPanelName} />
            {renderSideMainMenu()}
        </Container>
    );
};
