import { Container, Sprite } from '@pixi/react';
import { useCallback } from 'react';
import * as AssetsFactory from '@common/AssetsFactory';

export const ShipFuelBull = (props) => {
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")
    const render = useCallback(() => {
        if (props.now === props.max) {
            return <Sprite texture={commonMisc[130]} />
        }
        if (props.now === 0) {
            return <Sprite texture={commonMisc[128]} />
        }
        const percentage = /\d\.(\d)/.exec(props.now / props.max)[1];
        if (percentage === "9") {
            return <Sprite texture={commonMisc[138]} />
        }
        if (percentage === "1") {
            return <Sprite texture={commonMisc[131]} />
        }
        return <Sprite texture={commonMisc[13 + percentage - 1]} />
    })
    return (
        <Container x={props.x} y={props.y}>
            {render()}
        </Container>
    );
};