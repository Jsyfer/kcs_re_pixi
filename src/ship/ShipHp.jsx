import { Container, Graphics } from '@pixi/react';

// TODO low hp color change
export const ShipHp = (props) => {
    const hp_length = 92;

    return (
        <Container x={props.x} y={props.y}>
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.beginFill(0x00ff00);
                    g.drawRoundedRect(0, 0, props.nowhp / props.maxhp * hp_length, 5, 5);
                    g.endFill();
                }}
            />
        </Container>
    );
};