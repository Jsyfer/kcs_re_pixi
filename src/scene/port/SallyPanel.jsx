import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '../../common/AssetsFactory';
import { PixiButton } from '../../common/PixiButton';

// 出航
export const SallyPanel = () => {
    const sallyTop = AssetsFactory.getSpritesheet("kcs2/img/sally/sally_top.json");
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json");

    return (
        <Container x={0} y={0}>
            <Sprite image={'kcs2/img/common/bg/016.png'} x={0} y={0} />
            <Sprite texture={commonMain[67]} x={0} y={104} />
            <Sprite texture={sallyTop[0]} x={195} y={114} />
            <PixiButton default={sallyTop[8]} hover={sallyTop[9]} x={179} y={174} />
            <Sprite texture={sallyTop[10]} x={246} y={575} />
            <PixiButton default={sallyTop[1]} hover={sallyTop[2]} x={516} y={174} />
            <Sprite texture={sallyTop[3]} x={572} y={575} />
            <PixiButton default={sallyTop[4]} hover={sallyTop[6]} x={852} y={174} />
            <Sprite texture={sallyTop[7]} x={909} y={575} />
        </Container>
    );
};