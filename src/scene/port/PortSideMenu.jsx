import { Container, Sprite } from '@pixi/react';
import { PixiButton } from '../../common/PixiButton';
import * as AssetsFactory from '../../common/AssetsFactory';

export const PortSideMenu = (props) => {
    const portSidemenu = AssetsFactory.getSpritesheet("kcs2/img/port/port_sidemenu.json");

    return (
        <Container x={0} y={0}>
            {/* backgtround */}
            <Sprite texture={portSidemenu[0]} x={0} y={183} />
            <Sprite texture={portSidemenu[1]} x={0} y={209} />
            <Sprite texture={portSidemenu[26]} x={63} y={378} />
            <Sprite texture={portSidemenu[2]} x={75} y={209} />
            {/* 吊车 */}
            <Sprite texture={portSidemenu[25]} x={0} y={591} />
            <Sprite texture={portSidemenu[15]} x={0} y={591} />
            {/* 編成按钮 */}
            <PixiButton
                default={portSidemenu[5]}
                hover={portSidemenu[6]}
                x={props.panelName === "organize" ? 8 : 0}
                y={194}
                isDisabled={props.panelName === "organize"}
                disabled={portSidemenu[6]}
                action={() => { props.setPanelName("organize") }}
            />
            {/* 補給按钮 */}
            <PixiButton
                default={portSidemenu[13]}
                hover={portSidemenu[14]}
                x={props.panelName === "supply" ? 8 : 0}
                y={275}
                isDisabled={props.panelName === "supply"}
                disabled={portSidemenu[14]}
                action={() => { props.setPanelName("supply") }}
            />
            {/* 改装按钮 */}
            <PixiButton
                default={portSidemenu[9]}
                hover={portSidemenu[10]}
                x={props.panelName === "remodel" ? 8 : 0}
                y={356}
                isDisabled={props.panelName === "remodel"}
                disabled={portSidemenu[10]}
                action={() => { props.setPanelName("remodel") }}
            />
            {/* 入渠按钮 */}
            <PixiButton
                default={portSidemenu[11]}
                hover={portSidemenu[12]}
                x={props.panelName === "repair" ? 8 : 0}
                y={439}
                isDisabled={props.panelName === "repair"}
                disabled={portSidemenu[12]}
                action={() => { props.setPanelName("repair") }}
            />
            {/* 工廠按钮 */}
            <PixiButton
                default={portSidemenu[3]}
                hover={portSidemenu[4]}
                x={props.panelName === "arsenal" ? 8 : 0}
                y={517}
                isDisabled={props.panelName === "arsenal"}
                disabled={portSidemenu[4]}
                action={() => { props.setPanelName("arsenal") }}
            />
            {/* 母港按钮 */}
            <PixiButton
                default={portSidemenu[7]}
                hover={portSidemenu[8]}
                x={75}
                y={329}
                action={() => { props.setPanelName("default") }}
            />
        </Container>
    );


};