import { App } from "../system/App";
import { Scene } from "../system/Scene";

export class Game extends Scene {
    create() {
        this.createBackground();
    }
    createBackground() {
        this.bg = App.sprite("./img/title/01.png");
        this.container.addChild(this.bg);
    }
}
