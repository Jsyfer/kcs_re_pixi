import * as PIXI from 'pixi.js';
import convertToPixiAtlas from './utils/atlas_load';
import originAtlasData from './assets/kcs2/img/port/port_skin_1.json';

// Create the application helper and add its render target to the page
const app = new PIXI.Application({ width: 1200, height: 720 });
document.body.appendChild(app.view);

const sprite = PIXI.Sprite.from('./assets/kcs2/img/title/title2.png');
app.stage.addChild(sprite);

// Create the SpriteSheet from data and image
const spritesheet = new PIXI.Spritesheet(
  PIXI.BaseTexture.from('./assets/kcs2/img/port/port_skin_1.png'),
  convertToPixiAtlas(originAtlasData),
);

// Generate all the Textures asynchronously
await spritesheet.parse();

const frame1 = PIXI.Sprite.from(spritesheet.textures.port_skin_1_0);

// add it to the stage to render
app.stage.addChild(frame1);
