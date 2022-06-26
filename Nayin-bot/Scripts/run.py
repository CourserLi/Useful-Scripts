#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import websocket
import time
import json
import requests
import os
import random
import datetime
import traceback
from bs4 import BeautifulSoup
websocket._logging._logger.level = -99

ip = '127.0.0.1'
port = 5555

SERVER = f'ws://{ip}:{port}'
HEART_BEAT = 5005
RECV_TXT_MSG = 1
RECV_TXT_CITE_MSG = 49
RECV_PIC_MSG = 3
USER_LIST = 5000
GET_USER_LIST_SUCCSESS = 5001
GET_USER_LIST_FAIL = 5002
TXT_MSG = 555
PIC_MSG = 500
AT_MSG = 550
CHATROOM_MEMBER = 5010
CHATROOM_MEMBER_NICK = 5020
PERSONAL_INFO = 6500
DEBUG_SWITCH = 6000
PERSONAL_DETAIL = 6550
DESTROY_ALL = 9999
JOIN_ROOM = 10000
ATTATCH_FILE = 5003

################################### 微信机器人的基础类 ######################################################


class WechatBot:
    def __init__(self, ip='127.0.0.1', port=5555):
        self.base_url = f'http://{ip}:{port}/'

    @staticmethod
    def get_id():
        return str(int(datetime.datetime.now().timestamp()))

    def send(self, uri, data):
        """
        通用发送函数，可能会失败，应在外层catch error
        """
        base_data = {
            'id': self.get_id(),
            'type': 'null',
            'roomid': 'null',
            'wxid': 'null',
            'content': 'null',
            'nickname': 'null',
            'ext': 'null',
        }
        base_data.update(data)
        url = f'{self.base_url}{uri}'
        res = requests.post(url, json={'para': base_data}, timeout=5)
        return res.json()

    def send_at_msg(self, wx_id, room_id, content, nickname):
        """
        发送at消息，at会写在最前面。@付好后的内容由nickname决定，但是是否真的收到at消息取决于wx_id
        :param wx_id:
        :param room_id:
        :param content:
        :param nickname:
        :return:
        """
        uri = 'api/sendatmsg'
        data = {
            'type': AT_MSG,
            'roomid': room_id,
            'content': content,
            'wxid': wx_id,
            'nickname': nickname
        }
        return self.send(uri, data)

    def send_pic(self, to, path):
        """
        发送图片
        :param to: roomid 或 wxid
        :param path: 绝对路径
        :return:
        """
        uri = 'api/sendpic'
        data = {
            'type': PIC_MSG,
            'wxid': to,
            'content': path
        }
        return self.send(uri, data)

    def get_memberid(self):
        """
        获取群成员id
        :return:
        """
        uri = 'api/getmemberid'
        data = {
            'type': CHATROOM_MEMBER,
            'content': 'op:list member'
        }
        return self.send(uri, data)

    def get_contact_list(self):
        """
        获取通讯录信息
        :return:
        """
        uri = 'api/getcontactlist'
        data = {
            'type': USER_LIST,
        }
        return self.send(uri, data)

    def get_member_nick(self, wx_id, room_id):
        """
        获取指定群的成员的昵称（可用于at）
        :param wx_id: 成员wx id
        :param room_id: 群id
        :return:
        """
        uri = 'api/getmembernick'
        data = {
            'type': CHATROOM_MEMBER_NICK,
            'wxid': wx_id,
            'roomid': room_id
        }
        return self.send(uri, data)

    def get_chatroom_member_list(self):
        """
        获取所有群的群友
        :return:
        """
        uri = 'api/get_charroom_member_list'
        data = {
            'type': CHATROOM_MEMBER,
        }
        return self.send(uri, data)

    def send_txt_msg(self, to, content):
        """
        发送文字消息
        :param to: roomid或wxid,必填
        :param content: 内容
        :return:
        """
        uri = 'api/sendtxtmsg'
        data = {
            'type': TXT_MSG,
            'wxid': to,
            'content': content
        }
        return self.send(uri, data)

    def send_attach(self, to, path):
        """
        发送本地文件
        :param to: roomid或wxid,必填
        :param path: 绝对路径
        :return:
        """
        uri = 'api/sendattatch'
        data = {
            'type': ATTATCH_FILE,
            'wxid': to,
            'content': path
        }
        return self.send(uri, data)

    def get_personal_info(self):
        """
        获取本人用户信息
        :return:
        """
        uri = 'api/get_personal_info'
        data = {
            'type': PERSONAL_INFO
        }
        return self.send(uri, data)

