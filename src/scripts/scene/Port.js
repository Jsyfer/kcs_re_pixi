import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import { PortMainMenu } from "../menu/portMainMenu";
import { PortTopMenu } from "../menu/portTopMenu";
import { PortSideMenu } from "../menu/portSideMenu";

// 母港界面
export class Port extends Scene {
    async create() {
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

        this.portMainMenu = new PortMainMenu();

        // 添加母港顶部菜单
        this.portTopMenu = new PortTopMenu();
        // this.portMainMenu = new PortMainMenu({
        //     henseiAction: this.switchToHensei,
        // });

        // 添加母港侧边菜单
        this.portSideMenu = new PortSideMenu();

        
        this.container.addChild(
            this.portMainMenu.container,
            this.portTopMenu.container,
            this.portSideMenu.container,
        );

    }

    switchToHensei = () => {
        console.log('switch');
    }


}
