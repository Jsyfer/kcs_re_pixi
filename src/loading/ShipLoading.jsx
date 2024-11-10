import { useState, useEffect } from 'react';
import { Container, Sprite } from '@pixi/react';
import axios from 'axios';
import * as AssetsFactory from '../common/AssetsFactory';

export const ShipLoading = (props) => {
    const [titleMainTextures, setTitleMainTextures] = useState([])
    const [getDataloaded, setGetDataLoaded] = useState(false)
    const [requireInfoloaded, setRequireInfoLoaded] = useState(false)

    useEffect(() => {
        AssetsFactory.loadAsFrames('assets/kcs2/img/title/title_main.json', setTitleMainTextures);
        // get common game data
        axios.post("kcsapi/api_start2/getData")
            .then(res => {
                props.setGetData(res.data)
                setGetDataLoaded(true)
            })
            .catch(error => {
                console.log(error)
            });
        axios.post("kcsapi/api_get_member/require_info")
            .then(res => {
                props.setRequireInfo(res.data)
                setRequireInfoLoaded(true)
            })
            .catch(error => {
                console.log(error)
            });
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