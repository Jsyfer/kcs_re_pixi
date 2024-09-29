import { useState } from 'react';
import { Container, Text, Sprite, useTick } from '@pixi/react';
import { PortTopMenu } from './menu/PortTopMenu';

export const PortScene = () => {

    const [angle, setAngle] = useState(0);

    // useTick(delta => setAngle(r => r + (0.01 * delta)))

    // const renderContent = useCallback(() => {
    //     if (sceneName === "LoadingScene") {
    //         if (isLoaded) {
    //             return <StartScene setSceneName={setSceneName} />
    //         } else {
    //             return <LoadingScene loadingDuration={loadingDuration} />
    //         }
    //     } else {
    //         switch (sceneName) {
    //             case "PortScene":
    //                 return <PortScene />
    //             case "StartScene":
    //                 return <StartScene />
    //             default:
    //                 return <StartScene />
    //         }
    //     }
    // }, [sceneName, isLoaded])

    return (
        <Container x={0} y={0}>
            <PortTopMenu />
        </Container>
    );
};
