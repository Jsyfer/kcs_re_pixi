import { useState } from 'react';
import { Container, Sprite, useTick } from '@pixi/react';
import { PixiButton } from '../common/PixiButton';
import * as AssetsFactory from '../common/AssetsFactory';

// 开始界面
export const StartScene = ({ setSceneName }) => {
    const [positionY, setPositionY] = useState(800);
    const titleMain = AssetsFactory.getSpritesheet("kcs2/img/title/title_main.json");

    useTick(delta => {
        setPositionY((prevPosition) => Math.max(prevPosition - delta, 550));
    });

    return (
        <Container x={0} y={0}>
            <Sprite image={"kcs2/img/title/title2.png"} />
            <Sprite x={775} y={110} texture={titleMain[3]} />
            <PixiButton
                x={650}
                y={positionY}
                isDisabled={positionY !== 550}
                default={titleMain[4]}
                disabled={titleMain[6]}
                hover={titleMain[7]}
                down={titleMain[5]}
                action={() => { setSceneName("ShipLoading") }}
            />
        </Container>
    );
};
