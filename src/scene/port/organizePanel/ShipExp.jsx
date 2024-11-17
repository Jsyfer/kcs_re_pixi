import { Container, Sprite } from '@pixi/react';

export const ShipExp = (props) => {
    return (
        <Container x={props.x} y={props.y}>
            <Sprite texture={props.commonMain[21]} x={0} y={0} />
            <Sprite texture={props.commonMain[22]} x={3} y={3} scale={{ x: props.exp[2] / 100, y: 1 }} />
        </Container>
    );
};