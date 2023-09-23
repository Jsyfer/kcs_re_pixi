import * as PIXI from "pixi.js";

export class Button {
    constructor(config) {
        this.default = config.default;
        // use default button texture if not provide
        this.disabled = config.disabled ? config.disabled : this.default;
        this.down = config.down ? config.down : this.default;
        this.hover = config.hover ? config.hover : this.default;
        this.button = new PIXI.Sprite(this.default);
        // set interactive
        this.button.eventMode = 'static';
        // change cursor
        this.button.cursor = 'pointer';
        this.init()
    }

    init() {
        this.mouseHover();
        this.mouseLeave();
        this.mouseDown();
        this.mouseUp();
    }

    disable() {}

    mouseDown() {
        this.button.on('pointerdown', ()=>{
            this.button.texture = this.down;
        });
    }

    mouseUp() {
        this.button.on('pointerup', ()=>{
            this.button.texture = this.hover;
        });
    }
    
    mouseHover() {
        this.button.on('pointerover',() => {
            this.button.texture = this.hover;
        });
    }

    mouseLeave() {
        this.button.on('pointerleave',() => {
            this.button.texture = this.default;
        });
    }

}