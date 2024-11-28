import { useCallback, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import '@pixi/events';
import { ButtonGear } from './ButtonGear'
import { ButtonTips } from './ButtonTips'
import { ButtonEffect } from './ButtonEffect';
import { SallyButtonShip } from './SallyButtonShip';
import { SallyButtonWave } from './SallyButtonWave';

export const SallyButton = (props) => {
    const [isHover, setIsHover] = useState(false)
    const [buttonAlpha, setButtonAlpha] = useState(1)

    const renderButton = useCallback(() => {
        return <>
            {/* not hover */}
            <Sprite texture={props.textures[3]} anchor={0.5} x={37} y={44} visible={!isHover} />
            <Sprite texture={props.textures[4]} anchor={0.5} x={-37} y={44} visible={!isHover} />
            <Sprite
                texture={props.textures[0]}
                anchor={0.5}
                x={0}
                y={0}
                alpha={buttonAlpha}
                eventMode={"static"}
                cursor={'pointer'}
                pointerup={() => {
                    if (props.action !== undefined) {
                        props.action();
                    }
                }}
                pointerover={() => {
                    setIsHover(true)
                    setButtonAlpha(0)
                }}
                pointerout={() => {
                    setIsHover(false)
                    setButtonAlpha(1)
                }}
            />
            <Sprite texture={props.textures[2]} anchor={0.5} x={0} y={-40} visible={!isHover} />
            <Sprite texture={props.textures[1]} anchor={0.5} x={0} y={40} visible={!isHover} />
            {/* hover */}
            <ButtonGear texture={props.textures[24]} visible={isHover} />
            <SallyButtonWave texture={props.textures[25]} x={-37} y={44} wavePosition={"L"} visible={isHover} />
            <SallyButtonWave texture={props.textures[26]} x={37} y={44} wavePosition={"R"} visible={isHover} />
            <Sprite texture={props.textures[23]} anchor={0.5} x={0} y={0} visible={isHover} />
            <SallyButtonShip texture={props.textures[27]} x={0} y={-40} visible={isHover} />
            <Sprite texture={props.textures[28]} anchor={0.5} x={0} y={40} visible={isHover} />
            <ButtonEffect texture={props.textures[31]} visible={isHover} />
            <ButtonTips texture={props.textures[13]} visible={isHover} />
        </>
    }, [isHover])

    return (
        <Container
            x={props.x}
            y={props.y}
        >
            {renderButton()}
        </Container>
    );
};