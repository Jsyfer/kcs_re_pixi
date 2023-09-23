import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import title from './../../assets/kcs2/img/title/04.png'

// 初始加载界面
export class Loading extends Scene {
    create() {
        this.container.addChild(PIXI.Sprite.from(title));

        const progressBar = new PIXI.Graphics();
        progressBar.beginFill(0x22a39f).drawRect(0, 0, 965, 25).endFill();
        progressBar.position.set(118,665);
        progressBar.scale.x = 0;
        this.container.addChild(progressBar);

        const progressBarBorder = new PIXI.Graphics();
        progressBarBorder.lineStyle(3, 0xFFFFFF).drawRect(0, 0, 965, 25).endFill();
        progressBarBorder.position.set(118,665);
        this.container.addChild(progressBarBorder);

        // 加载进度条动画
        return new Promise(async function(resolve) {
            const timer = ms => new Promise(res => setTimeout(res, ms))
            while (progressBar.scale.x < 0.99) {
                progressBar.scale.x += 0.05;
                await timer(100);
            }
            resolve();
        });
    }

}
