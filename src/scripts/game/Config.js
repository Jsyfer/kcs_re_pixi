import { Loading } from "./Loading";
import { Start } from "./Start";
import { Port } from "./Port";
import { Tools } from "../system/Tools";

export const Config = {
    assets: Tools.massiveRequire(require["context"]('./../../assets/kcs2', true, /\.(json|mp3|png|jpe?g)$/)),
    scenes: {
        "Loading": Loading,
        "Start": Start,
        "Port": Port
    }
};