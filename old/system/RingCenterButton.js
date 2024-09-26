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

    // 初始化
    init() {
        // 创建Container对象，并添加对象
        this.button = new PIXI.Container();
        this.addToContainer();
        // 设置图形中心点
        this.centerSpritePivot();
        // 放置图形
        this.setSpritePosition();
        // 隐藏hover图形
        this.hideHoverSprite();
        // 设定事件模式
        this.defaultGear.eventMode = 'static';
        // 设置事件光标
        this.defaultGear.cursor = 'pointer';
        // 添加各类按钮事件
        this.mouseHover();
        this.mouseLeave();
        this.mouseDown();
        this.mouseUp();
    }

    // 添加图案至容器
    addToContainer = () => {
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
    }
    
    // 批量设置Sprite中心点
    centerSpritePivot = () => {
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
    }

    // 放置图形
    setSpritePosition = () => {
        this.defaultShip.position.set(0,-40);
        this.defaultText.position.set(0,40);
        this.defaultWaveL.position.set(-37,44);
        this.defaultWaveR.position.set(37,44);
        this.hoverShip.position.set(0,-40);
        this.hoverText.position.set(0,40);
        this.hoverWaveL.position.set(-37,44);
        this.hoverWaveR.position.set(37,44);
        this.tooltips.position.set(0,-30);
    }

    hideAll = () => {
        this.hideDefaultrSprite();
        this.defaultGear.visible = false;
        this.hideHoverSprite();
    }

    showAll = () => {
        this.showDefaultrSprite();
        this.defaultGear.visible = true;
    }

    // 隐藏默认sprite
    hideDefaultrSprite = () => {
        this.defaultWaveR.visible = false;
        this.defaultWaveL.visible = false;
        this.defaultShip.visible = false;
        this.defaultText.visible = false;
    }

    // 显示默认sprite
    showDefaultrSprite = () => {
        this.defaultWaveR.visible = true;
        this.defaultWaveL.visible = true;
        this.defaultShip.visible = true;
        this.defaultText.visible = true;
    }

    // 隐藏hover sprite
    hideHoverSprite = () => {
        this.hoverGear.visible = false;
        this.hoverWaveR.visible = false;
        this.hoverWaveL.visible = false;
        this.hoverBlueCircle.visible = false;
        this.hoverShip.visible = false;
        this.hoverText.visible = false;
        this.tooltips.visible = false;
        this.ringEffect1.visible = false;
        this.ringEffect2.visible = false;
    }
    
    // 显示hover sprite
    showHoverSprite = () => {
        this.hoverGear.visible = true;
        this.hoverWaveR.visible = true;
        this.hoverWaveL.visible = true;
        this.hoverBlueCircle.visible = true;
        this.hoverShip.visible = true;
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
            // 设置对象显示隐藏
            this.hideDefaultrSprite();
            this.defaultGear.alpha = 0;
            this.showHoverSprite();
            // 添加齿轮旋转动画
            App.app.ticker.add(this.rotateGear);
            // 添加舰船旋转动画
            // 顺时针旋转flag
            this.clockwiseFlag = true;
            App.app.ticker.add(this.rotateShip);
            // 添加波浪动画
            this.hoverWaveL.angle = 0;
            this.hoverWaveR.angle = 0;
            this.hoverWaveL.position.set(-37,44);
            this.hoverWaveR.position.set(37,44);
            // 波浪阶段动画完成 flag
            this.waveLStep1Flag = false;
            this.waveLStep2Flag = false;
            this.waveRStep1Flag = false;
            this.waveRStep2Flag = false;
            App.app.ticker.add(this.waveEffect);
            // 添加椭圆放大动画
            this.ringEffect1.scale.set(0,0);
            this.ringEffect2.scale.set(0,0);
            this.addSecondRingEffect = false;
            App.app.ticker.add(this.spreadCircle);
            // 添加tooltips效果
            this.tooltips.position.x = 0;
            this.tooltips.alpha = 0;
            App.app.ticker.add(this.tooltipEffect);
            // 其它指定事件
            if (this.eventHover) this.eventHover();
        });
    }
    // 鼠标离开事件
    mouseLeave() {
        this.defaultGear.on('pointerleave',() => {
            // 设置对象显示隐藏
            this.showDefaultrSprite();
            this.defaultGear.alpha = 1;
            this.hideHoverSprite();
            // 移除齿轮旋转动画
            App.app.ticker.remove(this.rotateGear);
            // 移除舰船旋转动画
            App.app.ticker.remove(this.rotateShip);
            // 移除波浪动画
            App.app.ticker.remove(this.waveEffect);
            // 移除椭圆放大动画
            App.app.ticker.remove(this.spreadCircle);
            // 移除tooltips效果
            App.app.ticker.remove(this.tooltipEffect);
            // 其它指定事件
            if (this.eventLeave) this.eventLeave();
        });
    }
    
    // 齿轮旋转动画
    rotateGear = () =>{
        this.hoverGear.rotation += 0.005;
    }

    // 舰船旋转动画
    rotateShip = () =>{
        if (this.clockwiseFlag){
            if (this.hoverShip.angle < 3){
                this.hoverShip.angle += 0.05;
            } else {
                this.clockwiseFlag = false;
            }
        } else {
            if (this.hoverShip.angle > -3){
                this.hoverShip.angle -= 0.05;
            } else {
                this.clockwiseFlag = true;
            }
        }
    }

    // 波浪效果
    waveEffect = () => {
        // 左侧波浪动画
        if (!this.waveLStep1Flag && this.hoverWaveL.angle > -5) {
            this.hoverWaveL.angle -= 0.2;
        } else {
            this.waveLStep1Flag = true
            if (!this.waveLStep2Flag && this.hoverWaveL.position.x > -65) {
                this.hoverWaveL.position.x -= 0.3;
            } else {
                this.waveLStep2Flag = true
                if (this.hoverWaveL.angle < 0) {
                    this.hoverWaveL.angle += 0.2;
                } else {
                    if (this.hoverWaveL.position.x < -37) {
                        this.hoverWaveL.position.x += 0.3;
                    } else {
                        this.waveLStep1Flag = false;
                        this.waveLStep2Flag = false;
                    }
                }
            }
        }
        // 右侧波浪动画
        if (!this.waveRStep1Flag && this.hoverWaveR.angle < 5) {
            this.hoverWaveR.angle += 0.2;
        } else {
            this.waveRStep1Flag = true
            if (!this.waveRStep2Flag && this.hoverWaveR.position.x < 65) {
                this.hoverWaveR.position.x += 0.3;
            } else {
                this.waveRStep2Flag = true
                if (this.hoverWaveR.angle > 0) {
                    this.hoverWaveR.angle -= 0.2;
                } else {
                    if (this.hoverWaveR.position.x > 37) {
                        this.hoverWaveR.position.x -= 0.3;
                    } else {
                        this.waveRStep1Flag = false;
                        this.waveRStep2Flag = false;
                    }
                }
            }
        }
    }

    // 椭圆放大动画
    spreadCircle = () =>{
        this.updateRingEffect(this.ringEffect1);
        if (this.ringEffect1.scale.x > 0.5) {
            this.addSecondRingEffect = true;
        }
        if (this.addSecondRingEffect) {
            this.updateRingEffect(this.ringEffect2);
        }
    }

    // 椭圆效果
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

    // tooltips渐入效果
    tooltipEffect = () => {
        if (this.tooltips.position.x < 35) {
            this.tooltips.position.x += 3;
            this.tooltips.alpha += 0.2;
        }
    }

}