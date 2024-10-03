const base_name = "assets/kcs2/img/port/port_ringmenu"
const test_img = base_name + ".png"
const test_img_json = base_name + ".json"

class TestScene extends Phaser.Scene {
  constructor() {
    super({ key: 'testScene' });
  }
  preload() {
    this.load.image('img_refer', test_img);
    this.load.atlas('img_col', test_img, test_img_json);
  }
  create() {
    // refer
    this.add.image(0, 0, 'img_refer').setOrigin(0, 0);;
    // add text
    let title_main = this.textures.get('img_col');
    let frames = title_main.getFrameNames();
    for (let i = 0; i < frames.length; i++) {
      let originx = title_main.frames[frames[i]].cutX;
      let originy = title_main.frames[frames[i]].cutY;
      this.add.text(originx, originy, i, { font: "16px Arial", color: "#ff0000", backgroundColor: "#ffff02" });
    }
  }
}

let img = new Image();
let config = {}
img.src = test_img;
img.onload = function () {
  // set the configuration of the game
  config = {
    type: Phaser.WEBGL, // Phaser will use WebGL if available, if not it will use Canvas
    width: this.width,
    height: this.height
  }
  // create new scene
  let testScene = new TestScene();
  // create a new game, pass the configuration
  let game = new Phaser.Game(config);
  // load scenes
  game.scene.add('testScene', testScene);
  // start title
  game.scene.start('testScene');
}


