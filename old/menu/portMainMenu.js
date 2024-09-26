import * as PIXI from "pixi.js";
import { RingButton } from "../system/RingButton";
import { RingCenterButton } from "../system/RingCenterButton";
import { App, BASE_URL } from "../App";

export class PortMainMenu {
    constructor() {
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        this.create();
    }

    create = async () => {
        const data = await PIXI.Assets.load(BASE_URL + "assets/kcs2/img/port/port_ringmenu.json")
        // 改装按钮
        this.kaisou = new RingButton({
            type: "kaisou",
            textures: data.textures,
            eventUp: this.kaisouEvent,
        });
        this.kaisou.button.position.set(477, 335);
        // 工廠按钮
        this.koujyou = new RingButton({
            type: "koujyou",
            textures: data.textures,
            eventUp: this.koujyouEvent,
        });
        this.koujyou.button.position.set(406, 543);
        // 出撃按钮
        this.syutsugeki = new RingCenterButton({
            textures: data.textures,
        });
        this.syutsugeki.button.position.set(294, 390);
        // 入渠按钮
        this.nyuukyo = new RingButton({
            type: "nyuukyo",
            textures: data.textures,
            eventUp: this.nyuukyoEvent,
        });
        this.nyuukyo.button.position.set(186, 543);
        // 補給按钮
        this.hokyuu = new RingButton({
            type: "hokyuu",
            textures: data.textures,
            eventUp: this.hokyuuEvent,
        });
        this.hokyuu.button.position.set(118, 335);
        // 編成按钮
        this.hensei = new RingButton({
            type: "hensei",
            textures: data.textures,
            eventUp: this.henseiEvent,
        });
        this.hensei.button.position.set(296, 202);
        // 添加 logo和按钮至容器
        this.container.addChild(
            this.kaisou.button,
            this.koujyou.button,
            this.nyuukyo.button,
            this.syutsugeki.button,
            this.hokyuu.button,
            this.hensei.button
        );
    }
    // 编成按钮事件
    henseiEvent = () => {
        this.hideAll();
        App.port.portSideMenu.showAll();
        App.port.portSideMenu.henseiEvent();
    }
    // 補給按钮事件
    hokyuuEvent = () => {
        this.hideAll();
        App.port.portSideMenu.showAll();
        App.port.portSideMenu.hokyuuEvent();
    }
    // 改装按钮事件
    kaisouEvent = () => {
        this.hideAll();
        App.port.portSideMenu.showAll();
        App.port.portSideMenu.kaisouEvent();
    }
    // 入渠按钮事件
    nyuukyoEvent = () => {
        this.hideAll();
        App.port.portSideMenu.showAll();
        App.port.portSideMenu.nyuukyoEvent();
    }
    // 工廠按钮事件
    koujyouEvent = () => {
        this.hideAll();
        App.port.portSideMenu.showAll();
        App.port.portSideMenu.koujyouEvent();
    }

    hideAll = () => {
        this.kaisou.hideAll();
        this.koujyou.hideAll();
        this.nyuukyo.hideAll();
        this.syutsugeki.hideAll();
        this.hokyuu.hideAll();
        this.hensei.hideAll();
    }

    showAll = () => {
        this.kaisou.showAll();
        this.koujyou.showAll();
        this.nyuukyo.showAll();
        this.syutsugeki.showAll();
        this.hokyuu.showAll();
        this.hensei.showAll();
    }


}