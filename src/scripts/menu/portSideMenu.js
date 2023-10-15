import * as PIXI from "pixi.js";
import { Button } from "../system/Button";

export class PortSideMenu{
    constructor() {
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        this.create();
        
    }

    create = async () => {
        const data = await PIXI.Assets.load("assets/kcs2/img/port/port_sidemenu.json")
        // backgtround
        this.bg1 = new PIXI.Sprite(data.textures.port_sidemenu_0);
        this.bg1.position.set(0,185);
        this.bg2 = new PIXI.Sprite(data.textures.port_sidemenu_1);
        this.bg2.position.set(0,210);
        // 吊车
        this.craneBase = new PIXI.Sprite(data.textures.port_sidemenu_25);
        this.craneBase.position.set(0,600);
        this.craneArm = new PIXI.Sprite(data.textures.port_sidemenu_15);
        this.craneArm.position.set(0,600);
        // 編成按钮
        this.hensei = new Button({
            default: data.textures.port_sidemenu_5,
            hover: data.textures.port_sidemenu_6,
        });
        this.hensei.button.position.set(0,195);
        // 補給按钮
        this.hokyuu = new Button({
            default: data.textures.port_sidemenu_13,
            hover: data.textures.port_sidemenu_14,
        });
        this.hokyuu.button.position.set(0,278);
        // 改装按钮
        this.kaisou = new Button({
            default: data.textures.port_sidemenu_9,
            hover: data.textures.port_sidemenu_10,
        });
        this.kaisou.button.position.set(0,360);
        // 入渠按钮
        this.nyuukyo = new Button({
            default: data.textures.port_sidemenu_11,
            hover: data.textures.port_sidemenu_12,
        });
        this.nyuukyo.button.position.set(0,440);
        // 工廠按钮
        this.koujyou = new Button({
            default: data.textures.port_sidemenu_3,
            hover: data.textures.port_sidemenu_4,
        });
        this.koujyou.button.position.set(0,518);
        // 母港按钮
        this.port = new Button({
            default: data.textures.port_sidemenu_7,
            hover: data.textures.port_sidemenu_8,
        });
        this.port.button.position.set(74,330);

        // 添加至容器
        this.container.addChild(
            this.bg1,
            this.bg2,
            this.craneBase,
            this.craneArm,
            this.hensei.button,
            this.hokyuu.button,
            this.kaisou.button,
            this.nyuukyo.button,
            this.koujyou.button,
            this.port.button,
        );
        this.hideAll();
    }

    hideAll = () => {
        this.bg1.visible = false;
        this.bg2.visible = false;
        this.craneBase.visible = false;
        this.craneArm.visible = false;
        this.hensei.hideAll();
        this.hokyuu.hideAll();
        this.kaisou.hideAll();
        this.nyuukyo.hideAll();
        this.koujyou.hideAll();
        this.port.hideAll();
    }

    showAll = () => {
        this.bg1.visible = true;
        this.bg2.visible = true;
        this.craneBase.visible = true;
        this.craneArm.visible = true;
        this.hensei.showAll();
        this.hokyuu.showAll();
        this.kaisou.showAll();
        this.nyuukyo.showAll();
        this.koujyou.showAll();
        this.port.showAll();
    }
}