import { useState, useCallback } from 'react';
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

export const PortScene = ({ setSceneName }) => {
    const [panelName, setPanelName] = useState("default");

    const renderBackground = useCallback(() => {
        switch (panelName) {
            case "organize":
                return <OrganizePanel />
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
                return <PortBackground />
        }
    }, [panelName])

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
