import { Scene } from "../system/Scene";
import { PortMainMenu } from "../menu/portMainMenu";
import { PortTopMenu } from "../menu/portTopMenu";
import { PortSideMenu } from "../menu/portSideMenu";
import { PortBackground } from "../panel/portBackground";
import { HenseiPanel } from "../panel/henseiPanel";

// 母港界面
export class Port extends Scene {
    async create() {
        // 添加背景
        this.portBackground = new PortBackground();
        // 添加编成面板
        this.henseiPanel = new HenseiPanel();
        // 添加母港主菜单
        this.portMainMenu = new PortMainMenu();
        // 添加母港顶部菜单
        this.portTopMenu = new PortTopMenu();
        // 添加母港侧边菜单
        this.portSideMenu = new PortSideMenu();

        this.container.addChild(
            this.portBackground.container,
            this.henseiPanel.container,
            this.portMainMenu.container,
            this.portTopMenu.container,
            this.portSideMenu.container,
        );

    }

}
