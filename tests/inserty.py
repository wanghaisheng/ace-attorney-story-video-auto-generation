
# from pyonfx import *
# import random

# io = Ass("1.ass")
# meta, styles, lines = io.get_data()
# circle = Shape.ellipse(20, 20)


# def romaji(line, l):

#     for syl in Utils.all_non_empty(line.syls):
#         # Leadin Effect
#         l.layer = 0
#         ledi = line.leadin/2 if line.leadin < 300 else 300
#         l.start_time = line.start_time - ledi
#         l.end_time = line.start_time + syl.start_time
#         l.dur = l.end_time - l.start_time
#         l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(%d,0)}%s" % (
#             syl.center, syl.middle, ledi, syl.text)

#         io.write_line(l)
#         # Main Effect
#         l.layer = 1

#         l.start_time = line.start_time + syl.start_time
#         l.end_time = line.start_time + syl.end_time
#         l.dur = l.end_time - l.start_time

#         l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)"\
#             "\\t(0,%d,0.5,\\bord3\blur3\\3c&HFFFFFF&\\fscx125\\fscy125)"\
#             "\\t(%d,%d,1.5,\\fscx100\\fscy100\\bord$%3.f\\blur1\\1c%s\\3c%s)}%s" % (
#                 syl.center, syl.middle,
#                 l.dur/3, l.dur/3, l.dur, line.styleref.outline, line.styleref.color1, line.styleref.color3, syl.text)

#         io.write_line(l)

#         if line.effect == "efek":

#             l.layer = 2
#             l.start_time = line.start_time + syl.start_time
#             l.end_time = line.start_time + syl.end_time + 1200
#             l.dur = l.end_time - l.start_time

#             posisix = random.uniform(-7, 7)
#             posisiy = random.uniform(20, 30)
#             atasbawah = [1, -1]
#             pengali = random.choice(atasbawah)

#             l.text = "{\\alpha&HFF&\\blur1\\bord1\\3c&HFFFFFF&\\t(0,%d,\\bord2\\blur3\\alpha&H00&)\\t(%d,%d,\\bord1\\blur1\\alpha&HFF&)\\t(%d,%d,\\bord2\\blur3\\alpha&H00&)\\t(%d,%d,\\bord1\\blur1\\alpha&HFF&)\\t(%d,%d,\\bord2\\blur3\\alpha&H00&)\\t(%d,%d,\\bord1\\blur1\\alpha&HFF&)\\p1\\pos(%.3f,%.3f)}%s" % (
#                 l.dur/6, l.dur/6, l.dur/3, l.dur/3, l.dur/2, l.dur/2, (l.dur*2)/3, (l.dur*2)/3, (l.dur*5)/6, (l.dur*5)/6, l.dur, syl.center+posisix, syl.middle+(pengali*posisiy), Shape.glance(5, 3, 3))

#             io.write_line(l)

#         # Leadout Effect
#         l.layer = 0
#         ledo = line.leadin/2 if line.leadout < 300 else 300
#         l.start_time = line.start_time + syl.end_time
#         l.end_time = line.end_time + ledo
#         l.dur = l.end_time - l.start_time

#         l.text = "{\\blur1\\an5\\pos(%.3f,%.3f)\\fad(0,%d)}%s" % (
#             syl.center, syl.middle, ledo, syl.text)

#         io.write_line(l)


# def sub(line, l):
#     # Translation Effect

#     l.layer = line.i

#     ledi2 = line.leadin/2 if line.leadin < 300 else 300
#     ledo2 = line.leadin/2 if line.leadout < 300 else 300

#     l.start_time = line.start_time - ledi2
#     l.end_time = line.end_time + ledo2
#     l.dur = l.end_time - l.start_time
#     l.text = "{\\blur1\\fad(%d,%d)}%s" % (
#         ledi2, ledo2, line.text)
#     io.write_line(l)


# # Generating lines
# for line in lines:
# #     print(line.text)
#     if line.styleref.alignment >= 7:
#         romaji(line, line.copy())
#     else:
#         sub(line, line.copy())


# from pyonfx import *

# io = Ass("1.ass")
# meta, styles, lines = io.get_data()


# for line in lines:

#     newline = line.copy()
# #     newline.i = lines[0].i+1
#     newline.text = 'wo shi ge da sha bi'
#     io.write_line(newline)

# io.save()


# from pyonfx import *

# io = Ass("1.ass")
# meta, styles, lines = io.get_data()

# for line in lines:
#     l = line.copy()

#     l.start_time += 2000
#     l.end_time += 2000
#     l.text='edited by me'
#     io.write_line(l)

# io.save()
# io.open_aegisub()

from pyonfx import *

io = Ass("1.ass")
meta, styles, lines = io.get_data()
for line in lines:
    print(line.i)
# lines.insert(1,lines[0].copy())
newline=lines[0].copy()
newline.i=len(lines)+1
newline.syls
lines.insert(newline.i,newline)
newline.text = "I am a new line!"
print(newline.start_time,newline.end_time)
newline.start_time += 2000
newline.end_time += 2000
print(newline.start_time,newline.end_time)
io.write_line(newline)
print(len(lines))
io.save()
# io.open_aegisub()
