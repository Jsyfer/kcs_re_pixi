import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../common/AssetsFactory';

export const NyuukyoPanel = () => {
    const [commonSpritesheets, setCommonSpritesheets] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('kcs2/img/common/common_main.json', setCommonSpritesheets);
    }, []);

    if (commonSpritesheets.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            <Sprite image={'kcs2/img/common/bg/014.png'} x={0} y={0} />
            {/* <Sprite texture={commonSpritesheets[15]} x={150} y={146} /> */}
        </Container>
    );
};