import { useState } from 'react';
import { Container, Text, Sprite, useTick } from '@pixi/react';
import { SatelliteButton } from '../common/satelliteButton';

export const HomeScene = () => {

    const [angle, setAngle] = useState(0);

    useTick(delta => setAngle(r => r + (0.01 * delta)))

    return (
        <Container x={0} y={0}>
            <Text text="Home Scene" anchor={0.5} x={220} y={150} />
            <Sprite
                x={300}
                y={300}
                scale={{ x: 0.4, y: 0.4 }}
                image={"assets/pixi-react-logo.png"}
                rotation={angle}
                anchor={0.5}
            />
            <SatelliteButton />
        </Container>
    );
};
