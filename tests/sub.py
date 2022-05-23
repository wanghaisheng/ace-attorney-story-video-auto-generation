# from datetime import datetime
# # class for subtitle object, including method to display them in .ssa format
# class Subtitle:
#     def __init__(self, start, end, style, text):
#         self.start = start
#         self.end = end
#         self.style = style
#         self.text = text

#     def display(self):
#         self.start=datetime.strptime(self.start,'%H:%M:%S.%f')
#         print(type(self.start),self.start)
#         datetime.strftime(self.start,'%H:%M:%S.%f')
#         print(type(self.start),self.start)
#         effect = '\fad,{\move(1800,800,572,800,0,700)} {\an7}' 
#         # the effect depends on the language, left-to-right or right-to-left;
#         # for the purpose of testing, will be using right-to-left
#         # subtitle moves from position 1800;800 to 572;800 
#         # movement starts at time self.start + 0 and ends at self.start + 700 milliseconds
#         # this effect was manually programmed in .ssa and can be modified using the tags listed on http://docs.aegisub.org/3.2/ASS_Tags/
#         display = '\n' + 'Dialogue: Marked=0,' + self.start + ',' + self.end + ',' + self.style + ',' + effect + self.text
#         return display

# # Open the xml file
# def get_xml(file_name):
#     xml_file = open(file_name + '.xml',encoding='utf8')
#     content = xml_file.read()
#     xml_file.close()
#     return content

# # Create a txt file with only the subtitles
# def get_subtitles():
#     xml_file = get_xml('SWIhack_copypaste_clean.mp4') # change this file name to suit your need and open any xml subtitle file
#     subtitles = xml_file.split('\n')
#     return subtitles # list of subtitles

# # function to pull data from the TTML tags - 
# def retrieve_data():
#     subtitles = get_subtitles()
#     template = open('sub-style-template.ass', 'a')
#     for subtitle in subtitles:
#         if (subtitle.find('<p begin') != -1): # ignore the lines that do not contain a subtitle (metadata, etc.)
#             attributes = subtitle.split('"') # split at each attribute and value to isolate values
#             start = attributes[1]
#             start = '0:00:0' + start.replace('s', '') # timecode format is adapted
#             end = attributes[5]
#             end = '0:00:0' + end.replace('s', '') # timecode format is adapted
#             style = 'StyleWhite,NTP,0,0,0,' # sets default style; if you edit the template, make sure it matches one of the new styles
#             text = attributes[6] # actual subtitle text
#             text = text.replace('>', '', 1) # clean text from remaining tags
#             text = text.replace('</p>', '') # clean text from remaining tags
#             print(text) # displays in terminal, for verification purpose
#             ass_object = Subtitle(start, end, style, text) # create an object of the Subtitle class
#             ass_subtitle = ass_object.display() # apply the class method to return the correctly formatted subtitle
#             template.write(ass_subtitle) # add the subtitle to the template in the 'events' section
#     template.close()
#     # template = open('template.ass', 'r') 
#     # ass_content = template.read() 
#     # template.close()
#     # return ass_content 

# retrieve_data()



# from pyonfx import *

# # io = Ass("sub-style-template.ass")
# io =Ass('in.ass','out.ass')
# meta, styles, lines = io.get_data()

# lines[0].text = "I am a new line!"
# io.write_line(lines[0])

# io.save()
# io.open_aegisub()

         

# from pysubparser import parser

# subtitles = parser.parse('1.ass')

# for subtitle in subtitles:
#     print(subtitle.start)

# from pyonfx import *

# io = Ass("1.ass",'out.ass')
# meta, styles, lines = io.get_data()

# for line in lines:
#     l = line.copy()
#     print(l.start_time)
# #     l.start_time=
#     l.start_time += 2000
#     l.end_time += 2000
#     print(l.effect)
#     io.write_line(l)

# io.save()
# io.open_aegisub()



from pyonfx import *

io = Ass("1.ass",'out.ass')
meta, styles, lines = io.get_data()
for line in lines:
    print(line.i)
# lines.insert(1,lines[0].copy())
newline=Line()
newline.i=len(lines)+1
# lines.insert(newline.i,newline)
newline.text = "I am a new line!"
print(newline.start_time,newline.end_time)
newline.start_time =0
newline.end_time =1
print(newline.start_time,newline.end_time)
io.write_line(newline)
print(len(lines))
io.save()
# io.open_aegisub()
