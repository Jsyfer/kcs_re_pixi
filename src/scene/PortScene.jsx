import { useState, useCallback, useEffect } from 'react';
import { Container } from '@pixi/react';
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

    useEffect(() => {
        ApiFactory.get("kcsapi/api_port/port", setPortData)
    }, []);

    const renderBackground = useCallback(() => {
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
                if (portData !== null) {
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
            <PortTopMenu panelName={panelName} setPanelName={setPanelName} />
            {renderSideMainMenu()}
        </Container>
    );
};
