import { Sprite } from '@pixi/react';
import '@pixi/events';

export const RadioButton = (props) => {
    return (
        <Sprite
            x={props.x}
            y={props.y}
            eventMode={"static"}
            cursor={props.isDisabled ? 'default' : 'pointer'}
            texture={props.isDisabled ? props.disabled : (props.isSelected ? props.selected : props.default)}
            pointerup={() => {
                if (!props.isDisabled) {
                    if (props.action !== undefined) {
                        props.action();
                    }
                }
            }}
        />
    );
};