import { useState } from 'react';
import { Container, Graphics, useTick } from '@pixi/react';

export const Loading = () => {
    const [angle, setAngle] = useState(0)

    useTick(() => {
        setAngle(angle => angle += 0.2)
    });

    return (
        <Container >
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.beginFill(0xffffff);
                    g.drawCircle(1150, 7150, 20);
                    g.endFill();
                }}
                angle={angle}
            />
        </Container>
    );
};