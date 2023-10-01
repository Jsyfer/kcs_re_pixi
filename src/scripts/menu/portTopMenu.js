import * as PIXI from "pixi.js";
import {Tools} from "../system/Tools"
import {Button} from "../system/Button"
import {App} from "../App"

export class PortTopMenu{
    constructor(config) {
        this.timer = 0;
        // 创建Container对象，并添加对象
        this.container = new PIXI.Container();
        PIXI.Assets.load("assets/kcs2/img/port/port_skin_1.json").then((data) => {
            // 按钮背景
            this.btnBackground = new PIXI.Sprite(data.textures.port_skin_1_14);
            // 边栏
            this.leftBar = new PIXI.Sprite(data.textures.port_skin_1_13);
            this.topBar = new PIXI.Sprite(data.textures.port_skin_1_12);
            this.topBar.position.set(415,0);
            this.bottomBar = new PIXI.Sprite(data.textures.port_skin_1_11);
            this.bottomBar.position.set(415,706);
            // 左上角ring
            this.leftTopRing = new PIXI.Sprite(data.textures.port_skin_1_2);
            this.leftTopRingBackground = new PIXI.Sprite(data.textures.port_skin_1_1);
            this.leftTopRingText = new PIXI.Sprite(data.textures.port_skin_1_3);
            Tools.centerPivot(this.leftTopRing);
            Tools.centerPivot(this.leftTopRingBackground);
            Tools.centerPivot(this.leftTopRingText);
            this.leftTopRing.position.set(65,60);
            this.leftTopRingBackground.position.set(65,60);
            this.leftTopRingText.position.set(65,60);
            App.app.ticker.add(this.leftTopRingRotate);
            App.app.ticker.add(this.leftTopRingTextRotate);

            // user name
            this.userName = this.createTopMenuText('ロビン',174,12);
            // 艦隊司令部Lv.
            this.sireibu = new PIXI.Sprite(data.textures.port_skin_1_24)
            this.sireibu.position.set(415,17);
            this.sireibuLv = this.createTopMenuText('120',550,16);
            this.sireibuRank = this.createTopMenuText('[大将]',600,16);
            // 艦娘
            this.ships = new PIXI.Sprite(data.textures.port_skin_1_25)
            this.ships.position.set(697,17);
            this.shipsNum = this.createTopMenuText('285',740,16);
            // 装備
            this.equipment = new PIXI.Sprite(data.textures.port_skin_1_26)
            this.equipment.position.set(790,17);
            this.equipmentNum = this.createTopMenuText('1210',833,16);
            // 高速修復
            this.repaireMat = new PIXI.Sprite(data.textures.port_skin_1_19)
            this.repaireMat.position.set(900,17);
            this.repaireMatNum = this.createTopMenuText('3000',940,16);
            // 開発資材
            this.developMat = new PIXI.Sprite(data.textures.port_skin_1_20)
            this.developMat.position.set(1000,17);
            this.developMatNum = this.createTopMenuText('3000',1040,16);
            // 改修資材
            this.renovateMat = new PIXI.Sprite(data.textures.port_skin_1_21)
            this.renovateMat.position.set(1100,17);
            this.renovateMatNum = this.createTopMenuText('3000',1140,16);
            // 燃料
            this.fuel = new PIXI.Sprite(data.textures.port_skin_1_15)
            this.fuel.position.set(990,50);
            this.fuelNum = this.createTopMenuText('300000',1020,50);
            // 弾薬
            this.bullet = new PIXI.Sprite(data.textures.port_skin_1_16)
            this.bullet.position.set(990,79);
            this.bulletNum = this.createTopMenuText('300000',1020,79);
            // 鋼
            this.steel = new PIXI.Sprite(data.textures.port_skin_1_17)
            this.steel.position.set(1096,50);
            this.steelNum = this.createTopMenuText('300000',1126,50);
            // ボーキサイト
            this.aluminum = new PIXI.Sprite(data.textures.port_skin_1_18)
            this.aluminum.position.set(1096,79);
            this.aluminumNum = this.createTopMenuText('300000',1126,79);

            // 戦績表示
            this.senki = new Button({
                default: data.textures.port_skin_1_37,
                down: data.textures.port_skin_1_38,
                hover: data.textures.port_skin_1_38,
            })
            this.senki.button.position.set(180,45)
            // 友軍艦隊
            this.yuugun = new Button({
                default: data.textures.port_skin_1_42,
                down: data.textures.port_skin_1_43,
                hover: data.textures.port_skin_1_43,
            })
            this.yuugun.button.position.set(298,43)
            // 図鑑表示
            this.zuken = new Button({
                default: data.textures.port_skin_1_44,
                down: data.textures.port_skin_1_45,
                hover: data.textures.port_skin_1_45,
            })
            this.zuken.button.position.set(418,45)
            // アイテム
            this.item = new Button({
                default: data.textures.port_skin_1_30,
                down: data.textures.port_skin_1_31,
                hover: data.textures.port_skin_1_31,
            })
            this.item.button.position.set(540,45)
            // 模様替え
            this.appearanceChange = new Button({
                default: data.textures.port_skin_1_32,
                down: data.textures.port_skin_1_33,
                hover: data.textures.port_skin_1_33,
            })
            this.appearanceChange.button.position.set(663,45)
            // 任務（クエスト）
            this.quest = new Button({
                default: data.textures.port_skin_1_34,
                down: data.textures.port_skin_1_35,
                hover: data.textures.port_skin_1_35,
            })
            this.quest.button.position.set(780,45)
            // アイテム屋
            this.itemShop = new Button({
                default: data.textures.port_skin_1_22,
                down: data.textures.port_skin_1_23,
                hover: data.textures.port_skin_1_23,
            })
            this.itemShop.button.position.set(900,45)


            // 添加 logo和按钮至容器
            this.container.addChild(
                this.leftTopRing,
                this.btnBackground,
                this.leftBar,
                this.topBar,
                this.bottomBar,
                this.leftTopRingBackground,
                this.leftTopRingText,
                this.userName,
                this.sireibu,
                this.sireibuLv,
                this.sireibuRank,
                this.ships,
                this.shipsNum,
                this.equipment,
                this.equipmentNum,
                this.repaireMat,
                this.repaireMatNum,
                this.developMat,
                this.developMatNum,
                this.renovateMat,
                this.renovateMatNum,
                this.fuel,
                this.fuelNum,
                this.bullet,
                this.bulletNum,
                this.steel,
                this.steelNum,
                this.aluminum,
                this.aluminumNum,
                this.senki.button,
                this.yuugun.button,
                this.zuken.button,
                this.item.button,
                this.appearanceChange.button,
                this.quest.button,
                this.itemShop.button,
            );
        })
    }

    // 左上角圆环旋转动画
    leftTopRingRotate = () => {
        this.timer += 1;
        while (this.timer > 60) {
            this.leftTopRing.angle += 3;
            this.timer -= 60;
        }
    }

    // 左上角圆环文字旋转动画
    leftTopRingTextRotate = () => {
        this.leftTopRingText.rotation += 0.005;
    }

    // 创建顶部菜单文字
    createTopMenuText = (text,x,y) => {
        const spriteText = new PIXI.Text(text, Tools.getTextStyleLight());
        spriteText.position.set(x,y);
        spriteText.style.fill = 'white';
        spriteText.style.fontSize = 18;
        spriteText.style.fontWeight = 100;
        return spriteText;
    }
}