import * as PIXI from "pixi.js";
import { BASE_URL } from "../App";

class KcsTools {
  // 设置图形坐标为中心点
  centerPivot = (sprite) => {
    sprite.pivot.set(Math.round(sprite.width / 2), Math.round(sprite.height / 2));
  }

  getTextStyleLight = () => {
    PIXI.Assets.load(BASE_URL + 'assets/kcs2/resources/font/A-OTF-UDShinGoPro-Light.woff2').then((font) => {
      return font;
    })
  }

  getTextStyleRegular = () => {
    PIXI.Assets.load(BASE_URL + 'assets/kcs2/resources/font/A-OTF-UDShinGoPro-Regular.woff2').then((font) => {
      return font;
    })
  }

}

export const Tools = new KcsTools();