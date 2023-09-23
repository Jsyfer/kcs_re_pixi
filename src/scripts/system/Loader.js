import * as PIXI from "pixi.js";

export class Loader {
    constructor(config) {
        this.config = config;
        this.resources = {}
    }

    preload() {
        for (const [key, val] of Object.entries(this.config.assets)) {
            if (key.indexOf(".png") !== -1 || key.indexOf(".jpg") !== -1) {
                PIXI.Assets.add(key,val);
            }
        }
    }
}