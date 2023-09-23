import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import { Button } from "../system/Button";

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

            const btn_default = new Button({
                default: data.textures.title_main_4,
                disabled: data.textures.title_main_6,
                down: data.textures.title_main_5,
                hover: data.textures.title_main_7,
            });
            btn_default.button.position.set(650,550);

            this.container.addChild(logo,btn_default.button);
        })

    }
}
