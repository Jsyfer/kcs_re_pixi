import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import { PixiButton } from '../../common/PixiButton';
import * as AssetsFactory from '../../common/AssetsFactory';

export const PortSideMenu = (props) => {
    const [portSkin, setPortSkin] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('kcs2/img/port/port_sidemenu.json', setPortSkin);
    }, []);

    if (portSkin.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            {/* backgtround */}
            <Sprite texture={portSkin[0]} x={0} y={183} />
            <Sprite texture={portSkin[1]} x={0} y={209} />
            <Sprite texture={portSkin[26]} x={63} y={378} />
            <Sprite texture={portSkin[2]} x={75} y={209} />
            {/* 吊车 */}
            <Sprite texture={portSkin[25]} x={0} y={591} />
            <Sprite texture={portSkin[15]} x={0} y={591} />
            {/* 編成按钮 */}
            <PixiButton
                default={portSkin[5]}
                hover={portSkin[6]}
                x={props.panelName === "organize" ? 8 : 0}
                y={194}
                isDisabled={props.panelName === "organize"}
                disabled={portSkin[6]}
                action={() => { props.setPanelName("organize") }}
            />
            {/* 補給按钮 */}
            <PixiButton
                default={portSkin[13]}
                hover={portSkin[14]}
                x={props.panelName === "hokyuuPanel" ? 8 : 0}
                y={275}
                isDisabled={props.panelName === "hokyuuPanel"}
                disabled={portSkin[14]}
                action={() => { props.setPanelName("hokyuuPanel") }}
            />
            {/* 改装按钮 */}
            <PixiButton
                default={portSkin[9]}
                hover={portSkin[10]}
                x={props.panelName === "kaisouPanel" ? 8 : 0}
                y={356}
                isDisabled={props.panelName === "kaisouPanel"}
                disabled={portSkin[10]}
                action={() => { props.setPanelName("kaisouPanel") }}
            />
            {/* 入渠按钮 */}
            <PixiButton
                default={portSkin[11]}
                hover={portSkin[12]}
                x={props.panelName === "nyuukyoPanel" ? 8 : 0}
                y={439}
                isDisabled={props.panelName === "nyuukyoPanel"}
                disabled={portSkin[12]}
                action={() => { props.setPanelName("nyuukyoPanel") }}
            />
            {/* 工廠按钮 */}
            <PixiButton
                default={portSkin[3]}
                hover={portSkin[4]}
                x={props.panelName === "koujyouPanel" ? 8 : 0}
                y={517}
                isDisabled={props.panelName === "koujyouPanel"}
                disabled={portSkin[4]}
                action={() => { props.setPanelName("koujyouPanel") }}
            />
            {/* 母港按钮 */}
            <PixiButton
                default={portSkin[7]}
                hover={portSkin[8]}
                x={75}
                y={329}
                action={() => { props.setPanelName("default") }}
            />
        </Container>
    );


};