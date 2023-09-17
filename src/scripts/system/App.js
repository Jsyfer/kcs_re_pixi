import * as PIXI from "pixi.js";
import { Loader } from "./Loader";
import { ScenesManager } from "./ScenesManager";
import { Loading } from "../game/Loading";

class Application {
    run(config) {
        // 读取配置文件
        this.config = config;
        // 创建主程序
        this.app = new PIXI.Application({ width: 1200, height: 720 });
        document.body.appendChild(this.app.view);
        // 初始化场景管理器
        this.scenesManager = new ScenesManager();
        // 初始化加载界面
        const loading = new Loading();
        // 添加加载界面至主程序
        this.app.stage.addChild(loading.container);
        // 运行加载界面
        loading.create().then(() => {
            // 加载界面完成运行后载入场景管理器
            this.app.stage.addChild(this.scenesManager.container)
        });
        // 加载资源
        this.loader = new Loader(this.config).preload();
        // 运行开始界面
        this.scenesManager.start("Start");
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
