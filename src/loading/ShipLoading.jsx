import { useState, useEffect } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../common/AssetsFactory';
import * as ApiFactory from '../common/ApiFactory';

export const ShipLoading = (props) => {
    const [titleMainTextures, setTitleMainTextures] = useState([])
    const [getDataloaded, setGetDataLoaded] = useState(false)
    const [requireInfoloaded, setRequireInfoLoaded] = useState(false)

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/title/title_main.json', setTitleMainTextures);
        // get common game data
        ApiFactory.get("kcsapi/api_start2/getData", props.setGetData, setGetDataLoaded)
        ApiFactory.get("kcsapi/api_get_member/require_info", props.setRequireInfo, setRequireInfoLoaded)
    }, []);

    if (titleMainTextures.length === 0) {
        return null
    }

    if (getDataloaded && requireInfoloaded) {
        props.setSceneName("Port")
    }

    return (
        <Container x={0} y={0}>
            <Sprite x={600} y={360} texture={titleMainTextures[0]} anchor={0.5} />
            <Sprite x={600} y={330} texture={titleMainTextures[1]} anchor={0.5} />
        </Container>
    );
};