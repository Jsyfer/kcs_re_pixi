import * as PIXI from "pixi.js";
import { Loading } from "./scene/Loading";
import { Start } from "./scene/Start";


class Application {
    run(config) {
        // 读取配置文件
        this.config = config;
        // 创建主程序
        this.app = new PIXI.Application({ width: 1200, height: 720 });
        document.body.appendChild(this.app.view);
        // 创建化加载界面
        const loading = new Loading();
        // 创建开始载界面
        const start = new Start();
        
        // 添加加载界面至主程序
        this.app.stage.addChild(loading.container);
        // 运行加载界面
        loading.create().then(() => {
            // 加载界面完成运行后载入场景管理器
            this.app.stage.addChild(start.container)
            // 删除加载界面
            this.app.stage.removeChildAt(0);
        });
        // TODO 开始按钮按下后切换至母港界面

    }

    res(key) {
        return this.loader.resources[key].texture;
    }

    sprite(key) {
        return new PIXI.Sprite(this.res(key));
    }

}

export const App = new Application();
