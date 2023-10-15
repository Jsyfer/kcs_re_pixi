import * as PIXI from "pixi.js";
import { App } from "../App";

export class RingButton{
    constructor(config) {
        switch (config.type) {
            case "kaisou":
                // 按钮默认图案
                this.default = new PIXI.Sprite(config.textures.port_ringmenu_17);
                // 按钮聚焦图案(文字部分)
                this.hoverText = new PIXI.Sprite(config.textures.port_ringmenu_18);
                // 按钮聚焦图案(Tip部分)
                this.tooltips = new PIXI.Sprite(config.textures.port_ringmenu_10);
                break;
            case "koujyou":
                // 按钮默认图案
                this.default = new PIXI.Sprite(config.textures.port_ringmenu_5);
                // 按钮聚焦图案(文字部分)
                this.hoverText = new PIXI.Sprite(config.textures.port_ringmenu_6);
                // 按钮聚焦图案(Tip部分)
                this.tooltips = new PIXI.Sprite(config.textures.port_ringmenu_8);
                break;
            case "nyuukyo":
                // 按钮默认图案
                this.default = new PIXI.Sprite(config.textures.port_ringmenu_19);
                // 按钮聚焦图案(文字部分)
                this.hoverText = new PIXI.Sprite(config.textures.port_ringmenu_20);
                // 按钮聚焦图案(Tip部分)
                this.tooltips = new PIXI.Sprite(config.textures.port_ringmenu_11);
                break;
            case "hokyuu":
                // 按钮默认图案
                this.default = new PIXI.Sprite(config.textures.port_ringmenu_29);
                // 按钮聚焦图案(文字部分)
                this.hoverText = new PIXI.Sprite(config.textures.port_ringmenu_30);
                // 按钮聚焦图案(Tip部分)
                this.tooltips = new PIXI.Sprite(config.textures.port_ringmenu_14);
                break;
            case "hensei":
                // 按钮默认图案
                this.default = new PIXI.Sprite(config.textures.port_ringmenu_15);
                // 按钮聚焦图案(文字部分)
                this.hoverText = new PIXI.Sprite(config.textures.port_ringmenu_16);
                // 按钮聚焦图案(Tip部分)
                this.tooltips = new PIXI.Sprite(config.textures.port_ringmenu_9);
                break;
        }
         
        // 按钮聚焦图案(齿轮部分)
        this.hoverGear = new PIXI.Sprite(config.textures.port_ringmenu_7);
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

        // 初始化
        this.init()

    }

    init() {
        this.button.addChild(this.default);
        this.button.addChild(this.hoverGear);
        this.button.addChild(this.hoverText);
        this.button.addChild(this.tooltips);
        this.button.addChild(this.ringEffect1);
        this.button.addChild(this.ringEffect2);

        this.button.position.set(0,0);
        this.hoverGear.position.set(0,0);
        this.hoverText.position.set(1,1);
        this.tooltips.position.set(0,-22);
        this.ringEffect1.position.set(1,0);
        this.ringEffect2.position.set(1,0);

        this.centerPivot(this.default);
        this.centerPivot(this.hoverGear);
        this.centerPivot(this.hoverText);
        this.centerPivot(this.ringEffect1);
        this.centerPivot(this.ringEffect2);

        this.hideHoverSprite();
        // 设定事件模式
        this.default.eventMode = 'static';
        // 设置事件光标
        this.default.cursor = 'pointer';
        // 添加各类按钮事件
        this.mouseHover();
        this.mouseLeave();
        this.mouseDown();
        this.mouseUp();
    }

    hideAll = () => {
        this.default.visible = false;
    }

    showAll = () => {
        this.default.visible = true;
    }

    // 隐藏hover sprite
    hideHoverSprite = () => {
        this.hoverGear.visible = false;
        this.hoverText.visible = false;
        this.tooltips.visible = false;
        this.ringEffect1.visible = false;
        this.ringEffect2.visible = false;
    }

    // 显示hover sprite
    showHoverSprite = () => {
        this.hoverGear.visible = true;
        this.hoverText.visible = true;
        this.tooltips.visible = true;
        this.ringEffect1.visible = true;
        this.ringEffect2.visible = true;
        this.ringEffect1.alpha = 1
        this.ringEffect2.alpha = 1
    }

    // 设置图形坐标为中心点
    centerPivot = (sprite) => {
        sprite.pivot.set(Math.round(sprite.width/2),Math.round(sprite.height/2));
    }

    // 鼠标按下事件
    mouseDown() {
        this.default.on('pointerdown', ()=>{
            if (this.eventDown) this.eventDown();
        });
    }
    // 鼠标松开事件
    mouseUp() {
        this.default.on('pointerup', ()=>{
            if (this.eventUp) this.eventUp();
        });
    }
    // 鼠标覆盖事件
    mouseHover() {
        this.default.on('pointerover',() => {
            this.default.alpha = 0;
            this.showHoverSprite();
            // 添加齿轮旋转动画
            App.app.ticker.add(this.rotateSprite);
            // 添加椭圆放大动画
            this.ringEffect1.scale.set(0,0);
            this.ringEffect2.scale.set(0,0);
            this.addSecondRingEffect = false;
            App.app.ticker.add(this.spreadCircle);
            // 添加tooltips效果
            this.tooltips.position.x = 0;
            this.tooltips.alpha = 0;
            App.app.ticker.add(this.tooltipEffect);
            if (this.eventHover) this.eventHover();
        });
    }
    // 鼠标离开事件
    mouseLeave() {
        this.default.on('pointerleave',() => {
            this.default.alpha = 1;
            this.hideHoverSprite();
            // 移除齿轮旋转动画
            App.app.ticker.remove(this.rotateSprite);
            // 移除椭圆放大动画
            App.app.ticker.remove(this.spreadCircle);
            // 移除tooltips效果
            App.app.ticker.remove(this.tooltipEffect);
            if (this.eventLeave) this.eventLeave();
        });
    }
    
    // 旋转动画
    rotateSprite = () =>{
        this.hoverGear.rotation += 0.005;
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

    // set tooltips effect
    tooltipEffect = () => {
        if (this.tooltips.position.x < 35) {
            this.tooltips.position.x += 3;
            this.tooltips.alpha += 0.2;
        }
    }


}