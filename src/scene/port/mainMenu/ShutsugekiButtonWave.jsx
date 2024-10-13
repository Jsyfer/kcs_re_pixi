import { useState } from 'react';
import { Sprite, useTick } from '@pixi/react';
import '@pixi/events';

export const ShutsugekiButtonWave = (props) => {
    const [waveStep1Flag, setWaveStep1Flag] = useState(true)
    const [waveStep2Flag, setWaveStep2Flag] = useState(true)
    const [waveAngle, setWaveAngle] = useState(0)
    const [wavePositionX, setWavePositionX] = useState(props.x)

    useTick(() => {
        if (props.wavePosition === "L") {
            // 左侧波浪动画
            if (!waveStep1Flag && waveAngle > -5) {
                setWaveAngle(angle => angle -= 0.2)
            } else {
                setWaveStep1Flag(true)
                if (!waveStep2Flag && wavePositionX > -65) {
                    setWavePositionX(x => x -= 0.3)
                } else {
                    setWaveStep2Flag(true)
                    if (waveAngle < 0) {
                        setWaveAngle(angle => angle += 0.2)
                    } else {
                        if (wavePositionX < -37) {
                            setWavePositionX(x => x += 0.3)
                        } else {
                            setWaveStep1Flag(false)
                            setWaveStep2Flag(false)
                        }
                    }
                }
            }
        } else {
            // 右侧波浪动画
            if (!waveStep1Flag && waveAngle < 5) {
                setWaveAngle(angle => angle += 0.2)
            } else {
                setWaveStep1Flag(true)
                if (!waveStep2Flag && wavePositionX < 65) {
                    setWavePositionX(x => x += 0.3)
                } else {
                    setWaveStep2Flag(true)
                    if (waveAngle > 0) {
                        setWaveAngle(angle => angle -= 0.2)
                    } else {
                        if (wavePositionX > 37) {
                            setWavePositionX(x => x -= 0.3)
                        } else {
                            setWaveStep1Flag(false)
                            setWaveStep2Flag(false)
                        }
                    }
                }
            }
        }
    });

    return (
        <Sprite texture={props.texture} anchor={0.5} visible={props.visible} angle={waveAngle} x={wavePositionX} y={props.y} />
    );
};