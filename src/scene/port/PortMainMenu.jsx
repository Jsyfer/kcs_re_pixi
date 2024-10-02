import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import { Assets, Texture } from 'pixi.js'
import { PixiButton } from '../../common/PixiButton';

export const PortMainMenu = ({ setPanelName }) => {
    const [portSkin, setPortSkin] = useState([])

    // useEffect(() => {
    //     Assets.load('assets/kcs2/img/port/port_sidemenu.json').then((data) => {
    //         setPortSkin(
    //             Object.keys(data.textures).map(frame =>
    //                 Texture.from(frame)
    //             )
    //         );
    //     });
    // }, []);

    if (portSkin.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>

        </Container>
    );


};