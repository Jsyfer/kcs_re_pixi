import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../common/AssetsFactory';

export const ShipExp = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")

    return (
        <Container x={props.x} y={props.y}>
            <Sprite texture={commonMain[21]} x={0} y={0} />
            <Sprite texture={commonMain[22]} x={3} y={3} scale={{ x: props.exp[2] / 100, y: 1 }} />
        </Container>
    );
};