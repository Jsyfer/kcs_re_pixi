import { useState } from 'react';
import { Sprite, useTick } from '@pixi/react';
import '@pixi/events';

export const ButtonEffect = (props) => {
    const [ringScale1, setRingScale1] = useState(0)
    const [ringAlpha1, setRingAlpha1] = useState(1)
    const [ringScale2, setRingScale2] = useState(0)
    const [ringAlpha2, setRingAlpha2] = useState(1)
    const [effect2UpdateFlg, setEffect2UpdateFlg] = useState(false)

    const updateRingEffect = (ringScale, setRingScale, setRingAlpha) => {
        if (ringScale < 1.2) {
            setRingScale(angle => angle += 0.01)
            if (ringScale > 0.8) {
                setRingAlpha(alpha => alpha -= 0.1)
            }
        } else {
            setRingScale(0)
            setRingAlpha(1)
        }
    }

    useTick(() => {
        updateRingEffect(ringScale1, setRingScale1, setRingAlpha1)
        if (ringScale1 > 0.5) {
            setEffect2UpdateFlg(true)
        }
        if (effect2UpdateFlg) {
            updateRingEffect(ringScale2, setRingScale2, setRingAlpha2)
        }
    });

    return (
        <>
            <Sprite texture={props.texture} anchor={0.5} x={1} scale={ringScale1} alpha={ringAlpha1} visible={props.visible} />
            <Sprite texture={props.texture} anchor={0.5} x={1} scale={ringScale2} alpha={ringAlpha2} visible={props.visible} />
        </>
    );
};