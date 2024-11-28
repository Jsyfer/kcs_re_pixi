import { useState, useCallback, useEffect } from 'react';
import { Container } from '@pixi/react';
import { Loading } from '../loading/Loading'
import { PortBackground } from './port/PortBackground';
import { PortTopMenu } from './port/PortTopMenu';
import { PortSideMenu } from './port/PortSideMenu';
import { PortMainMenu } from './port/PortMainMenu';
import { OrganizePanel } from './port/OrganizePanel';
import { SupplyPanel } from './port/SupplyPanel';
import { RemodelPanel } from './port/RemodelPanel';
import { RepairPanel } from './port/RepairPanel';
import { ArsenalPanel } from './port/ArsenalPanel';
import { RevampPanel } from './port/RevampPanel';
import { SallyPanel } from './port/SallyPanel';
import * as ApiFactory from '../common/ApiFactory';

export const PortScene = (props) => {
    const [panelName, setPanelName] = useState("default");
    const [portData, setPortData] = useState(null);
    const [fadeinAlpha, setFadeinAlpha] = useState(0);

    useEffect(() => {
        ApiFactory.get("kcsapi/api_port/port", setPortData)
    }, []);

    useEffect(() => {
        const intervalId = setInterval(() => {
            setFadeinAlpha(preAlpha => Math.min(preAlpha + 0.02, 1))
        }, 10)
        return () => { clearInterval(intervalId) };
    }, [fadeinAlpha]);

    const renderBackground = useCallback(() => {
        if (portData === null) {
            // return <Loading />
            return null
        } else {
            switch (panelName) {
                case "organize":
                    return <OrganizePanel portData={portData} getData={props.getData} />
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
                    return <PortBackground portData={portData} getData={props.getData} />
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
            <Container alpha={fadeinAlpha}>
                {renderBackground()}
            </Container>
            <PortTopMenu panelName={panelName} setPanelName={setPanelName} />
            {renderSideMainMenu()}
        </Container>
    );
};
