import { Container, Sprite } from '@pixi/react';
import { PixiButton } from '../../../common/PixiButton';

export const ShipCard = (props) => {

    return (
        <Container x={props.x} y={props.y}>
            {props.fleet[props.shipIndex] === -1 ?
                <>
                    <Sprite texture={props.organizeMain[31]} x={0} y={0} />
                    <Sprite texture={props.organizeMain[32]} x={246} y={0} />
                </>
                :
                <>
                    {/* background */}
                    <Sprite texture={props.organizeMain[30]} x={0} y={0} />
                    {/* 番号 */}
                    <Sprite texture={props.commonMisc["" + 3 + props.shipIndex]} x={-15} y={0} />

                    {/* TODO EXP (wrap in component)*/}
                    <Sprite texture={props.commonMain[21]} x={241} y={87} />
                    <Sprite texture={props.commonMain[22]} x={244} y={90} />
                    {/* 詳細 */}
                    <PixiButton
                        default={props.organizeMain[9]}
                        hover={props.organizeMain[10]}
                        x={250}
                        y={103}
                    />
                </>
            }
            {
                (props.lastShipIndex === -1 || props.lastShipIndex >= props.shipIndex) ?
                    // 変更
                    <PixiButton
                        default={props.organizeMain[24]}
                        hover={props.organizeMain[25]}
                        x={378}
                        y={103}
                    />
                    :
                    null
            }
        </Container>
    );
};