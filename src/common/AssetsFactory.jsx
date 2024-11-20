import { Assets, Texture } from 'pixi.js'

export const loadAsFrames = (spritesheet, setFrames) => {
    if (Assets.cache.has(spritesheet)) {
        setFrames(
            Object.keys(Assets.get(spritesheet).textures).map(frame =>
                Texture.from(frame)
            )
        );
    } else {
        Assets.load(spritesheet).then((data) => {
            setFrames(
                Object.keys(data.textures).map(frame =>
                    Texture.from(frame)
                )
            );
        });
    }
}

export const loadAsObject = (spritesheet, setObject) => {
    if (Assets.cache.has(spritesheet)) {
        setObject(Assets.get(spritesheet).textures);
    } else {
        Assets.load(spritesheet).then((data) => {
            setObject(data.textures);
        });
    }
}

// export const backgroundLoad = (resouce, setProgress) => {
//     if (setProgress === undefined) {
//         Assets.backgroundLoad(resouce);
//     } else {
//         Assets.backgroundLoad(resouce).then(() => {
//             setProgress(prevProgress => prevProgress + 1);
//         });
//     }
// }

// export const load = (resouce, setProgress) => {
//     if (setProgress === undefined) {
//         Assets.load(resouce);
//     } else {
//         Assets.load(resouce).then(() => {
//             setProgress(prevProgress => prevProgress + 1);
//         });
//     }
// }

export const loadFonts = () => {
    // Add font files to the bundle
    Assets.addBundle('fonts', [
        { alias: 'kcs-light', src: 'kcs2/resources/font/A-OTF-UDShinGoPro-Light.woff2' },
        { alias: 'kcs-regular', src: 'kcs2/resources/font/A-OTF-UDShinGoPro-Regular.woff2' },
    ]);
    Assets.loadBundle('fonts');
}