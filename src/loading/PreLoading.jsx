import { useState, useEffect } from 'react';
import { Container, Graphics, Sprite } from '@pixi/react';
import * as AssetsFactory from '../common/AssetsFactory';
import resources from '../resources.json'

const rndInt = Math.floor(Math.random() * 6) + 1

export const PreLoading = (props) => {
    const [progress, setProgress] = useState(0);
    const loadingImg = `kcs2/img/title/0${rndInt}.png`;
    const assetsLength = resources.assets.length;

    useEffect(() => {
        // load fonts
        // AssetsFactory.loadFonts();
        // preload assets
        resources.assets.forEach(item => {
            if (item.endsWith('.png')) {
                AssetsFactory.load(item, setProgress);
            } else {
                AssetsFactory.backgroundLoad(item, setProgress);
            }
        });
    }, []);

    if (progress >= assetsLength) {
        props.setIsLoaded(true);
    }

    return (
        <Container>
            <Sprite image={loadingImg} x={0} y={0} />
            {/* Progress Bar */}
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.beginFill(0x22a39f);
                    g.drawRect(118, 665, (progress / assetsLength) * 965, 25);
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