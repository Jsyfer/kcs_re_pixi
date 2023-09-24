import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import { RingButton } from "../system/RingButton";

// 母港界面
export class Port extends Scene {
    create() {
        // 打开容器内的对象排序
        this.container.sortableChildren = true
        // 添加背景
        const port_ground = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/494_1648.png');
        const port_wall = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/502_8118.png');
        const port_outside = PIXI.Sprite.from('assets/kcs2/resources/furniture/outside/window_bg_4-2.png');
        const port_window = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/491_9688.png');
        const port_on_wall = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/499_8458.png');
        const port_center = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/493_4897.png');
        const port_corner = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/498_8534.png');
        // 添加舰娘
        const port_ship = PIXI.Sprite.from('assets/kcs2/resources/ship/full/0538_2823_sullpopastgr.png');
        
        port_ground.position.y = 412.5;
        port_outside.position.x = 300;
        port_window.position.x = 300;
        port_center.position.y = 200;
        port_corner.position.x = 870;
        port_ship.position.set(400, 100);
        this.container.addChild(port_ground,port_wall,port_outside,port_window,port_on_wall,port_center,port_corner,port_ship);

        // TODO 添加母港按钮
        PIXI.Assets.load("assets/kcs2/img/port/port_ringmenu.json").then((data) => {
            // 改装按钮
            this.kaisouBtn = new RingButton({
                default: data.textures.port_ringmenu_17,
                hoverGear: data.textures.port_ringmenu_7,
                hoverText: data.textures.port_ringmenu_18,
                hoverTip: data.textures.port_ringmenu_10,
                hoverEffect: data.textures.port_ringmenu_31,
            });
            this.kaisouBtn.button.position.set(447,335);
            // 工廠按钮
            this.koujyouBtn = new RingButton({
                default: data.textures.port_ringmenu_5,
                hoverGear: data.textures.port_ringmenu_7,
                hoverText: data.textures.port_ringmenu_6,
                hoverTip: data.textures.port_ringmenu_8,
                hoverEffect: data.textures.port_ringmenu_31,
            });
            this.koujyouBtn.button.position.set(406,543);
            // 入渠按钮
            this.nyukyoBtn = new RingButton({
                default: data.textures.port_ringmenu_19,
                hoverGear: data.textures.port_ringmenu_7,
                hoverText: data.textures.port_ringmenu_20,
                hoverTip: data.textures.port_ringmenu_11,
                hoverEffect: data.textures.port_ringmenu_31,
            });
            this.nyukyoBtn.button.position.set(186,543);
            // 補給按钮
            this.hokyuBtn = new RingButton({
                default: data.textures.port_ringmenu_29,
                hoverGear: data.textures.port_ringmenu_7,
                hoverText: data.textures.port_ringmenu_30,
                hoverTip: data.textures.port_ringmenu_14,
                hoverEffect: data.textures.port_ringmenu_31,
            });
            this.hokyuBtn.button.position.set(118,335);
            // 編成按钮
            this.henseiBtn = new RingButton({
                default: data.textures.port_ringmenu_15,
                hoverGear: data.textures.port_ringmenu_7,
                hoverText: data.textures.port_ringmenu_16,
                hoverTip: data.textures.port_ringmenu_9,
                hoverEffect: data.textures.port_ringmenu_31,
            });
            this.henseiBtn.button.position.set(296,202);
            // 添加 logo和按钮至容器
            this.container.addChild(this.kaisouBtn.button,this.koujyouBtn.button,this.nyukyoBtn.button,this.hokyuBtn.button,this.henseiBtn.button);
        })
    }

}
