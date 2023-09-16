import * as PIXI from 'pixi.js';
// import { getSpritesheet } from './utils/atlas_load';

import atlasData from './assets/kcs2/img/port/port_skin_1.json';

// Create the application helper and add its render target to the page
const app = new PIXI.Application({ width: 1200, height: 720 });
document.body.appendChild(app.view);

const sprite = PIXI.Sprite.from('./assets/kcs2/img/title/title2.png');
app.stage.addChild(sprite);

// Create the SpriteSheet from data and image
// const spritesheet = getSpritesheet('../assets/kcs2/img/port/port_skin_1.json');

// const frame1 = PIXI.Sprite.from(spritesheet.textures.port_skin_1_0);

// getSpritesheet('./assets/kcs2/img/port/port_skin_1.json').then((spritesheet) => {
//   const frame1 = PIXI.Sprite.from(spritesheet.textures.port_skin_1_0);
//   // add it to the stage to render
//   app.stage.addChild(frame1);
// });

// Create the SpriteSheet from data and image
const spritesheet = new PIXI.Spritesheet(
  PIXI.BaseTexture.from(atlasData.meta.image),
  atlasData,
);
// Generate all the Textures asynchronously
await spritesheet.parse();
// add it to the stage to render
// app.stage.addChild(frame1);
