import { PixiComponent } from "@pixi/react";

const PixiSceneComponent = PixiComponent("Scene", {
  config: {
    destroy: false, // we don't want to auto destroy the instance on unmount
    destroyChildren: false, // we also don't want to destroy its children on unmount
  },
});

export default PixiSceneComponent;
