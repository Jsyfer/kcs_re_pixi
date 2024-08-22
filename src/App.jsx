import "./App.css";
import { Stage, Sprite } from "@pixi/react";

const App = () => {
  const bunnyUrl = "assets/kcs2/img/title/04.png";
  return (
    <Stage width={1200} height={720} options={{ background: 0x1099bb }}>
      <Sprite image={bunnyUrl} x={0} y={0} />
    </Stage>
  );
};

export default App;
