import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";

// 开始界面
export class Start extends Scene {
    create() {
        // 打开容器内的对象排序
        this.container.sortableChildren = true
        // 添加背景
        PIXI.Assets.load('assets/kcs2/img/title/title2.png').then(value => {
            const bg = new PIXI.Sprite(value);
            bg.zIndex = -1;
            this.container.addChild(bg);
        });

        // 添加按钮
        PIXI.Assets.load("assets/kcs2/img/title/title_main.json").then((data) => {
            const logo = new PIXI.Sprite(data.textures.title_main_3);
            logo.position.set(775,110);
            const btn_default = new PIXI.Sprite(data.textures.title_main_4);
            btn_default.position.set(650,550);
            this.container.addChild(logo,btn_default);
        })

    }
}
