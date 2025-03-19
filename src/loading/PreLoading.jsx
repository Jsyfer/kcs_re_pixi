import { useState, useEffect } from 'react';
import { Container, Graphics, Sprite } from '@pixi/react';
import resources from '../resources.json'
import { Assets } from 'pixi.js'

// 预加载界面
export const PreLoading = (props) => {
    const [progress, setProgress] = useState(0);
    const assetsLength = resources.assets.length;

    useEffect(() => {
        // load fonts
        // AssetsFactory.loadFonts();
        // preload assets
        resources.assets.forEach(async item => {
            await Assets.load(item);
            setProgress(prevProgress => prevProgress + 1);
        });
    }, []);

    if (progress >= assetsLength) {
        props.setIsLoaded(true);
    }

    return (
        <Container>
            <Sprite image={props.loadingImg} x={0} y={0} />
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