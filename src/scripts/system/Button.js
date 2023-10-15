import * as PIXI from "pixi.js";

export class Button {
    constructor(config) {
        // 按钮默认图案
        this.default = config.default;
        // 按钮禁用图案
        this.disabled = config.disabled ? config.disabled : this.default;
        // 按钮聚焦图案
        this.hover = config.hover ? config.hover : this.default;
        // 按钮按下图案
        this.down = config.down ? config.down : this.hover;
        // 设定光标覆盖时的事件
        this.eventHover = config.eventHover;
        // 设定光标离开时的事件
        this.eventLeave = config.eventLeave;
        // 设定按钮按下时的事件
        this.eventDown = config.eventDown;
        // 设定按钮松开时的事件
        this.eventUp = config.eventUp;
        // 创建Sprite对象
        this.button = new PIXI.Sprite(this.default);
        // 设定事件模式
        this.button.eventMode = 'static';
        // 设置事件光标
        this.button.cursor = 'pointer';
        // 初始化
        this.init()
    }

    init() {
        // 添加各类按钮事件
        this.mouseHover();
        this.mouseLeave();
        this.mouseDown();
        this.mouseUp();
    }

    hideAll = () => {
        this.button.visible = false;
    }

    showAll = () => {
        this.button.visible = true;
    }

    // 禁用按钮
    disable() {
        this.button.texture = this.disabled;
        this.button.eventMode = 'none';
    }

    // 启用按钮
    enable() {
        this.button.texture = this.default;
        this.button.eventMode = 'static';
    }

    // 鼠标按下事件
    mouseDown() {
        this.button.on('pointerdown', ()=>{
            this.button.texture = this.down;
            if (this.eventDown) this.eventDown();
        });
    }
    // 鼠标松开事件
    mouseUp() {
        this.button.on('pointerup', ()=>{
            this.button.texture = this.hover;
            if (this.eventUp) this.eventUp();
        });
    }
    // 鼠标覆盖事件
    mouseHover() {
        this.button.on('pointerover',() => {
            this.button.texture = this.hover;
            if (this.eventHover) this.eventHover();
        });
    }
    // 鼠标离开事件
    mouseLeave() {
        this.button.on('pointerleave',() => {
            this.button.texture = this.default;
            if (this.eventLeave) this.eventLeave();
        });
    }

}