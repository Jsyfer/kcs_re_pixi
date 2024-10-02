import { Container, Sprite } from '@pixi/react';


export const PortBackground = () => {
    return (
        <Container x={0} y={0}>
            {/* 家具 */}
            <Sprite image={'assets/kcs2/resources/furniture/normal/494_1648.png'} y={415.5} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/502_8118.png'} />
            <Sprite image={'assets/kcs2/resources/furniture/outside/window_bg_4-2.png'} x={300} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/491_9688.png'} x={300} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/499_8458.png'} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/493_4897.png'} y={200} />
            <Sprite image={'assets/kcs2/resources/furniture/normal/498_8534.png'} x={870} />
            {/* 舰娘 */}
            <Sprite image={'assets/kcs2/resources/ship/full/0538_2823_sullpopastgr.png'} x={400} y={100} />
        </Container>
    );
};