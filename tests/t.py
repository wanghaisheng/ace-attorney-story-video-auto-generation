#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: szkm330
# @Date:   2021-02-18 16:25:32
import sys
import re
import os
import random
from pathlib import Path

'''
1.运行lrc_to_ass.py
2.记事本另存output.ass为ANSI
3.aegisub另存一次ass
'''


# 设置弹幕区
right = 852
left = -25

# 弹幕高度池
high = [65,95,125,155,185,215,245,275,305,335]
n = 0

# 写入ass文件头
info = """
[Script Info]
; Script generated by Aegisub 3.2.2
; http://www.aegisub.org/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.601
PlayResX: 852
PlayResY: 480

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,霞鹜文楷,30,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,2,0,1,10,10,10,1
Style: TALK,霞鹜文楷,35,&H00FFFFFF,&H000000FF,&H004B164D,&H00000000,-1,0,0,0,100,100,0,0,1,2,0,2,10,10,10,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

input_file_name = "input.lrc"
input_file_name=r'D:\Download\audio-visual\objection_engine\夜空中最亮的星.lrc'

output_file_name = "output.ass"


if len(sys.argv)>1 :
    file_name = sys.argv[1]
    file_item = Path(file_name)
    if file_item.exists() and file_item.is_file() :
        input_file_name = sys.argv[1]
        output_file_name = re.sub(r'\..{1,4}$', ".ass", input_file_name)

file_item = Path(input_file_name)
if not(file_item.exists() or file_item.is_file()) :
    sys.exit(-2)

if input_file_name==output_file_name :
    output_file_name = input_file_name + ".ass"

print('{}{}'.format("input: ",input_file_name))
print('{}{}'.format("output: ",output_file_name))

ass = open(output_file_name,"w",encoding = "utf-8")
ass.write(info)
ass.close()

# lrc转换ass
lrc = open(input_file_name,"r",encoding = "utf-8")
ass = open(output_file_name,"a",encoding = "utf-8")

counter_r=0
counter_w=0

for line in lrc:
    line = line.strip()
    print('{}{}'.format("R ",line))
    counter_r=counter_r+1

    if not( re.match("^\[[0-9:\.\s]+\].+",line)) :
        continue

    time_str = line.split(']')[0][1:]
    time_str = time_str.split(':')
    time = [0,0,0]
    if len(time_str)>2 :
        time[0] = int(time_str[0])
        time[1] = int(time_str[1])       
        time[2] = float(time_str[2])
    elif len(time_str)==2 :
        time[1] = int(time_str[0])
        time[2] = float(time_str[1]) 
    else :
        continue
    # 获取起始时间
    time0 = '{}:{}:{}'.format(time[0],time[1],time[2])
    # start_minute=int(time[0])
    # start_second=int(time[1])
    # start_csecond=int(time[2])
    # 时间进位计算
    # time[0] = int(time[0])
    # time[1] = int(time[1])
    time[2] = (time[2])+8

    # 为付费留言延长在弹幕中显示的时间
    if " 留言：" in line :
        time[2] = (time[2])+6    

    if time[2] < 10:
        time[2] = '0' + str(time[2])
    elif time[2] >= 60:
        time[2] = round((time[2]-60),2)
        if time[2] < 10:
            time[2] = '0' + str(time[2])
        else:
            time[2] = str(time[2])
        time[1] = time[1] + 1
    if time[1] < 10:
        time[1] = '0' + str(time[1])
    elif time[1] >= 60:
        time[1] = time[1] - 60
        time[0] = time[0] + 1
        if time[1] < 10:
            time[1] = '0' + str(time[1])
        else:
            time[1] = str(time[1])
    # 获取结束时间
    time1 = '{}:{}:{}'.format(time[0],time[1],time[2])
    # end_minute=int(time[0])
    # end_second=int(time[1])
    # end_csecond=int(time[2])
    # 按顺序轮流设置高度
    pos = high[n]
    n = n + random.randint(1,4)
    if n >= 10:
        n = n-10
    # 获取弹幕内容
    # dur = 6000*(end_minute - start_minute) + 100*(end_second - start_second) + end_csecond - start_csecond - 350

    comment =  line.split(']',2)[1].strip()
    comment = re.sub(r'.*\s(说|留言)：', "", comment)
    # 若内容为空
    if len(comment)<1 :
        continue
    res=''
    res += '{\\2c&HFFFFFF&\c&HFFFF00&}'
    # if flag == 0:
    #     res += '{\kf300}'
    # elif flag == 1:
    #     res += '{\k75}.{\k75}.{\k75}.{\k75}'
    res += '{\kf'
    # res += str(dur)
    res += '}'
    res += comment
    res += '{\kf50}'
    res += '\n'
    
    # 得到最终语句
    end = 'Dialogue: 0,{},{},Default,,0,0,0,,{{\move({},{},{},{})}}{}'.format(time0,time1,right,pos,left*len(comment),pos,comment)
    ass.write('{}\n'.format(end))
    print('{}{}'.format("W: ",end))
    counter_w=counter_w+1
# 结束
lrc.close()
ass.close()

print('\nFinish. W/R={}/{}'.format(counter_w,counter_r))