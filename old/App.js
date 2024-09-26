import * as PIXI from "pixi.js";
import { Loading } from "./scene/Loading";
import { Start } from "./scene/Start";
import { Port } from "./scene/Port";


class Application {
    async run() {
        // 创建主程序
        this.app = new PIXI.Application({ width: 1200, height: 720 });
        document.body.appendChild(this.app.view);
        // 创建化加载界面
        this.loading = new Loading();
        // 创建开始界面
        this.start = new Start();
        // 创建母港界面
        this.port = new Port();
        // 添加加载界面至主程序
        this.app.stage.addChild(this.loading.container);
        // 运行加载界面
        this.loading.update().then(() => {
            // 加载界面完成运行后显示开始界面
            this.app.stage.addChild(this.start.container)
            // 删除加载界面
            this.app.stage.removeChildAt(0);
        });
    }
}

export const App = new Application();
export const BASE_URL = "http://127.0.0.1:8000/"