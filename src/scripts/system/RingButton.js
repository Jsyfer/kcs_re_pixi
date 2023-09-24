import * as PIXI from "pixi.js";

export class RingButton{
    constructor(config) {
        // 按钮默认图案
        this.default = new PIXI.Sprite(config.default);
        // 按钮聚焦图案(齿轮部分)
        this.hoverGear = new PIXI.Sprite(config.hoverGear);
        // 按钮聚焦图案(文字部分)
        this.hoverText = new PIXI.Sprite(config.hoverText);
        // 按钮聚焦图案(Tip部分)
        this.hoverTip = new PIXI.Sprite(config.hoverTip);
        // 按钮聚焦图案(特效部分)
        this.hoverEffect = new PIXI.Sprite(config.hoverEffect);

        // 设定光标覆盖时的事件
        this.eventHover = config.eventHover;
        // 设定光标离开时的事件
        this.eventLeave = config.eventLeave;
        // 设定按钮按下时的事件
        this.eventDown = config.eventDown;
        // 设定按钮松开时的事件
        this.eventUp = config.eventUp;

        // 创建Container对象
        this.button = new PIXI.Container();

        this.button.addChild(this.default);
        this.button.addChild(this.hoverGear);
        this.button.addChild(this.hoverText);
        this.button.addChild(this.hoverTip);
        this.button.addChild(this.hoverEffect);

        this.button.position.set(0,0);
        this.hoverGear.position.set(1,1);
        this.hoverText.position.set(1,1);
        this.hoverTip.position.set(36,-22);
        this.hoverEffect.position.set(1,0);


        this.default.pivot.set(Math.round(this.default.width/2),Math.round(this.default.height/2));
        this.hoverGear.pivot.set(Math.round(this.hoverGear.width/2),Math.round(this.hoverGear.height/2));
        this.hoverText.pivot.set(Math.round(this.hoverText.width/2),Math.round(this.hoverText.height/2));
        this.hoverEffect.pivot.set(Math.round(this.hoverEffect.width/2),Math.round(this.hoverEffect.height/2));

        this.hoverGear.visible = false;
        this.hoverText.visible = false;
        this.hoverTip.visible = false;
        this.hoverEffect.visible = false;


        // this.button.addChild(this.hoverTip);
        // this.button.addChild(this.hoverEffect);
        // 设定事件模式
        this.default.eventMode = 'static';
        // 设置事件光标
        this.default.cursor = 'pointer';
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

    // 禁用按钮
    disable() {

        this.button.eventMode = 'none';
    }

    // 启用按钮
    enable() {

        this.button.eventMode = 'static';
    }

    // 鼠标按下事件
    mouseDown() {
        this.button.on('pointerdown', ()=>{

            if (this.eventDown) this.eventDown();
        });
    }
    // 鼠标松开事件
    mouseUp() {
        this.button.on('pointerup', ()=>{

            if (this.eventUp) this.eventUp();
        });
    }
    // 鼠标覆盖事件
    mouseHover() {
        this.default.on('pointerover',() => {

            this.hoverGear.visible = true;
            this.hoverText.visible = true;
            this.hoverTip.visible = true;
            this.hoverEffect.visible = true;

            if (this.eventHover) this.eventHover();
        });
    }
    // 鼠标离开事件
    mouseLeave() {
        this.default.on('pointerleave',() => {
            // this.button.removeChildren();
            // this.button.addChild(this.default);

            this.hoverGear.visible = false;
            this.hoverText.visible = false;
            this.hoverTip.visible = false;
            this.hoverEffect.visible = false;
            if (this.eventLeave) this.eventLeave();
        });
    }

}