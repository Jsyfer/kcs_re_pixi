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

export const PortScene = (props) => {
    const [panelName, setPanelName] = useState("default");
    const [portData, setPortData] = useState(null);
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
                    return <OrganizePanel portData={portData} getData={props.getData} requireInfo={props.requireInfo} />
                case "supply":
                    return <SupplyPanel portData={portData} getData={props.getData} />
                case "remodel":
                    return <RemodelPanel portData={portData} getData={props.getData} requireInfo={props.requireInfo} />
                case "repair":
                    return <RepairPanel portData={portData} getData={props.getData} />
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
