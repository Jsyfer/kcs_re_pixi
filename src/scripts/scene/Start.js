import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import { Button } from "../system/Button";
import { App } from "../App";

// 开始界面
export class Start extends Scene {
    create() {
        // 添加背景
        const bg = PIXI.Sprite.from('assets/kcs2/img/title/title2.png');
        bg.zIndex = -1;
        this.container.addChild(bg);
        // 添加 logo 和 按钮
        PIXI.Assets.load("assets/kcs2/img/title/title_main.json").then((data) => {
            // 添加 logo
            const logo = new PIXI.Sprite(data.textures.title_main_3);
            logo.position.set(775,110);
            // 添加游戏开始按钮
            this.btn_default = new Button({
                default: data.textures.title_main_4,
                disabled: data.textures.title_main_6,
                down: data.textures.title_main_5,
                hover: data.textures.title_main_7,
                eventUp: this.moveToPort,
            });
            this.btn_default.button.position.set(650,800);
            // 禁用按钮
            this.btn_default.disable()
            // 添加 logo和按钮至容器
            this.container.addChild(logo,this.btn_default.button);
        })
    }

    // 开始按钮按下后切换至母港界面
    moveToPort = () => {
        App.app.stage.removeChildAt(0);
        App.app.stage.addChild(App.port.container);
    }

    update () {
        // 设置按钮出现动画
        if (this.btn_default) {
            if (this.btn_default.button.position.y > 550) {
                this.btn_default.button.position.y -= 2;
            } else {
                // 动画结束后重新将按钮设定为有效
                if(!this.btn_default.button.isInteractive()){
                    this.btn_default.enable()
                }
            }
        }
    }

}
