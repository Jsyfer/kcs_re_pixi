import { useRef } from 'react';
import { Container, Sprite, useTick } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';

// 戒指
export const Ring = (props) => {
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")

    const spriteRef = useRef(null);
    const angle = useRef(0);
    const centerX = -12;
    const centerY = -12;
    const radiusX = 20; // 椭圆长轴
    const radiusY = 10; // 椭圆短轴
    const speed = 0.015;
    // 椭圆整体逆时针旋转45°
    const rotate = -Math.PI / 4;

    useTick((delta) => {
        angle.current += speed * delta;
        if (spriteRef.current) {
            angle.current += speed * delta;
            if (!spriteRef.current) return;
            // ① 先算普通水平椭圆
            const localX = radiusX * Math.cos(angle.current);
            const localY = radiusY * Math.sin(angle.current);
            // ② 整体逆时针旋转45°
            const rotatedX = localX * Math.cos(rotate) - localY * Math.sin(rotate);
            const rotatedY = localX * Math.sin(rotate) + localY * Math.cos(rotate);
            // ③ 平移回中心
            spriteRef.current.x = centerX + rotatedX;
            spriteRef.current.y = centerY + rotatedY;
        }
    });

    const spriteRefAlpha = useRef(null);
    const blinkTime = useRef(0);

    useTick((delta) => {
        blinkTime.current += 0.03 * delta;
        if (!spriteRefAlpha.current) return;
        spriteRefAlpha.current.alpha = 0.7 + 0.3 * Math.sin(blinkTime.current);
    });

    return (
        <Container x={props.x} y={props.y}>
            <Sprite texture={commonMisc[180]} ref={spriteRef} />
            <Sprite texture={commonMisc[179]} ref={spriteRefAlpha} />
        </Container>
    );
};