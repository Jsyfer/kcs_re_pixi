import { useState, useEffect } from 'react';
import { Container, Graphics, Sprite, useTick } from '@pixi/react';
import { Assets } from 'pixi.js'
import resources from '../resources.json'
import axios from 'axios';

const rndInt = Math.floor(Math.random() * 6) + 1

export const LoadingScene = (props) => {
    const [progress, setProgress] = useState(0);
    const loadingImg = `assets/kcs2/img/title/0${rndInt}.png`;

    // adjust the interval to control the loading speed
    useTick((delta) => {
        setProgress((prevProgress) => Math.min(prevProgress + delta * (100 / 60) / (props.loadingDuration / 1000), 100));
    });

    useEffect(() => {
        // get common game data
        axios.post("kcsapi/api_start2/getData")
            .then(res => {
                props.setGetData(res.data)
            })
            .catch(error => {
                console.log(error)
            });
        axios.post("kcsapi/api_get_member/require_info")
            .then(res => {
            })
            .catch(error => {
                console.log(error)
            });
    }, []);

    return (
        <Container>

        </Container>
    );
};