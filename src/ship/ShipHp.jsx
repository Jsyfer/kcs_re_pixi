import { Container, Graphics, Sprite } from '@pixi/react';
import { getShipHpColor } from '@ship/shipCommon';

// HP显示
export const ShipHp = (props) => {
    const hp_length = 92;

    return (
        <Container x={props.x} y={props.y}>
            <Sprite image={"/kcs2/img/common/hpgauge/hp_gauge_mask.png"} x={-2} y={-3} />
            <Sprite image={"/kcs2/img/common/hpgauge/hp_s_bg2.png"} x={-2} y={-3} />
            <Graphics
                draw={(g) => {
                    g.clear();
                    g.beginFill(getShipHpColor(props.nowhp, props.maxhp));
                    g.drawRoundedRect(0, 0, props.nowhp / props.maxhp * hp_length, 5, 5);
                    g.endFill();
                }}
            />
        </Container>
    );
};