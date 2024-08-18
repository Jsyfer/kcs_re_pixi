import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import { BASE_URL } from "../App";

// 初始加载界面
export class Loading extends Scene {
    create() {
        this.container.addChild(PIXI.Sprite.from(BASE_URL + 'assets/kcs2/img/title/04.png'));

        this.progressBar = new PIXI.Graphics();
        this.progressBar.beginFill(0x22a39f).drawRect(0, 0, 965, 25).endFill();
        this.progressBar.position.set(118, 665);
        this.progressBar.scale.x = 0;
        this.container.addChild(this.progressBar);

        const progressBarBorder = new PIXI.Graphics();
        progressBarBorder.lineStyle(3, 0xFFFFFF).drawRect(0, 0, 965, 25).endFill();
        progressBarBorder.position.set(118, 665);
        this.container.addChild(progressBarBorder);

    }

    async update() {
        // 加载进度条动画
        const timer = ms => new Promise(res => setTimeout(res, ms))
        while (this.progressBar.scale.x < 0.99) {
            this.progressBar.scale.x += 0.02;
            await timer(500);
        }
    }

}
