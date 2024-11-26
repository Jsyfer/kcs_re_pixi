import { useState, useEffect } from 'react';
import { Container, Sprite } from '@pixi/react';
import { Assets } from 'pixi.js'
import resouces_mapping from '../resources_mapping.json';
import * as AssetsFactory from '../common/AssetsFactory';
import * as ApiFactory from '../common/ApiFactory';

export const ShipLoading = (props) => {
    const [titleMainTextures, setTitleMainTextures] = useState([])
    const [getDataLoaded, setGetDataLoaded] = useState(false)
    const [requireInfoLoaded, setRequireInfoLoaded] = useState(false)
    const [furnitureLoaded, setFurnitureLoaded] = useState(false)
    const [portData, setPortData] = useState(null);

    useEffect(() => {
        AssetsFactory.loadAsFrames('kcs2/img/title/title_main.json', setTitleMainTextures);
        // get common game data
        ApiFactory.get("kcsapi/api_port/port", setPortData)
        ApiFactory.get("kcsapi/api_start2/getData", props.setGetData, setGetDataLoaded)
        ApiFactory.get("kcsapi/api_get_member/require_info", props.setRequireInfo, setRequireInfoLoaded)
        if (portData !== null) {
            portData.api_data.api_basic.api_furniture.forEach(async (furniture_key, idx, array) => {
                const furniture = resouces_mapping.furniture.find(item => item.api_id === furniture_key).furniture;
                // await fetch("kcs2/resources/furniture/normal/" + furniture);
                await Assets.load("kcs2/resources/furniture/normal/" + furniture);
                if (idx === array.length - 1) {
                    setFurnitureLoaded(true)
                }
            })
        }
    }, [portData]);

    if (titleMainTextures.length === 0) {
        return null
    }

    if (getDataLoaded && requireInfoLoaded && furnitureLoaded) {
        props.setSceneName("Port")
    }

    return (
        <Container x={0} y={0}>
            <Sprite x={600} y={360} texture={titleMainTextures[0]} anchor={0.5} />
            <Sprite x={600} y={330} texture={titleMainTextures[1]} anchor={0.5} />
        </Container>
    );
};