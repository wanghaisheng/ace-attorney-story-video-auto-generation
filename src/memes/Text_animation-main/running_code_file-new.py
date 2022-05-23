import argparse
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import os
import time

from numpy.lib.utils import source

def add_audio(source_path, tmp_res_path, res_path, audio_path = None):
    # extract audio
    if not os.path.exists('/tmp/audio'):
        os.makedirs('/tmp/audio')

    if audio_path is None:
        print("extracting orginal audio.")
        audio_path = "/tmp/audio/output-audio.mp3"
        cmd = f"ffmpeg -y -i {source_path} -vn -acodec copy {audio_path}"
        os.system(cmd)

    #add audio
    # time.sleep(2)
    
    if os.path.exists(audio_path):
        # cmd = f"ffmpeg -y  -i {tmp_res_path} -stream_loop -1 -i {audio_path}  -c:v copy -c:a aac {res_path}"
        # cmd = f"ffmpeg -i {tmp_res_path} -filter_complex 'amovie={audio_path}:loop=0,asetpts=N/SR/TB[aud];[0:a][aud]amix[a]'\
        #  -map 0:v -map '[a]' -c:v copy -c:a aac -b:a 256k -shortest {res_path}"
        # cmd = f"ffmpeg  -i {tmp_res_path} -c copy -v 0 -f nut - | \
        #     ffmpeg -thread_queue_size 10K -i -stream_loop -0 -i {audio_path} -map 0:v -map 1:a +shortest -y {res_path}"
        cmd = f"ffmpeg -y -i {tmp_res_path} -stream_loop -1 -i {audio_path} -c:v copy -shortest -fflags +shortest -max_interleave_delta 100M {res_path}"

    else:
        cmd = f"mv {tmp_res_path} {res_path}"

    os.system(cmd)
    os.system("rm -r  /tmp/audio")


    print("video genereate sucess fully at location : ",res_path)


def get_text(current_frame , txt_len, total_frames):
    change_interval = int(total_frames)/int(txt_len)
    return int(current_frame/change_interval) # index of sentence in sentences list.   

def animated_text(source_path,
                  audio_path,
                  sentences,
                  res_path,
                  font_file_path,
                  font_size=50,
                  font_color=[255,0,0,255]):
  
    cap = cv2.VideoCapture(source_path) 
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cap.get(cv2.CAP_PROP_FOURCC)
    tmp_res_path = "/tmp/output.mp4"
    #output vres_pathideo object 
    out = cv2.VideoWriter(tmp_res_path,cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))

    # out = cv2.VideoWriter(res_path,fourcc, fps, (frame_width,frame_height))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frame_counter = 0
    opa = 0 # for altering opacity of text
    boolean = True # varablle helps in effects of alternate frames.
    while(True): 
        ret, image = cap.read() # image is frame of videos.


        if not ret:
            if frame_counter <= 10:
                print("something went wrong.")
            break

        # code for different font style 


        # Convert to PIL Image
        cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im_rgb).convert('RGBA')
        txt = Image.new("RGBA", pil_im.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt)
        # font_path = "/home/saktiman/Dev-ai/video-text-project/font/AlexBrush-Regular.ttf"
        # Choose a font
        font = ImageFont.truetype(font_file_path, font_size)
        if boolean:
            if opa > 255:
                opa = 250
            # font_color=(255,0,0,opa)
            font_color[3]= opa
            opa +=6
            # boolean = not(boolean)
            x = int(frame_width/2)
            y = int(frame_height/2)

        else:
            # font_color=(0,0,255,opa)
            font_color[3]= opa
            boolean = not(boolean)
            x = int(frame_width/2)
            y = int(frame_height/2)

        # Draw the text
        sentence = sentences[get_text(frame_counter, len(sentences), total_frames)]
        print(sentence)
        w, h = draw.textsize(sentence, font=font)
        x = int((frame_width-w)/2 )
        y = int((frame_height-h)/2 )
        # print("wwwww",w)
        # draw.text((x,y), sentence, font=font, fill=font_color)
        draw.text((x,y), sentence, font=font, fill=tuple(font_color))
        pil_img = Image.alpha_composite(pil_im, txt)
        # Save the image
        cv2_im_processed = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
        # cv2.imwrite(f"./result{i}.png", cv2_im_processed)
        imS = cv2.resize(cv2_im_processed, (frame_width,frame_height)) 
        out.write(imS)
        # cv2.imshow('video', imS)
        frame_counter += 1

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    cap.release() 
    out.release()
    cv2.destroyAllWindows()
    add_audio(source_path, tmp_res_path, res_path, audio_path) # for adding audio to the video


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for adding custom audio and text on input video.")
    parser.add_argument("--source_video_path", help="Input video to be processed")
    parser.add_argument("-sa","--source_audio_path",default=None, \
                            help="Input audio to be added in processed")                        
    parser.add_argument("-dst", "--destination_path", type=str, default="./output/output.mp4", help="processed video path(output_path).")
    parser.add_argument("--font_file", default="/home/saktiman/Dev-ai/video-text-project/font/AlexBrush-Regular.ttf",\
                            help="font file for text(should be .ttf) ")
    parser.add_argument("-fs", "--font_size", default=50, type=int, help="font size")
    parser.add_argument("-fc", "--font_color", default="255,255,255,255", help="font color must be in RGBA format.")
    parser.add_argument("-tf", "--text_file", default=None, help=".txt file containing text to be added")
    opt = parser.parse_args()
    fc = list(map(int, opt.font_color.split(',')))

    if opt.text_file is not None:     
        with open(opt.text_file, 'r') as f:
            sentences = f.readlines()
    else:
        sentences = ""
    animated_text(source_path=opt.source_video_path,
                  audio_path=opt.source_audio_path,
                  sentences=sentences,
                  res_path=opt.destination_path,
                  font_file_path=opt.font_file,
                  font_size=opt.font_size,
                  font_color=fc)
