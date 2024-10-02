import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import { Assets, Texture } from 'pixi.js'
import { PixiButton } from '../../common/PixiButton';

export const PortSideMenu = ({ setPanelName }) => {
    const [portSkin, setPortSkin] = useState([])

    useEffect(() => {
        Assets.load('assets/kcs2/img/port/port_sidemenu.json').then((data) => {
            setPortSkin(
                Object.keys(data.textures).map(frame =>
                    Texture.from(frame)
                )
            );
        });
    }, []);

    if (portSkin.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            {/* backgtround */}
            <Sprite texture={portSkin[0]} x={0} y={185} />
            <Sprite texture={portSkin[1]} x={0} y={210} />
            <Sprite texture={portSkin[2]} x={74} y={210} />
            {/* 吊车 */}
            <Sprite texture={portSkin[25]} x={0} y={600} />
            <Sprite texture={portSkin[15]} x={0} y={600} />
            {/* 編成按钮 */}
            <PixiButton default={portSkin[5]} hover={portSkin[6]} x={0} y={195} action={() => { setPanelName("henseiPanel") }} />
            {/* 補給按钮 */}
            <PixiButton default={portSkin[13]} hover={portSkin[14]} x={0} y={278} action={() => { setPanelName("hokyuuPanel") }} />
            {/* 改装按钮 */}
            <PixiButton default={portSkin[9]} hover={portSkin[10]} x={0} y={360} action={() => { setPanelName("kaisouPanel") }} />
            {/* 入渠按钮 */}
            <PixiButton default={portSkin[11]} hover={portSkin[12]} x={0} y={440} action={() => { setPanelName("nyuukyoPanel") }} />
            {/* 工廠按钮 */}
            <PixiButton default={portSkin[3]} hover={portSkin[4]} x={0} y={518} action={() => { setPanelName("koujyouPanel") }} />
            {/* 母港按钮 */}
            <PixiButton default={portSkin[7]} hover={portSkin[8]} x={84} y={330} action={() => { setPanelName("default") }} />


        </Container>
    );


};