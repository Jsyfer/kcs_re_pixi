import * as PIXI from "pixi.js";
import { Loader } from "./Loader";
import { ScenesManager } from "./ScenesManager";

class Application {
    run(config) {

        this.config = config;

        this.app = new PIXI.Application({ width: 1200, height: 720 });
        document.body.appendChild(this.app.view);

        this.scenes = new ScenesManager();
        this.app.stage.addChild(this.scenes.container);

        // 加载界面
        const loadingResult = this.scenes.start("Loading");
        // 游戏加载
        this.loader = new Loader(this.config).preload();
        // 加载完成
        console.log(loadingResult);
        if (loadingResult) {
            this.scenes.start("Start");
        }
        // TODO 开始按钮按下后切换至母港界面
        // this.scenes.start("Port")

    }

    res(key) {
        return this.loader.resources[key].texture;
    }

    sprite(key) {
        return new PIXI.Sprite(this.res(key));
    }

}

export const App = new Application();
