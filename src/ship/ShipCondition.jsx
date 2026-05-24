import { useRef } from 'react';
import { Container, Sprite, useTick } from '@pixi/react';
import * as AssetsFactory from '@common/AssetsFactory';
import { Twinkle } from '@common/Twinkle';

// 戒指
export const ShipCondition = (props) => {
    const commonMain = AssetsFactory.getSpritesheet("kcs2/img/common/common_main.json")

    const renderConditionSprite = () => {
        if (props.shipCondition > 49) {
            switch (props.size) {
                case 'small':
                    return <>
                        <Twinkle texture={commonMain[35]} x={0} y={0} />
                        <Twinkle texture={commonMain[35]} x={23} y={0} />
                        <Twinkle texture={commonMain[35]} x={46} y={0} />
                        <Twinkle texture={commonMain[35]} x={69} y={0} />
                        <Twinkle texture={commonMain[35]} x={90} y={0} />
                    </>
                case 'medium':
                    return <>
                        <Twinkle texture={commonMain[35]} x={0} y={25} />
                        <Twinkle texture={commonMain[35]} x={40} y={0} />
                        <Twinkle texture={commonMain[35]} x={60} y={20} />
                        <Twinkle texture={commonMain[35]} x={10} y={60} />
                        <Twinkle texture={commonMain[35]} x={60} y={40} />
                        <Twinkle texture={commonMain[35]} x={200} y={-5} />
                        <Twinkle texture={commonMain[35]} x={235} y={15} />
                        <Twinkle texture={commonMain[35]} x={215} y={25} />
                        <Twinkle texture={commonMain[35]} x={195} y={45} />
                        <Twinkle texture={commonMain[35]} x={230} y={55} />
                    </>
                default:
                    return <>
                        <Twinkle texture={commonMain[35]} x={props.x} y={props.y} />
                    </>
            }
        } else {
            return null;
        }
    }

    return (
        <Container x={props.x} y={props.y}>
            {renderConditionSprite()}
        </Container>
    );
};