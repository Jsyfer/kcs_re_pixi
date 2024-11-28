import { useCallback, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import '@pixi/events';
import { ButtonGear } from './ButtonGear'
import { ButtonTips } from './ButtonTips'
import { ButtonEffect } from './ButtonEffect';

export const SatelliteButton = (props) => {
    const [isHover, setIsHover] = useState(false)
    const [buttonAlpha, setButtonAlpha] = useState(1)

    const renderButton = useCallback(() => {
        let defaultIndex, hoverIndex, tipsIndex = 0
        switch (props.type) {
            case "remodel":
                defaultIndex = 17
                hoverIndex = 18
                tipsIndex = 10
                break;
            case "arsenal":
                defaultIndex = 5
                hoverIndex = 6
                tipsIndex = 8
                break;
            case "repair":
                defaultIndex = 19
                hoverIndex = 20
                tipsIndex = 11
                break;
            case "supply":
                defaultIndex = 29
                hoverIndex = 30
                tipsIndex = 14
                break;
            case "organize":
                defaultIndex = 15
                hoverIndex = 16
                tipsIndex = 9
                break;
        }

        return <>
            <Sprite texture={props.textures[defaultIndex]}
                anchor={0.5}
                alpha={buttonAlpha}
                eventMode={"static"}
                cursor={'pointer'}
                pointerover={() => {
                    setIsHover(true)
                    setButtonAlpha(0)
                }}
                pointerout={() => {
                    setIsHover(false)
                    setButtonAlpha(1)
                }}
                pointerup={() => {
                    if (props.action !== undefined) {
                        props.action();
                    }
                }}
            />
            <ButtonGear texture={props.textures[7]} visible={isHover} />
            <Sprite texture={props.textures[hoverIndex]} anchor={0.5} x={1} y={1} visible={isHover} />
            <ButtonTips texture={props.textures[tipsIndex]} visible={isHover} />
            <ButtonEffect texture={props.textures[31]} visible={isHover} />
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