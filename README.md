# 目前脚本库含有的脚本：

- ### Diary（写日记）

- ### Nayin-bot（微信机器人）

# ① Diary

### 优点：

1. 即写即传，方便快捷

2. 省去打开日记软件时，出现花里胡哨界面耗费的时间，和填入心情、天气等无关紧要参数的时间

3. 采用 MarkDown 编辑，可以传入图片、表格等内容

### 应用场景：

1. 随时在 impromptu.md 中记录日志内容，然后打开终端并输入 up，自动上传日志至 diary.md（impromptu.md 内容自动清空）

3. 想回顾 diary.md 中的内容时，直接打开终端并输入 look 即可

### 注意：

1. 日志记录的时间，是当天（或之前天）最后修改 impromptu.md 的日期

2. 如果当天上传了多次日志，则从第二次开始，视为追加日志内容

### 使用指南：

1. 仅适用于 Windows，用 cmd 或 powershell 运行都可以
2. 在 diary.md 的目录建立 up.bat 和 look.bat，并添加其快捷键，目的是为了运行 python 脚本，记得修改对应的参数
3. 需要将 diary.md 所在的目录设置在 Path 中，以便直接运行 bat 命令
4. 填写 diary.py 中的三个参数，然后可以开始使用啦！
5. 如果 diary.md 中的内容太多了，那么可以将其存储为 pdf，再清空 diary.md 中的内容，重新开始记录

![Diary](https://s1.ax1x.com/2022/04/24/LhNCfP.png)

# ② Nayin-bot

### 优点：

据我所知，在微信机器人领域上另一个很出众的项目叫：Wechaty，虽然社区功能强大，但似乎是收费的，而且所能够使用的全部功能和我基于的开源项目 [wechat-bot](https://github.com/cixingguangming55555/wechat-bot) 相差不大 ，因此 free and easy 就是我最大的优点！

### 使用指南：

README.md 中有详细说明

### 应用场景：

1. 单独和张娜英聊
2. 拉张娜英进群聊

### 待开发：

- 关键字回复
  - 智能搜索：`sg`
  - 功能列表：`帮助 / 菜单 / 功能`
- 图片功能
  - ORC 识图，返回图中识别到的文字（`png`、`jpg`、`jpeg`）

![Nayin-bot](https://s1.ax1x.com/2022/06/26/jEeViD.png)

