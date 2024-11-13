import { useEffect, useState } from 'react';
import { Container } from '@pixi/react';
import { SatelliteButton } from './mainMenu/SatelliteButton';
import { ShutsugekiButton } from './mainMenu/ShutsugekiButton';
import * as AssetsFactory from '../../common/AssetsFactory';

export const PortMainMenu = ({ setPanelName }) => {
    const [portSkin, setPortSkin] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('kcs2/img/port/port_ringmenu.json', setPortSkin);
    }, []);

    if (portSkin.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            {/* 改装按钮 */}
            <SatelliteButton type={'kaisou'} textures={portSkin} action={() => { setPanelName("kaisouPanel") }} x={477} y={335} />
            {/* 工廠按钮 */}
            <SatelliteButton type={'koujyou'} textures={portSkin} action={() => { setPanelName("koujyouPanel") }} x={406} y={543} />
            {/* 出撃按钮 */}
            <ShutsugekiButton textures={portSkin} action={() => { setPanelName("shutsugekiPanel") }} x={294} y={390} />
            {/* 入渠按钮 */}
            <SatelliteButton type={'nyuukyo'} textures={portSkin} action={() => { setPanelName("nyuukyoPanel") }} x={186} y={543} />
            {/* 補給按钮 */}
            <SatelliteButton type={'hokyuu'} textures={portSkin} action={() => { setPanelName("hokyuuPanel") }} x={118} y={335} />
            {/* 編成按钮 */}
            <SatelliteButton type={'organize'} textures={portSkin} action={() => { setPanelName("organize") }} x={296} y={202} />
        </Container>
    );
};