import { Container, Sprite } from '@pixi/react';

export const ShipPowerUpStatus = (props) => {

    const isPowerUpMax = (property) => {
        if (property[1] === 0) {
            return true;
        }
        if (property[0] / property[1] > 0.89) {
            return true;
        }
        return false;
    }

    const powerUpLv = () => {
        // TODO calculation method need to identify
        let result = 1;
        if (isPowerUpMax(props.target_ship.api_karyoku)) {
            result += 1;
        }
        if (isPowerUpMax(props.target_ship.api_raisou)) {
            result += 1;
        }
        if (isPowerUpMax(props.target_ship.api_taiku)) {
            result += 1;
        }
        if (isPowerUpMax(props.target_ship.api_soukou)) {
            result += 1;
        }
        return result;
    }

    return (
        <Container x={props.x} y={props.y}>
            {Array.from({ length: powerUpLv() }, (_, i) => <Sprite key={i} texture={props.texture} x={18 * i} y={0} />)}
        </Container>
    );
};