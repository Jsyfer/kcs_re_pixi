import * as PIXI from "pixi.js";
import { App } from "../App";

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
        this.ringEffect1 = new PIXI.Sprite(config.ringEffect);
        this.ringEffect2 = new PIXI.Sprite(config.ringEffect);

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
        this.button.addChild(this.ringEffect1);
        this.button.addChild(this.ringEffect2);

        this.button.position.set(0,0);
        this.hoverGear.position.set(0,0);
        this.hoverText.position.set(1,1);
        this.hoverTip.position.set(36,-22);
        this.ringEffect1.position.set(1,0);
        this.ringEffect2.position.set(1,0);

        this.default.pivot.set(Math.round(this.default.width/2),Math.round(this.default.height/2));
        this.hoverGear.pivot.set(Math.round(this.hoverGear.width/2),Math.round(this.hoverGear.height/2));
        this.hoverText.pivot.set(Math.round(this.hoverText.width/2),Math.round(this.hoverText.height/2));
        this.ringEffect1.pivot.set(Math.round(this.ringEffect1.width/2),Math.round(this.ringEffect1.height/2));
        this.ringEffect2.pivot.set(Math.round(this.ringEffect2.width/2),Math.round(this.ringEffect2.height/2));

        this.hoverGear.visible = false;
        this.hoverText.visible = false;
        this.hoverTip.visible = false;
        this.ringEffect1.visible = false;
        this.ringEffect2.visible = false;

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
            this.ringEffect1.visible = true;
            this.ringEffect2.visible = true;
            this.default.alpha = 0;
            // 添加齿轮旋转动画
            App.app.ticker.add(this.rotateSprite);
            // 添加椭圆放大动画
            this.ringEffect1.scale.set(0,0);
            this.ringEffect2.scale.set(0,0);
            this.addSecondRingEffect = false;
            App.app.ticker.add(this.spreadCircle)

            if (this.eventHover) this.eventHover();
        });
    }
    // 鼠标离开事件
    mouseLeave() {
        this.default.on('pointerleave',() => {
            this.default.alpha = 1;
            this.hoverGear.visible = false;
            this.hoverText.visible = false;
            this.hoverTip.visible = false;
            this.ringEffect1.visible = false;
            this.ringEffect2.visible = false;
            // 移除齿轮旋转动画
            App.app.ticker.remove(this.rotateSprite);
            // 移除椭圆放大动画
            this.ringEffect1.scale.set(0,0);
            this.ringEffect2.scale.set(0,0);
            App.app.ticker.remove(this.spreadCircle)

            if (this.eventLeave) this.eventLeave();
        });
    }
    
    // 旋转动画
    rotateSprite = () =>{
        this.hoverGear.rotation += 0.01;
    }

    updateRingEffect = (ringEffect) => {
        if(ringEffect.scale.x < 1.2){
            ringEffect.scale.x += 0.01;
            ringEffect.scale.y += 0.01;
            if(ringEffect.scale.x > 0.8) {
                ringEffect.alpha -= 0.1
            }
        } else {
            ringEffect.scale.set(0,0);
            ringEffect.alpha = 1
        }
        return ringEffect.scale.x;
    }

    // 椭圆放大效果
    spreadCircle = () =>{
        this.updateRingEffect(this.ringEffect1);
        if (this.ringEffect1.scale.x > 0.5) {
            this.addSecondRingEffect = true;
        }
        if (this.addSecondRingEffect) {
            this.updateRingEffect(this.ringEffect2);
        }
    }



}