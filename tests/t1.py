#coding=utf-8 
import os
import sys
import importlib
importlib.reload(sys)
# p = input('请输入歌词所在路径：')
# os.chdir(p)

# f_name = input('请输入lrc文件名，不含后缀：')
f_name=r'D:\Download\audio-visual\objection_engine\夜空中最亮的星.lrc'

file = open(f'{f_name}',encoding= 'utf-8')
new = open(f'{f_name}.ass','w',encoding= 'utf-8')
new.write('[Script Info]\n')
new.write('; Script generated by Aegisub 3.2.2\n')
new.write('; http://www.aegisub.org/\n')
new.write('Title: Default Aegisub file\n')
new.write('ScriptType: v4.00+\n')
new.write('WrapStyle: 0\n')
new.write('ScaledBorderAndShadow: yes\n')
new.write('YCbCr Matrix: TV.601\n')
new.write('PlayResX: 640\n')
new.write('PlayResY: 360\n')
new.write('\n')
new.write('[V4+ Styles]\n')
new.write('\n')
new.write('Style: right,Arial,32,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,3,9,10,32,1\n')
new.write('Style: left,Arial,32,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,2,2,1,10,10,72,1\n')
new.write('\n')
new.write('[Events]\n')
new.write('Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n')

text = ''
l = 0
flag = 1
try:
    while True:
        text_line = file.readline()
        print(text_line)
        if text_line:
            if len(text)<2:
                start_minute = int(text_line[1:3])
                start_second = int(text_line[4:6])
                start_csecond = int(text_line[7:9]) 
                text = text_line[10:-1]
                flag = 1
            else:
                l += 1
                if start_second >= 3:
                    start_second -= 3
                else:
                    start_minute -= 1
                    start_second += 57
                end_minute = int(text_line[1:3])
                end_second = int(text_line[4:6])
                end_csecond = int(text_line[7:9])
                dur = 6000*(end_minute - start_minute) + 100*(end_second - start_second) + end_csecond - start_csecond - 350
                if l%2 == 0:
                    pos = 'left'
                else:
                    pos = 'right'
                for i in [start_csecond, start_minute, start_second, end_minute, end_second, end_csecond]:
                    if i < 10:
                        i = '0' + str(i)
                    else:
                        i = str(i)
                res = f'Dialogue: 0,0:{start_minute}:{start_second}.{start_csecond},0:{end_minute}:{end_second}.{end_csecond},{pos},,0,0,0,,'
                res += '{\\2c&HFFFFFF&\c&HFFFF00&}'
                if flag == 0:
                    res += '{\kf300}'
                elif flag == 1:
                    res += '{\k75}.{\k75}.{\k75}.{\k75}'
                res += '{\kf'
                res += str(dur)
                res += '}'
                res += text
                res += '{\kf50}'
                res += '\n'
                new.write(res)
                start_minute = int(text_line[1:3])
                start_second = int(text_line[4:6])
                start_csecond = int(text_line[7:9]) 
                text = text_line[10:-1]
                flag = 0
        else:
            break
finally:
    file.close()

new.close()
os.system("pause")