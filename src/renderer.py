import random
from typing import List
from .utils import get_characters
from .comment_bridge import CommentBridge
from .comment import Comment
from collections import Counter
from .anim import *
import os
from .utils import ensure_assets_are_available


def render_comment_list(comment_list: List[Comment], output_filename = 'hello.mp4', music_code = 'PWR',scene_line_character_fontspace_limit=240,scene_words_limit=85,tts_enabled=True,db_lounder=30,tts_lag=1000,tts_tool='polly',lag_frames=20,fps=18):
    ensure_assets_are_available()
    music_code = process_music_code(music_code)
    counter = Counter()
    thread = []
    for comment in comment_list:
        counter.update({comment.effective_user_id: 1})
    # print('counter-===',counter,type(counter))
    characters = get_characters(counter)
    # print(characters)
    for comment in comment_list:
        comment.character = characters[comment.effective_user_id]
        thread.append(CommentBridge(comment))
    if (output_filename[-4:] != '.mp4'):
        output_filename += '.mp4'
    return comments_to_scene(thread, name_music = music_code, scene_line_character_fontspace_limit=scene_line_character_fontspace_limit,output_filename=output_filename,scene_words_limit=scene_words_limit,tts_enabled=tts_enabled,db_lounder=db_lounder,tts_lag=tts_lag,tts_tool=tts_tool,lag_frames=lag_frames,fps=fps)

def process_music_code(music_code):
    music_code = music_code.lower()
    available_music = os.listdir('assets/music')
    if (music_code == 'rnd'):
        music_code = random.choice(available_music)
    elif (music_code not in available_music):
        music_code = available_music[0]
    return music_code
