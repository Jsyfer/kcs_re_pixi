import { useCallback, useEffect, useState } from 'react';
import { Sprite } from '@pixi/react';
import '@pixi/events';

// 选择按钮（单击循环切换）
export const SelectButton = (props) => {
    const [currentIndex, setCurrentIndex] = useState(0);

    return (
        <Sprite
            x={props.x}
            y={props.y}
            eventMode={"static"}
            cursor={props.isDisabled ? 'default' : 'pointer'}
            texture={props.isDisabled ? props.disabled : props.textureList[currentIndex]}
            pointerup={() => {
                if (!props.isDisabled) {
                    // Cycle to the next texture
                    const nextIndex = (currentIndex + 1) % props.textureList.length;
                    setCurrentIndex(nextIndex);

                    if (props.action !== undefined) {
                        props.action(nextIndex);
                    }
                }
            }}
            pointerupoutside={() => {
                if (!props.isDisabled) {
                    if (props.action !== undefined) {
                        props.action();
                    }
                }
            }}
        />
    );

};