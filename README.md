# kcs_re_pixi

这是一个基于pixi.js的kancolle重制版，目前处于开发阶段，仅支持部分功能。

## 架构

- 前端：`pixijs` + `React`
- 后端：`Django`
- 数据库：`Sqlite3`

## 开发进度

### 前端

母港界面基础动画以及编成，补给，改装，出击，工厂按钮基本功能构建完成。

### 后端

母港，编成，补给，改装，出击，工厂相关API构建完成。
数据库雏形完成

## TODO list

### 前端

- 编成，补给，改装，出击，工厂界面各类细节
- 改修工厂
- 出击海域
- 演习界面
- 远征界面
- 图鉴界面
- 战绩表示
- 家具界面
- 所持物品界面
- 战斗相关动画

### 后端

- 装备bonus master数据获取
- 舰娘初期装备master数据获取
- 编队预设上限解放
- 装备预设上限解放
- 各类物品使用逻辑
- 改修工厂
- 各海域出击
- 战斗逻辑
- 远征
- 舰娘升级逻辑
- 图鉴功能
- 家具购买
- 家具替换
- 初始教程
- 任务系统

### API参考：

ship.api_kyouka[0]火力，[1]雷装，[2]对空，[3]装甲，[4]运，[5]HP，[6]不明

> api_hougeki1

`api_at_eflag`攻击方区分flag

- 0: 我方攻击
- 1: 敌方攻击

`api_at_list`攻击实施舰船的位置
通过舰船在编队中所处位置表示

`api_at_type`炮击类型

- 0:普通攻击（通常单发炮击，反潜攻击，）
- 2:二连炮击
- 7:空母战爆联合

`api_cl_list`暴击flag

- 0:未命中
- 1:未暴击
- 2:暴击

`api_df_list`受到伤害的目标舰船位置

`api_si_list`发动攻击的装备列表
使用装备的id表示，通用装备或没有装备时使用`-1`表示

`api_color_no`

1. 通常的敌方遭遇点或空白点（白/蓝色底）
2. 资源获取点（铝、燃料、弹药等，绿色底）
3. 能产生分支选择的节点/漩涡点（紫色或红色等特殊标记）
4. 带有图标事件的点（如航空侦察、敌方联合舰队等，视具体活动而定）
5. Boss 节点（通常对应不同的难度或敌方旗舰类型）
6. Boss 节点（通常对应不同的难度或敌方旗舰类型）

在《舰队Collection》（艦これ）的地图出击 API 响应数据中（/kcsapi/api_req_map/start 或 /next），api_event_id 是一个至关重要的字段。它与 api_color_no 配合使用，用来定义舰队当前移动到的格子所触发的具体事件类型（如战斗、资源获取等）。 [1, 2]
根据开源插件（如 poi、七四式电子观测仪）的源码和社区逆向解析，api_event_id 的数值及其对应含义通常如下： [2, 3, 4, 5]

## api_event_id 数值定义映射表

| 数值 (api_event_id) [1, 2, 6, 7, 8, 9, 10] | 事件类型 (英文/日文描述)              | 中文具体含义                                                                                |
| ------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------- |
| 1                                          | No Event / 初期位置                   | 无事件（通常仅用于起点，或者某些完全没有发生任何事的极特殊空白点）                          |
| 2                                          | Obtain Resources / アイテム獲得       | 获得资源/道具（俗称绿点，能捡到燃料、弹药、钢材、铝、或开发资材等）                         |
| 3                                          | Lose Resources / 涡流（うずしお）     | 损失资源（俗称紫色漩涡点，会根据电探携带情况扣除燃料或弹药）                                |
| 4                                          | Normal Battle / 通常戦闘              | 常规敌方遭遇战（最普通的常规战斗点）                                                        |
| 5                                          | Boss Battle / ボス戦                  | Boss 战 / 旗舰战（该海域的最终或阶层 Boss 节点）                                            |
| 6                                          | Manual Selection / 能動分岐           | 能动分歧点（由玩家自主点击罗针盘选择接下来航向的格子）                                      |
| 7                                          | Air Strike / 航空戦 / 航空偵察        | 航空战/航空侦查点（不发生炮击战、纯进行对空对潜及开幕空袭的特殊点，或活动海域的航空侦察点） |
| 8                                          | Escort Success / 船団護衛成功         | 船团护卫成功 / 运输物资（主要存在于活动海域的 TP 运输管线结算点、远洋护卫等机制中）         |
| 9                                          | Long Distance Air Raid / 基地航空空袭 | 长距离空袭点 / 基地遭袭（高空迎击战或深海对玩家舰队进行的纯空袭点）                         |

---

