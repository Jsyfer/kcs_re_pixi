import { useState } from 'react';
import { Sprite, useTick } from '@pixi/react';
import '@pixi/events';

export const ShutsugekiButtonShip = (props) => {
    const [shipAngle, setShipAngle] = useState(0)
    const [clockwiseFlag, setClockwiseFlag] = useState(true)

    useTick(() => {
        if (props.visible) {
            if (clockwiseFlag) {
                if (shipAngle < 3) {
                    setShipAngle(angle => angle += 0.05)
                } else {
                    setClockwiseFlag(false)
                }
            } else {
                if (shipAngle > -3) {
                    setShipAngle(angle => angle -= 0.05)
                } else {
                    setClockwiseFlag(true)
                }
            }
        } else {
            setShipAngle(0);
        }
    });

    return (
        <Sprite texture={props.texture} anchor={0.5} angle={shipAngle} visible={props.visible} x={props.x} y={props.y} />
    );
};