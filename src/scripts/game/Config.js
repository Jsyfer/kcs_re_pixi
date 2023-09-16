import { Welcome } from "./Welcome";
import { Game } from "./Game";
import { Port } from "./Port";
import { Tools } from "../system/Tools";

export const Config = {
    loader: Tools.massiveRequire(require["context"]('./../../assets/kcs2/img', true, /\.(mp3|png|jpe?g)$/)),
    scenes: {
        "Welcome": Welcome,
        "Game": Game,
        "Port": Port
    }
};