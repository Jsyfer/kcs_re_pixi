import { useState, useCallback, useEffect } from 'react';
import { Container } from '@pixi/react';
import { Loading } from '../loading/Loading'
import { PortBackground } from './port/PortBackground';
import { PortTopMenu } from './port/PortTopMenu';
import { PortSideMenu } from './port/PortSideMenu';
import { PortMainMenu } from './port/PortMainMenu';
import { OrganizePanel } from './port/OrganizePanel';
import { HokyuuPanel } from './port/HokyuuPanel';
import { KaisouPanel } from './port/KaisouPanel';
import { NyuukyoPanel } from './port/NyuukyoPanel';
import { KoujyouPanel } from './port/KoujyouPanel';
import { KaisyuPanel } from './port/KaisyuPanel';
import { ShutsugekiPanel } from './port/ShutsugekiPanel';
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
            return <Loading />
        } else {
            switch (panelName) {
                case "organize":
                    return <OrganizePanel portData={portData} getData={props.getData} />
                case "hokyuuPanel":
                    return <HokyuuPanel />
                case "kaisouPanel":
                    return <KaisouPanel />
                case "nyuukyoPanel":
                    return <NyuukyoPanel />
                case "koujyouPanel":
                    return <KoujyouPanel />
                case "kaisyuPanel":
                    return <KaisyuPanel />
                case "shutsugekiPanel":
                    return <ShutsugekiPanel />
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
