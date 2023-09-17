import * as PIXI from "pixi.js";

export class Loader {
    constructor(config) {
        this.config = config;
        this.resources = {}
    }

    preload() {
        for (const asset of this.config.assets) {
            let key = asset.key;
            if (asset.key.indexOf(".png") !== -1 || asset.key.indexOf(".jpg") !== -1) {
                PIXI.Assets.add(key,asset.data);
            }
        }
    }
}