import { useState } from 'react';
import { Sprite } from '@pixi/react';
import '@pixi/events';

export const PixiButton = (props) => {
    const [buttonTexture, setButtonTexture] = useState(props.default)
    return (
        <Sprite
            x={props.x}
            y={props.y}
            anchor={props.anchor !== undefined ? props.anchor : 0}
            eventMode={"static"}
            cursor={props.isDisabled ? 'default' : 'pointer'}
            texture={props.isDisabled ? props.disabled : buttonTexture}
            pointerover={() => {
                if (!props.isDisabled) {
                    setButtonTexture(props.hover)
                    if (props.actionOver !== undefined) {
                        props.actionOver();
                    }
                }
            }}
            pointerout={() => {
                if (!props.isDisabled) {
                    setButtonTexture(props.default)
                    if (props.actionOut !== undefined) {
                        props.actionOut();
                    }
                }
            }}
            pointerdown={() => {
                if (!props.isDisabled) {
                    setButtonTexture(props.down)
                }
            }}
            pointerup={() => {
                if (!props.isDisabled) {
                    setButtonTexture(props.default);
                    if (props.action !== undefined) {
                        props.action();
                    }
                }
            }}
        />
    );
};