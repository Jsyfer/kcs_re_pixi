import * as PIXI from "pixi.js";

export class HenseiPanel{
    constructor() {
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        this.create();
    }

    create = async () => {
        const data = await PIXI.Assets.load('assets/kcs2/img/common/common_main.json');
        // 面板背景
        this.panelBg = new PIXI.Sprite(data.textures.common_main_15);
        this.panelBg.position.set(150,146);
        // 面板标题背景
        this.panelTitleBg = new PIXI.Sprite(data.textures.common_main_67);
        this.panelTitleBg.position.y = 104;
        // 面板标题
        this.panelTitle = new PIXI.Sprite(data.textures.common_main_1);
        this.panelTitle.position.set(195,114);

        this.hideAll();

        this.container.addChild(
            this.panelBg,
            this.panelTitleBg,
            this.panelTitle,
        )
    }

    hideAll = () => {
        this.panelBg.visible = false;
        this.panelTitleBg.visible = false;
        this.panelTitle.visible = false;
    }

    showAll = () => {
        this.panelBg.visible = true;
        this.panelTitleBg.visible = true;
        this.panelTitle.visible = true;
    }

}