import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import title_main from './../../assets/kcs2/img/title/title_main.json'
import title_main_img from './../../assets/kcs2/img/title/title_main.png'

// 开始界面
export class Start extends Scene {
    create() {
        // 打开容器内的对象排序
        this.container.sortableChildren = true
        // 添加背景
        PIXI.Assets.load('./img/title/title2.png').then(value => {
            const bg = new PIXI.Sprite(value);
            bg.zIndex = -1;
            this.container.addChild(bg);
        });

        // Create the SpriteSheet from data and image
        const spritesheet = new PIXI.Spritesheet(
            PIXI.BaseTexture.from(title_main_img),
            title_main
        );
        
        // Generate all the Textures asynchronously
        spritesheet.parse();
        const logo = new PIXI.Sprite(spritesheet.textures.title_main_3);
        logo.position.set(775,110);
        const btn_default = new PIXI.Sprite(spritesheet.textures.title_main_4);
        btn_default.position.set(650,550);
        this.container.addChild(logo,btn_default);
    }
}
