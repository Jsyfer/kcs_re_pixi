import './App.css';
import { useState, useCallback, useEffect } from 'react';
import { Stage } from '@pixi/react';
import { PreLoading } from './loading/PreLoading';
import { StartScene } from './scene/StartScene';
import { PortScene } from './scene/PortScene';
import { ShipLoading } from './loading/ShipLoading';
import { Assets } from 'pixi.js'

const rndInt = Math.floor(Math.random() * 6) + 1
const loadingImg = `kcs2/img/title/0${rndInt}.png`;

const App = () => {
    const [isLoaded, setIsLoaded] = useState(false);
    const [sceneName, setSceneName] = useState("PreLoading");
    const [bgImageLoaded, setBgImageLoaded] = useState(false);

    useEffect(() => {
        Assets.load(loadingImg).then(res => {
            setBgImageLoaded(true);
        });
    }, []);

    const renderContent = useCallback(() => {
        if (bgImageLoaded) {
            if (sceneName === "PreLoading") {
                if (isLoaded) {
                    return <StartScene setSceneName={setSceneName} />
                } else {
                    return <PreLoading setIsLoaded={setIsLoaded} loadingImg={loadingImg} />
                }
            } else {
                switch (sceneName) {
                    case "ShipLoading":
                        return <ShipLoading setSceneName={setSceneName} />
                    case "Port":
                        return <PortScene />
                    default:
                        return <StartScene />
                }
            }
        } else {
            return null;
        }
    }, [bgImageLoaded, sceneName, isLoaded])

    return (
        <Stage width={1200} height={720} options={{ background: 0x000000 }}>
            {renderContent()}
        </Stage>
    );
};

export default App;