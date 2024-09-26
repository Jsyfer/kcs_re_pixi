import * as PIXI from "pixi.js";
import { BASE_URL } from "../App";

export class ShipHensei {
    constructor() {
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        this.create();
    }

    create = async () => {
        const data_organize = await PIXI.Assets.load(BASE_URL + 'assets/kcs2/img/organize/organize_main.json');
        // 面板背景
        this.panelBgL = new PIXI.Sprite(data_organize.textures.organize_main_31);
        this.panelBgL.position.set(180, 189);
        this.panelBgR = new PIXI.Sprite(data_organize.textures.organize_main_32);
        this.panelBgR.position.set(426, 189);
        // 面板
        this.panel = new PIXI.Sprite(data_organize.textures.organize_main_30);
        this.panel.position.set(180, 189);

        // this.hideAll();

        this.container.addChild(
            this.panelBgL,
            this.panelBgR,
            this.panel,
        )
    }

    hideAll = () => {
        this.panelBgL.visible = false;
        this.panelBgR.visible = false;
        this.panel.visible = false;
    }

    showAll = () => {
        this.panelBgL.visible = true;
        this.panelBgR.visible = true;
        this.panel.visible = true;
    }

}