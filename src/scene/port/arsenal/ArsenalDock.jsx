import { useEffect, useState } from 'react';
import { Container, Sprite, Text } from '@pixi/react';
import * as AssetsFactory from '../../../common/AssetsFactory';
import { PixiButton } from '../../../common/PixiButton';

// 工廠ドック
export const ArsenalDock = (props) => {
    const [arsenalMain, setArsenalMain] = useState([])

    useEffect(() => {
        AssetsFactory.loadAsFrames("kcs2/img/arsenal/arsenal_main.json", setArsenalMain);
    }, []);

    if (arsenalMain.length === 0) {
        return null
    }

    return (
        <Container x={props.x} y={props.y}>
            {/* 状態 */}
            <Sprite texture={arsenalMain[144]} x={0} y={0} />
            {/* TODO 58開発中、59完了、60未登録 */}
            <Sprite texture={arsenalMain[60]} x={20} y={3} />
            {/* 残り時間 */}
            <Sprite texture={arsenalMain[156]} x={0} y={45} />
            <Text text={"00:00:00"} style={{ fontSize: 35 }} x={-10} y={70} />
            {/* 船 */}
            {/* <PixiButton default={arsenalMain[95]} hover={arsenalMain[96]} x={180} y={200} /> */}
        </Container>
    );
};