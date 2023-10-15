import * as PIXI from "pixi.js";

export class PortBackground{
    constructor() {
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        this.create();
    }

    create = async () => {
        // 添加背景
        this.ground = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/494_1648.png');
        this.wall = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/502_8118.png');
        this.outside = PIXI.Sprite.from('assets/kcs2/resources/furniture/outside/window_bg_4-2.png');
        this.window = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/491_9688.png');
        this.on_wall = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/499_8458.png');
        this.center = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/493_4897.png');
        this.corner = PIXI.Sprite.from('assets/kcs2/resources/furniture/normal/498_8534.png');
        // 添加舰娘
        this.ship = PIXI.Sprite.from('assets/kcs2/resources/ship/full/0538_2823_sullpopastgr.png');
        
        this.ground.position.y = 412.5;
        this.outside.position.x = 300;
        this.window.position.x = 300;
        this.center.position.y = 200;
        this.corner.position.x = 870;
        this.ship.position.set(400, 100);
        this.container.addChild(
            this.ground,
            this.wall,
            this.outside,
            this.window,
            this.on_wall,
            this.center,
            this.corner,
            this.ship,
        );
    }

}