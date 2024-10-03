import { useState } from 'react';
import { Sprite, useTick } from '@pixi/react';
import '@pixi/events';

export const ButtonGear = (props) => {
    const [gearAngle, setGearAngle] = useState(0)

    useTick(() => {
        setGearAngle(angle => angle += 0.2)
    });

    return (
        <Sprite texture={props.texture} anchor={0.5} angle={gearAngle} visible={props.visible} />
    );
};