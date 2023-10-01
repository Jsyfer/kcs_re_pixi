import * as PIXI from "pixi.js";
import { RingButton } from "../system/RingButton";
import { RingCenterButton } from "../system/RingCenterButton";

export class PortMainMenu{
    constructor(config) {
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        PIXI.Assets.load("assets/kcs2/img/port/port_ringmenu.json").then((data) => {
            // 改装按钮
            this.kaisouBtn = new RingButton({
                type: "kaisou",
                textures: data.textures,
            });
            this.kaisouBtn.button.position.set(477,335);
            // 工廠按钮
            this.koujyouBtn = new RingButton({
                type: "koujyou",
                textures: data.textures,
            });
            this.koujyouBtn.button.position.set(406,543);
            // 出撃按钮
            this.syutsugekiBtn = new RingCenterButton({
                textures: data.textures,
            });
            this.syutsugekiBtn.button.position.set(294,390);
            // 入渠按钮
            this.nyuukyoBtn = new RingButton({
                type: "nyuukyo",
                textures: data.textures,
            });
            this.nyuukyoBtn.button.position.set(186,543);
            // 補給按钮
            this.hokyuuBtn = new RingButton({
                type: "hokyuu",
                textures: data.textures,
            });
            this.hokyuuBtn.button.position.set(118,335);
            // 編成按钮
            this.henseiBtn = new RingButton({
                type: "hensei",
                textures: data.textures,
            });
            this.henseiBtn.button.position.set(296,202);
            // 添加 logo和按钮至容器
            this.container.addChild(this.kaisouBtn.button,this.koujyouBtn.button,this.nyuukyoBtn.button,this.syutsugekiBtn.button,this.hokyuuBtn.button,this.henseiBtn.button);
        })
    }

}