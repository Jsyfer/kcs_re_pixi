import { useState, useCallback } from 'react';
import { Container } from '@pixi/react';
import { PortBackground } from './port/PortBackground';
import { PortTopMenu } from './port/PortTopMenu';
import { PortSideMenu } from './port/PortSideMenu';
import { PortMainMenu } from './port/PortMainMenu';

export const PortScene = ({ setSceneName }) => {
    const [panelName, setPanelName] = useState("default");

    const renderBackground = useCallback(() => {
        switch (panelName) {
            case "henseiPanel":
                return <PortBackground />
            case "hokyuuPanel":
                return <PortBackground />
            case "kaisouPanel":
                return <PortBackground />
            case "nyuukyoPanel":
                return <PortBackground />
            case "koujyouPanel":
                return <PortBackground />
            case "kaisyuPanel":
                return <PortBackground />
            default:
                return <PortBackground />
        }
    }, [panelName])

    const renderSideMainMenu = useCallback(() => {
        if (panelName === "default") {
            return <PortMainMenu setPanelName={setPanelName} />
        } else {
            return <PortSideMenu setPanelName={setPanelName} />
        }
    }, [panelName])

    return (
        <Container x={0} y={0}>
            {renderBackground()}
            <PortTopMenu panelName={panelName} />
            {renderSideMainMenu()}
        </Container>
    );
};
