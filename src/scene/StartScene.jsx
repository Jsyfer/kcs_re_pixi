import { useEffect, useState } from 'react';
import { Container, Sprite, useTick } from '@pixi/react';
import { PixiButton } from '../common/PixiButton';
import * as AssetsFactory from '../common/AssetsFactory';

export const StartScene = ({ setSceneName }) => {
    const [positionY, setPositionY] = useState(800);
    const [titleMainTextures, setTitleMainTextures] = useState([])

    useTick(delta => {
        setPositionY((prevPosition) => Math.max(prevPosition - delta, 550));
    });

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/title/title_main.json', setTitleMainTextures);
    }, []);

    if (titleMainTextures.length === 0) {
        return (
            <Container x={0} y={0}>
                <Sprite image={"assets/kcs2/img/title/title2.png"} />
            </Container>
        );
    } else {
        return (
            <Container x={0} y={0}>
                <Sprite image={"assets/kcs2/img/title/title2.png"} />
                <Sprite x={775} y={110} texture={titleMainTextures[3]} />
                <PixiButton
                    x={650}
                    y={positionY}
                    isDisabled={positionY !== 550}
                    default={titleMainTextures[4]}
                    disabled={titleMainTextures[6]}
                    hover={titleMainTextures[7]}
                    down={titleMainTextures[5]}
                    action={() => { setSceneName("PortScene") }}
                />
            </Container>
        );
    }

};
