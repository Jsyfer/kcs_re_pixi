import { useEffect, useState } from 'react';
import { Container, Sprite, useTick } from '@pixi/react';
import { Assets, Texture } from 'pixi.js'

export const PortTopMenu = () => {
    const [portSkin, setPortSkin] = useState([])
    const [topLeftRingAngle, setTopLeftRingAngle] = useState(0)
    const [topLeftTextAngle, setTopLeftTextAngle] = useState(0)
    const [timer, setTimer] = useState(0)

    useTick(() => {
        setTimer(timer + 1);
        if (timer > 60) {
            setTopLeftRingAngle(angle => angle += 3);
            setTimer(timer - 60);
        }
        setTopLeftTextAngle(angle => angle += 0.2)
    });

    useEffect(() => {
        Assets.load('assets/kcs2/img/port/port_skin_1.json').then((data) => {
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
            {/* top left ring */}
            <Sprite texture={portSkin[2]} x={65} y={60} anchor={0.5} angle={topLeftRingAngle} />

            {/* top left ring background*/}
            <Sprite texture={portSkin[1]} x={65} y={60} anchor={0.5} />
            {/* top left text*/}
            <Sprite texture={portSkin[3]} x={65} y={60} anchor={0.5} angle={topLeftTextAngle} />

        </Container>
    );


};