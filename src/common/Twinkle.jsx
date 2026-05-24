import { useRef } from 'react';
import { Sprite, useTick } from '@pixi/react';

export const Twinkle = (props) => {
    const spriteRef = useRef(null);

    const config = useRef({
        time: Math.random() * 5,
        // 固定渐变
        fadeIn: 0.05,
        fadeOut: 0.05,
        // 随机停留
        visible: 0.12,
        hidden: Math.random() * 0.5,
    });

    useTick((delta) => {
        if (!spriteRef.current) return;
        const s = config.current;
        s.time += delta / 60;
        const cycle = s.fadeIn + s.visible + s.fadeOut + s.hidden;
        const t = s.time % cycle;
        let alpha = 0;
        if (t < s.fadeIn) {
            // 淡入
            alpha = t / s.fadeIn;
        } else if (t < s.fadeIn + s.visible) {
            // 保持亮
            alpha = 1;
        } else if (t < s.fadeIn + s.visible + s.fadeOut) {
            // 淡出
            alpha = 1 - (t - s.fadeIn - s.visible) / s.fadeOut;
        } else {
            // 灭
            alpha = 0;
        }
        spriteRef.current.alpha = alpha;
    });

    return (
        <Sprite
            ref={spriteRef}
            texture={props.texture}
            x={props.x}
            y={props.y}
            anchor={0.5}
        />
    );
}