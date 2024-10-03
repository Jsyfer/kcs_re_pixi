import { useState } from 'react';
import { Sprite, useTick } from '@pixi/react';
import '@pixi/events';

export const ButtonTips = (props) => {
    const [tipsPositionX, setTipsPositionX] = useState(0)
    const [tipsAlpha, setTipsAlpha] = useState(0)

    useTick(() => {
        if (tipsPositionX < 35) {
            setTipsPositionX(x => x += 3)
            setTipsAlpha(alpha => alpha += 0.2)
        }
        if (!props.visible) {
            setTipsPositionX(0)
            setTipsAlpha(0)
        }
    });

    return (
        <Sprite texture={props.texture} x={tipsPositionX} y={-22} alpha={tipsAlpha} visible={props.visible} />
    );
};