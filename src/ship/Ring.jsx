import { useRef, useState, useEffect } from 'react';
import { Container, Sprite, useTick } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';

// 戒指
export const Ring = (props) => {
    const commonMisc = AssetsFactory.getSpritesheet("kcs2/img/common/common_misc.json")

    const spriteRef = useRef(null);
    const angle = useRef(0);

    const [config, setConfig] = useState({
        textureRing: commonMisc[177],
        textureLight: commonMisc[178],
        centerX: 0, // 椭圆中心X坐标
        centerY: 0, // 椭圆中心Y坐标
        radiusX: 40, // 椭圆长轴
        radiusY: 20, // 椭圆短轴
        speed: 0.015, // 旋转速度
        rotate: -Math.PI / 4, // 整体逆时针旋转45°
    });
    useEffect(() => {
        switch (props.size) {
            case 'small':
                setConfig({
                    textureRing: commonMisc[179],
                    textureLight: commonMisc[180],
                    centerX: -12, // 椭圆中心X坐标
                    centerY: -12, // 椭圆中心Y坐标
                    radiusX: 20, // 椭圆长轴
                    radiusY: 10, // 椭圆短轴
                    speed: 0.015, // 旋转速度
                    rotate: -Math.PI / 4, // 整体逆时针旋转45°
                });
                break;
            case 'medium':
                setConfig({
                    textureRing: commonMisc[181],
                    textureLight: commonMisc[182],
                    centerX: -12, // 椭圆中心X坐标
                    centerY: -12, // 椭圆中心Y坐标
                    radiusX: 20, // 椭圆长轴
                    radiusY: 10, // 椭圆短轴
                    speed: 0.015, // 旋转速度
                    rotate: -Math.PI / 4, // 整体逆时针旋转45°
                });
                break;
            default:
                // large or default size
                setConfig({
                    textureRing: commonMisc[177],
                    textureLight: commonMisc[178],
                    centerX: 0, // 椭圆中心X坐标
                    centerY: 0, // 椭圆中心Y坐标
                    radiusX: 40, // 椭圆长轴
                    radiusY: 20, // 椭圆短轴
                    speed: 0.015, // 旋转速度
                    rotate: -Math.PI / 4, // 整体逆时针旋转45°
                });
                break;
        }
    }, [props.size]);


    useTick((delta) => {
        angle.current += config.speed * delta;
        if (spriteRef.current) {
            angle.current += config.speed * delta;
            if (!spriteRef.current) return;
            // ① 先算普通水平椭圆
            const localX = config.radiusX * Math.cos(angle.current);
            const localY = config.radiusY * Math.sin(angle.current);
            // ② 整体逆时针旋转45°
            const rotatedX = localX * Math.cos(config.rotate) - localY * Math.sin(config.rotate);
            const rotatedY = localX * Math.sin(config.rotate) + localY * Math.cos(config.rotate);
            // ③ 平移回中心
            spriteRef.current.x = config.centerX + rotatedX;
            spriteRef.current.y = config.centerY + rotatedY;
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
            <Sprite texture={config.textureLight} ref={spriteRef} />
            <Sprite texture={config.textureRing} ref={spriteRefAlpha} />
        </Container>
    );
};