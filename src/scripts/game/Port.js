import { App } from "../system/App";
import { Scene } from "../system/Scene";

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
