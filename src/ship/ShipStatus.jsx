import { useCallback } from 'react';
import { Container, Sprite } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';

// 小破/中破/大破/遠征中/修理中 显示
// TODO 破壊、退避等状态显示
export const ShipStatus = (props) => {
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")

    const render = useCallback(() => {
        if (props.isExpediting) {
            // 遠征中は遠征アイコンを表示
            return <Sprite texture={commonMisc[props.size === "large" ? 96 : 105]} />;
        }
        if (props.isFixing) {
            // 修理中は修理アイコンを表示
            return <Sprite texture={commonMisc[props.size === "large" ? 99 : 115]} />;
        }
        const hpRatio = props.nowHp / props.maxHp;
        if (hpRatio > 0.75) {
            return null;
        } else if (hpRatio > 0.5) {
            return <Sprite texture={commonMisc[props.size === "large" ? 98 : 112]} />;
        } else if (hpRatio > 0.25) {
            return <Sprite texture={commonMisc[props.size === "large" ? 95 : 104]} />;
        } else if (hpRatio > 0) {
            return <Sprite texture={commonMisc[props.size === "large" ? 100 : 116]} />;
        } else {
            return <Sprite texture={commonMisc[107]} />;
        }
    }, [props.nowHp, props.maxHp])

    return (
        <Container x={props.x} y={props.y}>
            {render()}
        </Container>
    );
};