################################### 微信机器人的基础函数 ################################################


def getid():
    return time.strftime("%Y%m%d%H%M%S")


def output(msg):
    now = time.strftime("%Y-%m-%d %X")
    print(f'[{now}]:{msg}')


def send_wxuser_list():
    qs = {
        'id': getid(),
        'type': USER_LIST,
        'content': 'user list',
        'wxid': 'null',
    }
    return json.dumps(qs)

def handle_nick(j):
    data = j.content
    i = 0
    for d in data:
        output(f'nickname:{d.nickname}')
        i += 1


def hanle_memberlist(j):
    data = j.content
    i = 0
    for d in data:
        output(f'roomid:{d.roomid}')
        i += 1


def handle_wxuser_list(j):
    output('启动完成')


def heartbeat(msgJson):
    output(msgJson['content'])


def on_open(ws):
    ws.send(send_wxuser_list())


def on_error(ws, error):
    output(f'on_error:{error}')


def on_close(ws):
    output("closed")

################################### 自定义函数 ################################################


def get_tuling(text, sid):
    # 使用字典定义请求信息
    req_dict = {
        "perception": {
            "inputText": {
                "text": text
            },
        },
        "userInfo": {
            "apiKey": "43caf9da5d374607b983d6cc06c14e72",  # 注册一个机器人填写自己的appkey
            "userId": sid
        }
    }

    # 指定请求头信息的类型为json
    header = {'Content-Type': "application/json"}
    url = "http://openapi.tuling123.com/openapi/api/v2"
    resp = requests.post(url=url, data=json.dumps(req_dict), headers=header)
    content = resp.content.decode()
    resp_dict = json.loads(content)
    # 机器人回复消息
    result = resp_dict['results']
    # 遍历消息
    for result in result:
        if result['resultType'] != 'text':
            continue
        else:
            text = result['values']['text']
        print("图灵机器人回复内容:%s" % text)
        return text

################################### 消息处理函数 ################################################


def handle_recv_msg(msgJson):
    wb = WechatBot()
    output(f'收到消息:{msgJson}')
    keyword = msgJson['content'].replace('\u2005', '')
    if '@chatroom' in msgJson['wxid']:
        roomid = msgJson['wxid']  # 群id
        senderid = msgJson['id1']  # 个人id
    else:
        roomid = None
        nickname = 'null'
        senderid = msgJson['wxid']  # 个人id
    nickname = wb.get_member_nick(wx_id=senderid, room_id=roomid)
    nickname = json.loads(nickname['content'])['nick']
    
    if roomid:
        sid = random.randint(1, 10)
        send_text = get_tuling(keyword, sid)
        wb.send_at_msg(wx_id=senderid, room_id=roomid,
                       content=send_text, nickname=nickname)
    else:
        sid = random.randint(1, 10)
        send_text = get_tuling(keyword, sid)
        wb.send_txt_msg(to=senderid, content=send_text)
    """
    if keyword[:2] == 'sg':  # 智能搜索
        keyword = keyword[2:].strip()
        pass
    elif keyword[:4] == "@张娜英":  # 闲聊
        keyword = keyword[4:]
        sid = random.randint(1, 10)
        send_text = get_tuling(keyword, sid)
        wb.send_txt_msg(to='25644933641@chatroom', content=send_text)
    """

################################### 无限服务器支持 ################################################


def on_message(ws, message):
    j = json.loads(message)
    resp_type = j['type']
    # switch结构
    action = {
        CHATROOM_MEMBER_NICK: handle_nick,
        PERSONAL_DETAIL: handle_recv_msg,
        AT_MSG: handle_recv_msg,
        DEBUG_SWITCH: handle_recv_msg,
        PERSONAL_INFO: handle_recv_msg,
        TXT_MSG: handle_recv_msg,
        PIC_MSG: handle_recv_msg,
        CHATROOM_MEMBER: hanle_memberlist,
        RECV_PIC_MSG: handle_recv_msg,
        RECV_TXT_MSG: handle_recv_msg,
        HEART_BEAT: heartbeat,
        USER_LIST: handle_wxuser_list,
        GET_USER_LIST_SUCCSESS: handle_wxuser_list,
        GET_USER_LIST_FAIL: handle_wxuser_list,
    }
    action.get(resp_type, print)(j)


ws = websocket.WebSocketApp(
    SERVER, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)
ws.run_forever()