## 进阶：如何与 api_event_kind 组合判断？

在实际开发和辅助工具的逻辑中，单靠 api_event_id 有时无法完全锁定格子的行为，需要同时结合 api_event_kind（事件种类代码）进行二级判定。 [2, 11]
例如当 api_event_id 为 4（常规战斗） 时： [12]

- 如果 api_event_kind = 1：代表 昼战（常规遭遇战）。
- 如果 api_event_kind = 2：代表 夜战点（进点直接触发夜战，不经过昼战）。
- 如果 api_event_kind = 4：代表 深海联合舰队点（敌方为 12 艘船的联合舰队组合）。
- 如果 api_event_kind = 5：代表 反潜战点 / 夜转昼战点（视海域而定）。 [4, 8, 10, 13, 14]

[1] [https://electronicobserver.blog.fc2.com](http://electronicobserver.blog.fc2.com/blog-entry-107.html?sp&m2=res)
[2] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@6.9.5/files/utils.js.map)
[3] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@6.9.5/files/utils.js.map)
[4] [https://g.nga.cn](https://g.nga.cn/read.php?tid=32299742&_fp=284&forder_by=postdatedesc)
[5] [https://electronicobserver.blog.fc2.com](http://electronicobserver.blog.fc2.com/blog-entry-107.html?sp&m2=res)
[6] [https://github.com](https://github.com/andanteyk/ElectronicObserver/issues/63)
[7] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@7.7.0/files/utils.js.map)
[8] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@7.7.0/files/utils.js.map)
[9] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@7.7.0/files/utils.js.map)
[10] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@6.9.5/files/utils.js.map)
[11] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@6.9.5/files/utils.js.map)
[12] [https://app.unpkg.com](https://app.unpkg.com/poi-plugin-prophet@7.7.0/files/utils.js.map)
[13] [https://nga.178.com](https://nga.178.com/read.php?tid=9357504&page=42)
[14] [https://electronicobserver.blog.fc2.com](http://electronicobserver.blog.fc2.com/blog-entry-74.html?sp&m2=res)
[15] [https://nga.178.com](https://nga.178.com/read.php?tid=9357504&page=42)

在《舰队Collection》的地图出击与前进接口（/api_req_map/start 和 /api_req_map/next）中，api_airsearch 是一个专门用来描述**“航空侦察”事件结果**的子 JSON 对象。 [1]
当舰队进入带有航空侦察机制的特殊绿点时（通常配合 api_event_id: 7 航空侦察点使用），后端会通过该对象告诉前端这次侦察是成功、大成功还是失败，以及派出了什么类型的侦察机。 [1, 2]

---

## 🧱 api_airsearch 的内部结构

该对象通常包含以下两个核心字段： [1]

"api_airsearch": {
"api_plane_type": 0,
"api_result": 0
}

## 1. api_plane_type（派出侦察机的机型种类）

定义了前端在播放航空侦察动画时，要在屏幕上渲染哪种飞机的模型与小图标。

- 0：未派飞机（通常是非航空侦察点、或者由于没有配备任何侦察/水上机导致无法触发侦察）。
- 1：水上侦察机 / 水上轰炸机（如 零式水上侦察机、瑞云等）。
- 2：舰载侦察机（如 彩云、二式舰上侦察机）。 [1, 2]

## 2. api_result（航空侦察的最终判定结果）

定义了本次侦察的成败。这个结果直接决定了你在这个格子能收货多少资源（如弹药、铝土），或者是否能触发后续的加成。

- 0：失败 / 无结果（没有获取资源）。
- 1：成功（播放白色/绿色“成功”特效，获得基础资源）。
- 2：大成功（播放金色“大成功”特效，获得的资源量大幅提升）。 [1]

---

## 💡 开发者与工具视角的逻辑

对于航海日志、poi 等辅助工具或插件开发者来说，通常的解析逻辑如下：

1.  如果在非侦察点（普通战斗点、漩涡点），该对象的值固定为 "api_plane_type": 0, "api_result": 0。
2.  当在活动海域抓包遇到 api_result 出现 1 或 2 时，工具可以立刻在掉落/物资统计面板中记录：“本次出击在 X 点触发航空侦察成功，斩获铝土/弹药 XX 个”。 [1]

如果你想知道特定活动海域中航空侦察大成功的装备索敌系数判定公式，或者需要其他战斗结算字段（如 api_destruction_battle 基地航空队遭袭），请随时告诉我！

[1] [https://nga.178.com](https://nga.178.com/read.php?tid=9357504&page=42)
[2] [https://en.kancollewiki.net](https://en.kancollewiki.net/Type_2_Reconnaissance_Aircraft)
