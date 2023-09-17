import * as PIXI from "pixi.js";
import { Scene } from "../system/Scene";
import title_main from './../../assets/kcs2/img/title/title_main.json'
import title_main_img from './../../assets/kcs2/img/title/title_main.png'

export class Start extends Scene {
    create() {
        // Create the SpriteSheet from data and image
        const spritesheet = new PIXI.Spritesheet(
            PIXI.BaseTexture.from(title_main_img),
            title_main
        );
        
        // Generate all the Textures asynchronously
        spritesheet.parse();
        this.container.addChild(new PIXI.Sprite(spritesheet.textures.title_main_0));

        PIXI.Assets.load('./img/port/port_main.png').then(
            value => this.container.addChild(new PIXI.Sprite(value))
        );

        // this.container.addChild();
    }
}
