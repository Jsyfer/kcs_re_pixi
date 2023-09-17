import * as PIXI from "pixi.js";
import { Tools } from "../system/Tools";
import { Scene } from "../system/Scene";

export class Welcome extends Scene {
    create() {
        this.createBackground();
    }
    createBackground() {
        const bg = Tools.massiveRequire(require["context"]('./../../assets/kcs2/img/title', true, /\.(mp3|png|jpe?g)$/));
        this.bg = PIXI.Sprite.from(bg[3].data.default);
        this.container.addChild(this.bg);

        const progressBar = new PIXI.Graphics();
        progressBar.beginFill(0x22a39f).drawRect(0, 0, 965, 25).endFill();
        progressBar.position.set(118,665);
        this.container.addChild(progressBar);

        const progressBarBorder = new PIXI.Graphics();
        progressBarBorder.lineStyle(3, 0xFFFFFF).drawRect(0, 0, 965, 25).endFill();
        progressBarBorder.position.set(118,665);
        this.container.addChild(progressBarBorder);

    }
}
