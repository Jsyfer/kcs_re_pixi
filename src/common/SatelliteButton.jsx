import { useState } from 'react';
import { Sprite } from '@pixi/react';
import '@pixi/events';

export const SatelliteButton = (props) => {
    const [buttonImg, setButtonImg] = useState(props.default)
    const [angle, setAngle] = useState(0);
    const [intervalId, setIntervalId] = useState();

    return (
        <Sprite
            x={550}
            y={450}
            scale={{ x: 0.4, y: 0.4 }}
            image={"assets/pixi-react-logo.png"}
            anchor={0.5}
            angle={angle}
            eventMode={"static"}
            pointerover={() => {
                setIntervalId(setInterval(() => {
                    setAngle((prevAngle) => prevAngle + 1);
                }, 10))
            }}
            pointerout={() => {
                clearInterval(intervalId);
            }}
        />
    );
};