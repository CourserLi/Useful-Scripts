#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import datetime
import os, time
import re

# 需要填写的三个参数：
# impromptu.md 的地址
impromptu = "C:\\Users\\LILANJUN\\Desktop\\impromptu.md"
# diary.md 的地址
diary = "D:\\XOPP\\Identity\\diary.md"
# 励志名言
good = "追求自由 保持好奇"

date = str(datetime.datetime.now())
week_list = {
    "Sun": "周日",
    "Mon": "周一",
    "Tue": "周二",
    "Wed": "周三",
    "Thu": "周四",
    "Thur": "周四",
    "Fri": "周五",
    "Sat": "周六"
}
month_list = {
    "Jan": "1",
    "Feb": "2",
    "Mar": "3",
    "Apr": "4",
    "May": "5",
    "Jun": "6",
    "Jul": "7",
    "Aug": "8",
    "Sep": "9",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
}
week = datetime.date(int(date[:4]), int(date[5:7]), int(date[8:10])).weekday()
remind = 7 - week - 1
impromptu_time = time.ctime(os.stat(impromptu).st_mtime)
impromptu_week = week_list[impromptu_time.split()[0]]
impromptu_month = month_list[impromptu_time.split()[1]]
impromptu_day = impromptu_time.split()[2]
impromptu_year = impromptu_time.split()[4]
impromptu_hour = impromptu_time.split()[3][:2]
impromptu_minute = impromptu_time.split()[3][3:5]


def impromptu2diary():
    up_line = []
    with open(impromptu, "r", encoding='utf-8') as file:
        file.readline()
        tmp = file.readline()
        while (tmp):
            up_line.append(tmp)
            tmp = file.readline()
    file.close()

    all_null = 0
    for tmp in up_line:
        if tmp == "\n":
            all_null += 1
    if (all_null == len(up_line)):
        print("您的日志为空，不能上传哦~")
        return

    while (up_line[0] == "\n"):
        up_line = up_line[1:]
    while (up_line[-1] == "\n"):
        up_line = up_line[:-1]

    with open(impromptu, "w", encoding='utf-8') as file:
        file.write("**" + good + "：距离本周结束还有 " + str(remind) + " 天【勿删】**\n\n")
    file.close()

    writeup = impromptu_year + "年" + impromptu_month + "月" + impromptu_day + "日 " + impromptu_week + " " + impromptu_hour + "点" + impromptu_minute + "分"

    with open(diary, "r", encoding='utf-8') as file:
        tmp = file.read()
    file.close()
    if (tmp == "" or tmp == "\n" or tmp == "\n\n"):
        with open(diary, "w", encoding='utf-8') as file:
            file.write("**" + writeup + "【" + good + "】" + "**\n")
            ans = 0
            while (ans < len(up_line)):
                file.write(up_line[ans])
                ans += 1
            print("成功上传啦 o(*￣▽￣*)ブ")
        file.close()
        return

    impromptu_verify = impromptu_year + "年" + impromptu_month + "月" + impromptu_day + "日"
    str_verify = "【" + good + "】"
    for line in open(diary, "r", encoding='utf-8'):
        if (str_verify in line):
            diary_verify = line
    diary_year, diary_month, diary_day = re.findall(r"\d+", diary_verify)[0], re.findall(r"\d+",diary_verify)[1], re.findall(r"\d+", diary_verify)[2]
    diary_verify = diary_year + "年" + diary_month + "月" + diary_day + "日"
    if (diary_verify == impromptu_verify):
        with open(diary, "a+", encoding='utf-8') as file:
            file.write("\n\n")
            ans = 0
            while (ans < len(up_line)):
                file.write(up_line[ans])
                ans += 1
            print("成功追加日志啦 o(*￣▽￣*)o")
        file.close()
        return

    with open(diary, "a+", encoding='utf-8') as file:
        file.write("\n\n\n\n")
        file.write("**" + writeup + "【" + good + "】" + "**\n")
        ans = 0
        while (ans < len(up_line)):
            file.write(up_line[ans])
            ans += 1
        print("成功上传啦 o(*￣▽￣*)ブ")
    file.close()


impromptu2diary()
