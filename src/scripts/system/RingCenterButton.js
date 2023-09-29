import * as PIXI from "pixi.js";
import { App } from "../App";

export class RingCenterButton{
    constructor(config) {
        // =========新建按钮图案=========
        // 按钮默认波浪（右）
        this.defaultWaveR = new PIXI.Sprite(config.textures.port_ringmenu_3);
        // 按钮默认波浪（左）
        this.defaultWaveL = new PIXI.Sprite(config.textures.port_ringmenu_4);
        // 按钮默认齿轮
        this.defaultGear = new PIXI.Sprite(config.textures.port_ringmenu_0);
        // 按钮默认舰船
        this.defaultShip = new PIXI.Sprite(config.textures.port_ringmenu_2);
        // 按钮默认文字
        this.defaultText = new PIXI.Sprite(config.textures.port_ringmenu_1);

        // 按钮聚焦齿轮
        this.hoverGear = new PIXI.Sprite(config.textures.port_ringmenu_24);
        // 按钮聚焦波浪（右）
        this.hoverWaveR = new PIXI.Sprite(config.textures.port_ringmenu_26);
        // 按钮聚焦波浪（左）
        this.hoverWaveL = new PIXI.Sprite(config.textures.port_ringmenu_25);
        // 按钮聚焦齿轮上层青色背景
        this.hoverBlueCircle = new PIXI.Sprite(config.textures.port_ringmenu_23);
        // 按钮聚焦舰船
        this.hoverShip = new PIXI.Sprite(config.textures.port_ringmenu_27);
        // 按钮聚焦文字
        this.hoverText = new PIXI.Sprite(config.textures.port_ringmenu_28);

        // 按钮聚焦图案(特效部分)
        this.ringEffect1 = new PIXI.Sprite(config.textures.port_ringmenu_31);
        this.ringEffect2 = new PIXI.Sprite(config.textures.port_ringmenu_31);
        // 按钮聚焦图案(Tip部分)
        this.tooltips = new PIXI.Sprite(config.textures.port_ringmenu_13);

        // 创建Container对象
        this.button = new PIXI.Container();
        // 添加图案至容器
        this.button.addChild(this.defaultWaveR);
        this.button.addChild(this.defaultWaveL);
        this.button.addChild(this.defaultGear);
        this.button.addChild(this.defaultShip);
        this.button.addChild(this.defaultText);

        this.button.addChild(this.hoverGear);
        this.button.addChild(this.hoverWaveR);
        this.button.addChild(this.hoverWaveL);
        this.button.addChild(this.hoverBlueCircle);
        this.button.addChild(this.hoverShip);
        this.button.addChild(this.hoverText);

        this.button.addChild(this.ringEffect1);
        this.button.addChild(this.ringEffect2);
        this.button.addChild(this.tooltips);

        // this.button.position.set(0,0);
        // this.hoverGear.position.set(0,0);
        // this.hoverText.position.set(1,1);
        this.tooltips.position.set(0,-30);
        // this.ringEffect1.position.set(1,0);
        // this.ringEffect2.position.set(1,0);

        this.centerPivot(this.defaultWaveR)
        this.centerPivot(this.defaultWaveL)
        this.centerPivot(this.defaultGear)
        this.centerPivot(this.defaultShip)
        this.centerPivot(this.defaultText)

        this.centerPivot(this.hoverGear)
        this.centerPivot(this.hoverWaveR)
        this.centerPivot(this.hoverWaveL)
        this.centerPivot(this.hoverBlueCircle)
        this.centerPivot(this.hoverShip)
        this.centerPivot(this.hoverText)

        this.centerPivot(this.ringEffect1)
        this.centerPivot(this.ringEffect2)
        // hide hover target
        this.hoverGear.visible = false;
        this.hoverWaveR.visible = false;
        this.hoverWaveL.visible = false;
        this.hoverBlueCircle.visible = false;
        this.hoverShip.visible = false;
        this.hoverText.visible = false;

        this.tooltips.visible = false;
        this.ringEffect1.visible = false;
        this.ringEffect2.visible = false;

        // 设定事件模式
        this.defaultGear.eventMode = 'static';
        // 设置事件光标
        this.defaultGear.cursor = 'pointer';

        // =========设置事件=========
        // 设定光标覆盖时的事件
        this.eventHover = config.eventHover;
        // 设定光标离开时的事件
        this.eventLeave = config.eventLeave;
        // 设定按钮按下时的事件
        this.eventDown = config.eventDown;
        // 设定按钮松开时的事件
        this.eventUp = config.eventUp;

        // =========初始化==========
        this.init()

    }

    init() {
        // 添加各类按钮事件
        this.mouseHover();
        this.mouseLeave();
        this.mouseDown();
        this.mouseUp();
    }
    // 设置图形坐标为中心点
    centerPivot = (sprite) => {
        sprite.pivot.set(Math.round(sprite.width/2),Math.round(sprite.height/2));
    }

    // 鼠标按下事件
    mouseDown() {
        this.defaultGear.on('pointerdown', ()=>{
            if (this.eventDown) this.eventDown();
        });
    }
    // 鼠标松开事件
    mouseUp() {
        this.defaultGear.on('pointerup', ()=>{
            if (this.eventUp) this.eventUp();
        });
    }
    // 鼠标覆盖事件
    mouseHover() {
        this.defaultGear.on('pointerover',() => {
            this.defaultGear.alpha = 0;

            this.hoverGear.visible = true;
            this.hoverWaveR.visible = true;
            this.hoverWaveL.visible = true;
            this.hoverBlueCircle.visible = true;
            this.hoverShip.visible = true;
            this.hoverText.visible = true;
            // 添加齿轮旋转动画
            App.app.ticker.add(this.rotateSprite);
            // 添加椭圆放大动画
            this.ringEffect1.scale.set(0,0);
            this.ringEffect2.scale.set(0,0);
            this.ringEffect1.alpha = 1
            this.ringEffect2.alpha = 1
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
        this.defaultGear.on('pointerleave',() => {
            this.defaultGear.alpha = 1;
            this.hoverGear.visible = false;
            this.hoverWaveR.visible = false;
            this.hoverWaveL.visible = false;
            this.hoverBlueCircle.visible = false;
            this.hoverShip.visible = false;
            this.hoverText.visible = false;

            this.tooltips.visible = false;
            this.ringEffect1.visible = false;
            this.ringEffect2.visible = false;
            // 移除齿轮旋转动画
            App.app.ticker.remove(this.rotateSprite);
            // 移除椭圆放大动画
            this.ringEffect1.scale.set(0,0);
            this.ringEffect2.scale.set(0,0);
            App.app.ticker.remove(this.spreadCircle);
            // 移除tooltips效果
            App.app.ticker.remove(this.tooltipEffect);
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

    // tooltips渐入效果
    tooltipEffect = () => {
        if (this.tooltips.position.x < 35) {
            this.tooltips.position.x += 3;
            this.tooltips.alpha += 0.2;
        }
    }


}