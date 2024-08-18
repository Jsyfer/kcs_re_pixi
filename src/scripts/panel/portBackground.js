import * as PIXI from "pixi.js";
import { BASE_URL } from "../App";

export class PortBackground {
  constructor() {
    // 创建Container对象，并添加对象
    this.container = new PIXI.Container();
    this.create();
  }

  create = async () => {
    // 添加背景
    this.ground = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/normal/494_1648.png');
    this.wall = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/normal/502_8118.png');
    this.outside = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/outside/window_bg_4-2.png');
    this.window = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/normal/491_9688.png');
    this.on_wall = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/normal/499_8458.png');
    this.center = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/normal/493_4897.png');
    this.corner = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/furniture/normal/498_8534.png');
    // panel bg
    this.panelBackground = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/img/common/bg/011.png');
    this.panelBackground.visible = false;
    // 添加舰娘
    this.ship = PIXI.Sprite.from(BASE_URL + 'assets/kcs2/resources/ship/full/0538_2823_sullpopastgr.png');

    this.ground.position.y = 412.5;
    this.outside.position.x = 300;
    this.window.position.x = 300;
    this.center.position.y = 200;
    this.corner.position.x = 870;
    this.ship.position.set(400, 100);
    this.container.addChild(
      this.ground,
      this.wall,
      this.outside,
      this.window,
      this.on_wall,
      this.center,
      this.corner,
      this.ship,
      this.panelBackground,
    );
  }

  // 母港事件
  portEvent = () => {
    this.showAll();
  }
  // 编成事件
  henseiEvent = () => {
    this.panelBackground.texture = PIXI.Texture.from(BASE_URL + 'assets/kcs2/img/common/bg/011.png');
    this.hideAll();
  }
  // 補給事件
  hokyuuEvent = () => {
    this.panelBackground.texture = PIXI.Texture.from(BASE_URL + 'assets/kcs2/img/common/bg/012.png');
    this.hideAll();
  }
  // 改装事件
  kaisouEvent = () => {
    this.panelBackground.texture = PIXI.Texture.from(BASE_URL + 'assets/kcs2/img/common/bg/013.png');
    this.hideAll();
  }
  // 入渠事件
  nyuukyoEvent = () => {
    this.panelBackground.texture = PIXI.Texture.from(BASE_URL + 'assets/kcs2/img/common/bg/014.png');
    this.hideAll();
  }
  // 工廠事件
  koujyouEvent = () => {
    this.panelBackground.texture = PIXI.Texture.from(BASE_URL + 'assets/kcs2/img/common/bg/015.png');
    this.hideAll();
  }


  hideAll = () => {
    this.ground.visible = false;
    this.outside.visible = false;
    this.window.visible = false;
    this.center.visible = false;
    this.corner.visible = false;
    this.ship.visible = false;
    this.panelBackground.visible = true;
  }

  showAll = () => {
    this.ground.visible = true;
    this.outside.visible = true;
    this.window.visible = true;
    this.center.visible = true;
    this.corner.visible = true;
    this.ship.visible = true;
    this.panelBackground.visible = false;
  }

}