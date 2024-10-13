import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../common/AssetsFactory';
import { PixiButton } from '../../common/PixiButton';

export const ShutsugekiPanel = () => {
    const [sallyTop, setSallyTop] = useState([])
    const [commonSpritesheets, setCommonSpritesheets] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/sally/sally_top.json', setSallyTop);
        AssetsFactory.loadAsFrames('assets/kcs2/img/common/common_main.json', setCommonSpritesheets);
    }, []);

    if (sallyTop.length === 0 || commonSpritesheets.length === 0) {
        return null
    }

    return (
        <Container x={0} y={0}>
            <Sprite image={'assets/kcs2/img/common/bg/016.png'} x={0} y={0} />
            <Sprite texture={commonSpritesheets[67]} x={0} y={104} />
            <Sprite texture={sallyTop[0]} x={195} y={114} />
            <PixiButton default={sallyTop[8]} hover={sallyTop[9]} x={180} y={175} />
            <Sprite texture={sallyTop[10]} x={245} y={575} />
            <PixiButton default={sallyTop[1]} hover={sallyTop[2]} x={515} y={175} />
            <Sprite texture={sallyTop[3]} x={570} y={575} />
            <PixiButton default={sallyTop[4]} hover={sallyTop[6]} x={850} y={175} />
            <Sprite texture={sallyTop[7]} x={905} y={575} />
        </Container>
    );
};