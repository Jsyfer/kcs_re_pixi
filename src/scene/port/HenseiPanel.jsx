import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../common/AssetsFactory';

export const HenseiPanel = () => {
    const [commonSpritesheets, setCommonSpritesheets] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/common/common_main.json', setCommonSpritesheets);
    }, []);

    if (commonSpritesheets.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            <Sprite image={'assets/kcs2/img/common/bg/011.png'} x={0} y={0} />
            <Sprite texture={commonSpritesheets[15]} x={150} y={146} />
            <Sprite texture={commonSpritesheets[67]} x={0} y={104} />
            <Sprite texture={commonSpritesheets[1]} x={195} y={114} />
        </Container>
    );
};