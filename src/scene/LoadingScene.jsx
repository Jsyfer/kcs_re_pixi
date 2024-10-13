import { useState, useEffect } from 'react';
import { Container, Graphics, Sprite, useTick } from '@pixi/react';
import { Assets } from 'pixi.js'

const assets = [
    'assets/kcs2/img/title/title_main.json',
    'assets/kcs2/img/port/port_skin_1.json',
    'assets/kcs2/img/port/port_sidemenu.json',
    'assets/kcs2/img/port/port_ringmenu.json',
    'assets/kcs2/img/common/common_main.json',
    'assets/kcs2/img/sally/sally_top.json',
    'assets/kcs2/resources/font/A-OTF-UDShinGoPro-Light.woff2',
    'assets/kcs2/img/title/title2.png',
    'assets/kcs2/resources/furniture/normal/494_1648.png',
    'assets/kcs2/resources/furniture/normal/502_8118.png',
    'assets/kcs2/resources/furniture/outside/window_bg_4-2.png',
    'assets/kcs2/resources/furniture/normal/491_9688.png',
    'assets/kcs2/resources/furniture/normal/499_8458.png',
    'assets/kcs2/resources/furniture/normal/493_4897.png',
    'assets/kcs2/resources/furniture/normal/498_8534.png',
    'assets/kcs2/resources/ship/full/0538_2823_sullpopastgr.png',
    'assets/kcs2/img/common/bg/011.png',
    'assets/kcs2/img/common/bg/012.png',
    'assets/kcs2/img/common/bg/013.png',
    'assets/kcs2/img/common/bg/014.png',
    'assets/kcs2/img/common/bg/015.png',
    'assets/kcs2/img/common/bg/016.png',
    'assets/kcs2/img/common/bg/031.png',
]

export const LoadingScene = (props) => {
    const [progress, setProgress] = useState(0);
    const loadingImg = "assets/kcs2/img/title/04.png";

    // adjust the interval to control the loading speed
    useTick((delta) => {
        setProgress((prevProgress) => Math.min(prevProgress + delta * (100 / 60) / (props.loadingDuration / 1000), 100));
    });

    useEffect(() => {
        assets.forEach(item => {
            if (item.endsWith('.json')) {
                Assets.backgroundLoad(item);
            } else {
                Assets.load(item);
            }
        })
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