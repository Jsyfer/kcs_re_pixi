import { useState, useEffect } from 'react';
import { Container, Graphics, Sprite, useTick } from '@pixi/react';
import { Assets } from 'pixi.js'
import resources from '../resources.json'
import axios from 'axios';

const rndInt = Math.floor(Math.random() * 6) + 1

export const PreLoadingScene = (props) => {
    const [progress, setProgress] = useState(0);
    const loadingImg = `assets/kcs2/img/title/0${rndInt}.png`;

    // adjust the interval to control the loading speed
    useTick((delta) => {
        setProgress((prevProgress) => Math.min(prevProgress + delta * (100 / 60) / (props.loadingDuration / 1000), 100));
    });

    useEffect(() => {
        // preload assets
        Assets.backgroundLoad(loadingImg);
        resources.assets.forEach(item => {
            if (item.endsWith('.png')) {
                Assets.load(item);
            } else {
                Assets.backgroundLoad(item);
            }
        });
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
                props.setRequireInfo(res.data)
            })
            .catch(error => {
                console.log(error)
            });
    }, []);

    return (
        <Container>
            <Sprite image={loadingImg} x={0} y={0} />
            {/* Progress Bar */}
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.beginFill(0x22a39f);
                    g.drawRect(118, 665, (progress / 100) * 965, 25);
                    g.endFill();
                }}
            />
            {/* Progress Bar Border */}
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.lineStyle(3, 0xFFFFFF);
                    g.drawRect(118, 665, 965, 25);
                    g.endFill();
                }}
            />
        </Container>
    );
};