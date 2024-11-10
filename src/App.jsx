import './App.css';
import { useState, useEffect, useCallback } from 'react';
import { Stage } from '@pixi/react';
import { PreLoading } from './loading/PreLoading';
import { StartScene } from './scene/StartScene';
import { PortScene } from './scene/PortScene';
import { ShipLoading } from './loading/ShipLoading';

const App = () => {
    const loadingDuration = 3000;
    const [isLoaded, setIsLoaded] = useState(false);
    const [sceneName, setSceneName] = useState("PreLoading");
    const [getData, setGetData] = useState(null);
    const [requireInfo, setRequireInfo] = useState(null);

    useEffect(() => {
        setTimeout(() => {
            setIsLoaded(true);
        }, 4000); // adjust the timeout to control the loading time
    }, []);

    const renderContent = useCallback(() => {
        if (sceneName === "PreLoading") {
            if (isLoaded) {
                return <StartScene setSceneName={setSceneName} />
            } else {
                return <PreLoading loadingDuration={loadingDuration} />
            }
        } else {
            switch (sceneName) {
                case "ShipLoading":
                    return <ShipLoading setSceneName={setSceneName} setGetData={setGetData} setRequireInfo={setRequireInfo} />
                case "Port":
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