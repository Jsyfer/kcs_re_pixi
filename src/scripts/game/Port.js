import { App } from "../system/App";
import { Scene } from "../system/Scene";

// 母港界面
export class Port extends Scene {
    create() {
        this.createPort();
        console.log("after port created")
    }
    createPort() {
        this.bg = App.sprite("./port/port_main.png");
        this.container.addChild(this.bg);
    }
}
