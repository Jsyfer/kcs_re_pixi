import { useEffect, useState } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { PixiButton } from '../../../common/PixiButton';

export const ShipCard = (props) => {
    const [organizeMainSpritesheets, setOrganizeMainSpritesheets] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/organize/organize_main.json', setOrganizeMainSpritesheets);
    }, []);

    if (organizeMainSpritesheets.length === 0) {
        return null
    }

    return (
        <Container x={props.x} y={props.y}>
            <Sprite texture={organizeMainSpritesheets[30]} x={0} y={0} />
            <PixiButton
                default={organizeMainSpritesheets[9]}
                hover={organizeMainSpritesheets[10]}
                x={250}
                y={103}
            />
            <PixiButton
                default={organizeMainSpritesheets[24]}
                hover={organizeMainSpritesheets[25]}
                x={378}
                y={103}
            />
        </Container>
    );
};