import { useState, useEffect, useMemo } from 'react';
import { Sprite, useApp } from '@pixi/react';
import * as PIXI from 'pixi.js';
import '@pixi/events';

// 复选按钮
export const CheckboxButton = (props) => {

    const app = useApp();
    const defaultTransparentTexture = useMemo(() => {
        // 1. Create the Graphics object
        const g = new PIXI.Graphics();

        // 2. Draw the shape
        g.beginFill(0x000000, 0);
        g.drawRect(0, 0, props.default.width, props.default.height);
        g.endFill();

        // 3. Generate a texture from the graphics using the renderer
        return app.renderer.generateTexture(g);
    }, [app.renderer]);

    // Define the mathematical hit zone for the Sprite
    const spriteHitArea = useMemo(() => new PIXI.Rectangle(0, 0, props.default.width, props.default.height), []);

    const defaultTexture = props.isDefaultTextureTransparent ? defaultTransparentTexture : props.default;
    const [buttonTexture, setButtonTexture] = useState(props.isSelected ? props.selected : defaultTexture);

    useEffect(() => {
        setButtonTexture(props.isSelected ? props.selected : defaultTexture);
    }, [props.isSelected])

    return (
        <Sprite
            x={props.x}
            y={props.y}
            eventMode={"static"}
            cursor={props.isDisabled ? 'default' : 'pointer'}
            texture={props.isDisabled ? props.disabled : buttonTexture}
            hitArea={spriteHitArea}
            pointerup={() => {
                if (!props.isDisabled) {
                    if (props.action !== undefined) {
                        props.action();
                    }
                }
            }}
            pointerover={() => {
                if (!props.isDisabled) {
                    if (!props.isSelected) {
                        setButtonTexture(props.hover)
                    }
                    if (props.actionOver !== undefined) {
                        props.actionOver();
                    }
                }
            }}
            pointerout={() => {
                if (!props.isDisabled) {
                    if (!props.isSelected) {
                        setButtonTexture(defaultTexture)
                    }
                    if (props.actionOut !== undefined) {
                        props.actionOut();
                    }
                }
            }
            }
        />
    );
};