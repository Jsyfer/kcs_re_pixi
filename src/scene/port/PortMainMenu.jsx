import { Container } from '@pixi/react';
import { SatelliteButton } from './mainMenu/SatelliteButton';
import { SallyButton } from './mainMenu/SallyButton';
import * as AssetsFactory from '../../common/AssetsFactory';

// 母港主菜单
export const PortMainMenu = ({ setPanelName }) => {
    const portRingmenu = AssetsFactory.getSpritesheet("kcs2/img/port/port_ringmenu.json")

    return (
        <Container x={0} y={0}>
            {/* 改装按钮 */}
            <SatelliteButton type={'remodel'} textures={portRingmenu} action={() => { setPanelName("remodel") }} x={477} y={335} />
            {/* 工廠按钮 */}
            <SatelliteButton type={'arsenal'} textures={portRingmenu} action={() => { setPanelName("arsenal") }} x={406} y={543} />
            {/* 出撃按钮 */}
            <SallyButton textures={portRingmenu} action={() => { setPanelName("sally") }} x={294} y={390} />
            {/* 入渠按钮 */}
            <SatelliteButton type={'repair'} textures={portRingmenu} action={() => { setPanelName("repair") }} x={186} y={543} />
            {/* 補給按钮 */}
            <SatelliteButton type={'supply'} textures={portRingmenu} action={() => { setPanelName("supply") }} x={118} y={335} />
            {/* 編成按钮 */}
            <SatelliteButton type={'organize'} textures={portRingmenu} action={() => { setPanelName("organize") }} x={296} y={202} />
        </Container>
    );
};