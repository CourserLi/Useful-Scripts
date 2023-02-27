### 项目：Nayin-bot【第一版】

PS： 出于 Github 的限制不能完整上传资源，因此建议直接在我的[云网盘](https://onedrive-vercel-index-seven-xi.vercel.app/zh-CN/Nayin-bot/)下载

包含以下资源：

- WeChatSetup_3.2.1.121.exe【老版本微信】
- 3.2.1.121-0.0.0.015_稳定版.dll【被注入的 DLL】
- 微信DLL注入器V1.0.3.exe【用于注入 DLL 的注入器】
- wechat-bot-client-python【前辈们的模板，用于借鉴】
- Scripts
  - test1.py【用于测试是否能持续运行】
  - test2.py【用于测试各项功能的运行】
  - run.py【正式运行的脚本】
  - myself.py【我自用的脚本】

### 使用说明

**PS：推荐搭建在 Windows 云服务器上，因为服务器不会关机，机器人的使用需要 24 小时登入微信，且不间断运行 run.py 脚本**

python 版本：3.8 +

```python
# 需要下载的库
websocket-client==0.57.0
bs4
requests
```

详细步骤：

- 下载微信【版本 3.2.1.121】
- 登入微信号【机器人的号】
- 使用注入器注入 DLL
- 测试
  - 运行 test1.py
  - 运行 test2.py

- 运行 run.py，成功即代表完成整个流程【机器人的运行不能关闭 run.py 脚本】

### 开发指南

**PS：只需要修改 run.py**

经过我的缝合，现在 run.py 脚本主要由以下几部分组成：

- 微信机器人的基础类
- 微信机器人的基础函数
- 自定义函数
- 消息处理函数
- 无限服务器支持

但开发所需要迭代的部分只有两个：

- 自定义函数
  - get_tuling【目前我只有此模块，用于闲聊】
- 消息处理函数
  - handle_recv_msg【根据上面来修改】

PS：我使用的 get_tuling 模块 api 接口源于[图灵机器人](http://www.turingapi.com/)

```python
# 从老师那里白嫖的图灵机器人 token
43caf9da5d374607b983d6cc06c14e72
```

关于部分变量我做出大致的解释：

```txt
--------- 关于变量 ---------
@chatroom：群聊
wx_id / senderid：微信号
keyword：接收到的文本消息
nickname：个人用户名

--------- 关于函数 ---------
send_at_msg：发送 @ 消息
send_pic：发送图片
get_memberid：获取群成员名字
get_contact_list：获取通讯录信息
get_member_nick：获取指定群的成员的名字（可用于 @）
send_txt_msg：发送文字消息
send_attach：发送本地文件
get_personal_info：获取本人用户信息
```

值得注意的是，无论你怎么增删改查，该 DLL 最多只能支持微信的以下几个功能（[转自项目源码](https://github.com/cixingguangming55555/wechat-bot)）：

- 发送
  - 客户端发送好友文本消息（支持websocket和HTTP）
  - 客户端获取通讯录好友wxid和名字（支持websocket和HTTP）
  - 客户端发送图片给好友（支持websocket和HTTP）
  - 发送AT消息（支持websocket和HTTP）
  - 发送附件（仅支持HTTP,weboscket)
  - 获取chatroom成员列表(wxid)和昵称（支持websocket和HTTP）
- 接收
  - 文本接收
  - 图片接收（不解密不保存，解密异或即可）
  - 引用消息接收
  - 公众号消息接收
  - 好友请求消息接收

### 碎碎念

当然这个 DLL 支持的功能远不能满足我，但若是做一些新奇的功能，我想那倒是足够了（如 ORC 识别图片提取文字），而且光依赖于文字能做的功能也不少，当我获取到目标 api 接口时，便可以先利用服务器处理再转发给我（如 RSS 订阅、查看图书馆剩余座位、爬虫等）

**但这终归是微信，功能远没有 telegram 强大，因此今后我想更专注于 telegram 而不是 Nayin-bot 第二版了**

## Reference

参考文章：[【WechatBot】基于内存注入下的微信机器人](https://blog.hz2016.com/2022/05/%e3%80%90wechatbot%e3%80%91%e5%9f%ba%e4%ba%8e%e5%86%85%e5%ad%98%e6%b3%a8%e5%85%a5%e4%b8%8b%e7%9a%84%e5%be%ae%e4%bf%a1%e6%9c%ba%e5%99%a8%e4%ba%ba/)

源码项目：[wechat-bot](https://github.com/cixingguangming55555/wechat-bot)