import './App.css';
import { useState, useEffect, useCallback } from 'react';
import { Stage } from '@pixi/react';
import { PreLoadingScene } from './scene/PreLoadingScene';
import { StartScene } from './scene/StartScene';
import { PortScene } from './scene/PortScene';

const App = () => {
    const loadingDuration = 3000;
    const [isLoaded, setIsLoaded] = useState(false);
    const [sceneName, setSceneName] = useState("LoadingScene");
    const [getData, setGetData] = useState(null);
    const [requireInfo, setRequireInfo] = useState(null);

    useEffect(() => {
        setTimeout(() => {
            setIsLoaded(true);
        }, 4000); // adjust the timeout to control the loading time
    }, []);

    const renderContent = useCallback(() => {
        if (sceneName === "LoadingScene") {
            if (isLoaded) {
                return <StartScene setSceneName={setSceneName} />
            } else {
                return <PreLoadingScene loadingDuration={loadingDuration} setGetData={setGetData} setRequireInfo={setRequireInfo} />
            }
        } else {
            switch (sceneName) {
                case "PortScene":
                    return <PortScene setSceneName={setSceneName} getData={getData} requireInfo={requireInfo} />
                default:
                    return <StartScene />
            }
        }
    }, [sceneName, isLoaded])

    return (
        <Stage width={1200} height={720} options={{ background: 0x000000 }}>
            {renderContent()}
        </Stage>
    );
};

export default App;