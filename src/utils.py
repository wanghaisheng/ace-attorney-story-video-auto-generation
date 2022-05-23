import eyed3
from .constants import Character
import random
from collections import Counter
import os
import requests
import zipfile
import textwrap
# from harvesttext import HarvestText
from PIL import Image, ImageDraw, ImageFont, ImageFile
import re
from plane import *
# import hanlp
import budoux
# import jieba
import pysubs2
from pysubs2 import SSAEvent
from pyonfx import *
import ffmpeg
# import nltk

import cv2
import time
from playwright.sync_api import sync_playwright
import langid

regexpatternforurl = r"((?<=[^a-zA-Z0-9])(?:https?\:\/\/|[a-zA-Z0-9]{1,}\.{1}|\b)(?:\w{1,}\.{1}){1,5}(?:com|org|edu|gov|uk|net|ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil|iq|io|ac|ly|sm){1}(?:\/[a-zA-Z0-9]{1,})*)"

regex_french_characters=r"/^[a-zàâçéèêëîïôûùüÿñæœ .-]*$/i"

regex_turkish_characters = r".*[öçğışü].*"
regex_spanish_characters = r"/^[0-9a-zñáéíóúü]+$/i"
re1=r"(?U)[^-_/.,\p{Alnum} ]+"
def split_str_into_newlines(text: str, font_path, font_size, scene_line_character_fontspace_limit: int = 240):
    font = ImageFont.truetype(font_path, font_size)
    image_size = font.getsize(text=text)
    new_text = ""
    # lines = int(image_size[0]/scene_line_character_fontspace_limit)+1
    lang = langid.classify(text)[0]
    # results = longtext2paragraph(text,80,lang,lines)
    # print(lines,'==scene to lines:',results)
    # return ''.join(results)
    if lang in ['zh', 'jp', 'kr']:

        text = spliteKeyWord_zh(text)
        for word in text:
            last_sentence = new_text.split("\n")[-1] + word
            # print('00000000000000---',last_sentence,font.getsize(text=last_sentence)[0])
            if font.getsize(text=last_sentence)[0] >= scene_line_character_fontspace_limit:
                new_text += "\n" + word
            else:
                new_text += word
    else:
        # text = spliteKeyWord_en(text)
        text = text.split(' ')
        for word in text:
            last_sentence = new_text.split("\n")[-1] + word + " "
            # print('00000000000000---',last_sentence,font.getsize(text=last_sentence)[0])
            if font.getsize(text=last_sentence)[0] >= scene_line_character_fontspace_limit:
                new_text += "\n" + word + " "
            else:
                new_text += word + " "
    print('=======new_text', new_text.strip())
    return new_text.strip(), lang


def get_playright(url):
    with sync_playwright() as p:
        #     browser = p.chromium.launch()
        #     browser = p.firefox.launch(headless=False)

        PROXY_SOCKS5 = "socks5://127.0.0.1:1080"

        browserLaunchOptionDict = {
            "headless": False,
            "proxy": {
                "server": PROXY_SOCKS5,
            }
        }

        browser = p.chromium.launch(**browserLaunchOptionDict)
    #     context = browser.new_context(proxy={"server": "socks5://127.0.0.1:1080"})
        # Open new page
        page = browser.new_page()
        page.goto(url)
    return


def tts_playright():

    with sync_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = browser_type.launch(headless=False)
            page = browser.newPage()
            page.goto('https://duckduckgo.com/')
            element = page.querySelector(
                'input[id=\"search_form_input_homepage\"]')

            parent = element.querySelector('xpath=..')
            grandparent = element.querySelector('xpath=../..')
            siblings = element.querySelectorAll('xpath=following-sibling::*')
            children = element.querySelectorAll('xpath=child::*')

            browser.close()


def TextCorrectorbeforeTTS(txt):
    p = Plane()
    txt=txt.replace('&#x200B;','')
    punc.remove(txt)
    # update() will init Plane.text and Plane.values
    p.update(txt).replace(URL, '').text
    # update() will init Plane.text and Plane.values
    p.update(txt).replace(HTML, '').text
    # print(result)
    # ASCII = build_new_regex('ascii', r'[a-zA-Z0-9]+', ' ')
    # WORDS = ASCII + CHINESE_WORDS
    CN_EN_NUM = sum([CHINESE, ENGLISH, NUMBER])

    txt =' '.join([t.value for t in list(extract(txt, CN_EN_NUM))])
    return txt


def ensure_assets_are_available():
    if not os.path.exists('./assets'):
        print('Assets not present. Downloading them')
        response = requests.get(
            'https://drive.google.com/file/d/1hQ5MTPxjom_E6mqyJO_ppNrhFp_c4PYx/view?usp=sharing')
        with open('assets.zip', 'wb') as file:
            file.write(response.content)
        with zipfile.ZipFile('assets.zip', 'r') as zip_ref:
            zip_ref.extractall('assets')
        os.remove('assets.zip')


def spliteKeyWord_en(str):
    # sent_text = nltk.sent_tokenize(str)  # this gives us a list of sentences
    # # now loop over each sentence and tokenize it separately
    # words = []
    # for sentence in sent_text:
    #     tokenized_text = nltk.word_tokenize(sentence)
    #     # tagged = nltk.pos_tag(tokenized_text)
    #     words.extend(tokenized_text)
    words = segment(punc.remove(str))    

    return words


def spliteKeyWord_zh(str):
    words = segment(punc.remove(str))    

    # words = jieba.lcut(str)
    return words


def get_characters(common: Counter):
    users_to_characters = {}
    most_common = [t[0] for t in common.most_common()]
    # print('most_common',type(most_common),most_common)
    all_rnd_characters = [
        Character.GODOT,
        Character.FRANZISKA,
        Character.JUDGE,
        Character.LARRY,
        Character.MAYA,
        Character.KARMA,
        Character.PAYNE,
        Character.MAGGEY,
        Character.PEARL,
        Character.LOTTA,
        Character.GUMSHOE,
        Character.GROSSBERG,
        Character.APOLLO,
        Character.KLAVIER,
        Character.MIA,
        Character.WILL,
        Character.OLDBAG,
        Character.REDD,
    ]
    rnd_characters = []
    if len(most_common) > 0:
        users_to_characters[most_common[0]] = Character.PHOENIX
        if len(most_common) > 1:
            users_to_characters[most_common[1]] = Character.EDGEWORTH
            for character in most_common[2:]:
                if len(rnd_characters) == 0:
                    rnd_characters = all_rnd_characters.copy()
                rnd_character = random.choice(
                    rnd_characters
                )
                rnd_characters.remove(rnd_character)
                users_to_characters[character] = rnd_character
    return users_to_characters


def get_all_music_available():
    ensure_assets_are_available()
    available_music = os.listdir('./assets/music')
    available_music.append('rnd')
    return available_music


def is_music_available(music: str) -> bool:
    music = music.lower()
    ensure_assets_are_available()
    available_music = os.listdir('./assets/music')
    available_music.append('rnd')
    return music in available_music


def url_ok(url):

    try:
        response = requests.head(url)
    except Exception as e:
        # print(f"NOT OK: {str(e)}")
        return False
    else:
        if response.status_code == 200:
            # print("OK")
            return True
        else:
            print(f"NOT OK: HTTP response code {response.status_code}")

            return False


abbreviations = {'dr.': 'doctor', 'mr.': 'mister', 'bro.': 'brother', 'bro': 'brother', 'mrs.': 'mistress', 'ms.': 'miss', 'jr.': 'junior', 'sr.': 'senior',
                 'i.e.': 'for example', 'e.g.': 'for example', 'vs.': 'versus'}
terminators = ['.', '!', '?']
wrappers = ['"', "'", ')', ']', '}']


def find_sentences(paragraph):
    end = True
    sentences = []
    while end > -1:
        end = find_sentence_end(paragraph)
        if end > -1:
            sentences.append(paragraph[end:].strip())
            paragraph = paragraph[:end]
    sentences.append(paragraph)
    sentences.reverse()
    return sentences


def find_sentence_end(paragraph):
    [possible_endings, contraction_locations] = [[], []]
    contractions = abbreviations.keys()
    sentence_terminators = terminators + \
        [terminator + wrapper for wrapper in wrappers for terminator in terminators]
    for sentence_terminator in sentence_terminators:
        t_indices = list(find_all(paragraph, sentence_terminator))
        possible_endings.extend(([] if not len(t_indices) else [
                                [i, len(sentence_terminator)] for i in t_indices]))
    for contraction in contractions:
        c_indices = list(find_all(paragraph, contraction))
        contraction_locations.extend(
            ([] if not len(c_indices) else [i + len(contraction) for i in c_indices]))
    possible_endings = [
        pe for pe in possible_endings if pe[0] + pe[1] not in contraction_locations]
    if len(paragraph) in [pe[0] + pe[1] for pe in possible_endings]:
        max_end_start = max([pe[0] for pe in possible_endings])
        possible_endings = [
            pe for pe in possible_endings if pe[0] != max_end_start]
    possible_endings = [pe[0] + pe[1] for pe in possible_endings if sum(pe) > len(
        paragraph) or (sum(pe) < len(paragraph) and paragraph[sum(pe)] == ' ')]
    end = (-1 if not len(possible_endings) else max(possible_endings))
    return end


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


# partition list a into k partitions
def partition_list_from_sentence_charactersum(a, k, result):
    # check degenerate conditions
    if k <= 1:
        return [result]
    if k >= len(a):
        return [[x] for x in result]
    # create a list of indexes to partition between, using the index on the
    # left of the partition to indicate where to partition
    # to start, roughly partition the array into equal groups of len(a)/k (note
    # that the last group may be a different size)
    partition_between = []
    for i in range(k-1):
        partition_between.append(int((i+1)*len(a)/k))
    # the ideal size for all partitions is the total height of the list divided
    # by the number of paritions
    # print(a)
    average_height = float(sum(a))/k
    best_score = None
    best_partitions = None
    count = 0
    no_improvements_count = 0
    # loop over possible partitionings
    while True:
        # partition the list
        partitions = []
        result_partitions = []

        index = 0
        for div in partition_between:
            # create partitions based on partition_between
            # print('!!!', index, div)
            partitions.append(a[index:div])
            result_partitions.append(result[index:div])
            index = div
        # append the last partition, which runs from the last partition divider
        # to the end of the list
        partitions.append(a[index:])
        result_partitions.append(result[index:])
        # evaluate the partitioning
        worst_height_diff = 0
        worst_partition_index = -1
        for p in partitions:
            # compare the partition height to the ideal partition height
            height_diff = average_height - sum(p)
            # if it's the worst partition we've seen, update the variables that
            # track that
            if abs(height_diff) > abs(worst_height_diff):
                worst_height_diff = height_diff
                worst_partition_index = partitions.index(p)
        # if the worst partition from this run is still better than anything
        # we saw in previous iterations, update our best-ever variables
        if best_score is None or abs(worst_height_diff) < best_score:
            best_score = abs(worst_height_diff)
            best_partitions = result_partitions
            no_improvements_count = 0
        else:
            no_improvements_count += 1
        # decide if we're done: if all our partition heights are ideal, or if
        # we haven't seen improvement in >5 iterations, or we've tried 100
        # different partitionings
        # the criteria to exit are important for getting a good result with
        # complex data, and changing them is a good way to experiment with getting
        # improved results
        if worst_height_diff == 0 or no_improvements_count > 5 or count > 100:
            return best_partitions
        count += 1
        # adjust the partitioning of the worst partition to move it closer to the
        # ideal size. the overall goal is to take the worst partition and adjust
        # its size to try and make its height closer to the ideal. generally, if
        # the worst partition is too big, we want to shrink the worst partition
        # by moving one of its ends into the smaller of the two neighboring
        # partitions. if the worst partition is too small, we want to grow the
        # partition by expanding the partition towards the larger of the two
        # neighboring partitions
        if worst_partition_index == 0:  # the worst partition is the first one
            if worst_height_diff < 0:
                # partition too big, so make it smaller
                partition_between[0] -= 1
            else:
                # partition too small, so make it bigger
                partition_between[0] += 1
        # the worst partition is the last one
        elif worst_partition_index == len(partitions)-1:
            if worst_height_diff < 0:
                # partition too small, so make it bigger
                partition_between[-1] += 1
            else:
                # partition too big, so make it smaller
                partition_between[-1] -= 1
        else:  # the worst partition is in the middle somewhere
            left_bound = worst_partition_index - 1  # the divider before the partition
            right_bound = worst_partition_index  # the divider after the partition
            if worst_height_diff < 0:  # partition too big, so make it smaller
                # the partition on the left is bigger than the one on the right, so make the one on the right bigger
                if sum(partitions[worst_partition_index-1]) > sum(partitions[worst_partition_index+1]):
                    partition_between[right_bound] -= 1
                else:  # the partition on the left is smaller than the one on the right, so make the one on the left bigger
                    partition_between[left_bound] += 1
            else:  # partition too small, make it bigger
                # the partition on the left is bigger than the one on the right, so make the one on the left smaller
                if sum(partitions[worst_partition_index-1]) > sum(partitions[worst_partition_index+1]):
                    partition_between[left_bound] -= 1
                else:  # the partition on the left is smaller than the one on the right, so make the one on the right smaller
                    partition_between[right_bound] += 1


# partition list a into k partitions
def partition_list(a, k):
    # check degenerate conditions
    if k <= 1:
        return [a]
    if k >= len(a):
        return [[x] for x in a]
    # create a list of indexes to partition between, using the index on the
    # left of the partition to indicate where to partition
    # to start, roughly partition the array into equal groups of len(a)/k (note
    # that the last group may be a different size)
    partition_between = []
    for i in range(k-1):
        partition_between.append((i+1)*len(a)/k)
    # the ideal size for all partitions is the total height of the list divided
    # by the number of paritions
    average_height = float(sum(a))/k
    best_score = None
    best_partitions = None
    count = 0
    no_improvements_count = 0
    # loop over possible partitionings
    while True:
        # partition the list
        partitions = []
        index = 0
        for div in partition_between:
            # create partitions based on partition_between
            partitions.append(a[index:div])
            index = div
        # append the last partition, which runs from the last partition divider
        # to the end of the list
        partitions.append(a[index:])
        # evaluate the partitioning
        worst_height_diff = 0
        worst_partition_index = -1
        for p in partitions:
            # compare the partition height to the ideal partition height
            height_diff = average_height - sum(p)
            # if it's the worst partition we've seen, update the variables that
            # track that
            if abs(height_diff) > abs(worst_height_diff):
                worst_height_diff = height_diff
                worst_partition_index = partitions.index(p)
        # if the worst partition from this run is still better than anything
        # we saw in previous iterations, update our best-ever variables
        if best_score is None or abs(worst_height_diff) < best_score:
            best_score = abs(worst_height_diff)
            best_partitions = partitions
            no_improvements_count = 0
        else:
            no_improvements_count += 1
        # decide if we're done: if all our partition heights are ideal, or if
        # we haven't seen improvement in >5 iterations, or we've tried 100
        # different partitionings
        # the criteria to exit are important for getting a good result with
        # complex data, and changing them is a good way to experiment with getting
        # improved results
        if worst_height_diff == 0 or no_improvements_count > 5 or count > 100:
            return best_partitions
        count += 1
        # adjust the partitioning of the worst partition to move it closer to the
        # ideal size. the overall goal is to take the worst partition and adjust
        # its size to try and make its height closer to the ideal. generally, if
        # the worst partition is too big, we want to shrink the worst partition
        # by moving one of its ends into the smaller of the two neighboring
        # partitions. if the worst partition is too small, we want to grow the
        # partition by expanding the partition towards the larger of the two
        # neighboring partitions
        if worst_partition_index == 0:  # the worst partition is the first one
            if worst_height_diff < 0:
                # partition too big, so make it smaller
                partition_between[0] -= 1
            else:
                # partition too small, so make it bigger
                partition_between[0] += 1
        # the worst partition is the last one
        elif worst_partition_index == len(partitions)-1:
            if worst_height_diff < 0:
                # partition too small, so make it bigger
                partition_between[-1] += 1
            else:
                # partition too big, so make it smaller
                partition_between[-1] -= 1
        else:  # the worst partition is in the middle somewhere
            left_bound = worst_partition_index - 1  # the divider before the partition
            right_bound = worst_partition_index  # the divider after the partition
            if worst_height_diff < 0:  # partition too big, so make it smaller
                # the partition on the left is bigger than the one on the right, so make the one on the right bigger
                if sum(partitions[worst_partition_index-1]) > sum(partitions[worst_partition_index+1]):
                    partition_between[right_bound] -= 1
                else:  # the partition on the left is smaller than the one on the right, so make the one on the left bigger
                    partition_between[left_bound] += 1
            else:  # partition too small, make it bigger
                # the partition on the left is bigger than the one on the right, so make the one on the left smaller
                if sum(partitions[worst_partition_index-1]) > sum(partitions[worst_partition_index+1]):
                    partition_between[left_bound] -= 1
                else:  # the partition on the left is smaller than the one on the right, so make the one on the right smaller
                    partition_between[right_bound] += 1


def print_best_partition(a, k):
    # simple function to partition a list and print info
    print('    Partitioning {0} into {1} partitions'.format(a, k))
    p = partition_list(a, k)
    print('    The best partitioning is {0}\n    With heights {1}\n'.format(
        p, map(sum, p)))


def split_comment2scene(comment, scene_words_limit):

    stences_list = find_sentences(comment)
    # print('--',stences_list)
    amount = [len(i) for i in stences_list]
    # print('---',amount)
    # scene_no=sum(amount) /250+1
    chunks = int(sum(amount)/scene_words_limit) + 1
    # print('---0', chunks)
    # print('---0', chunks)

    sentence_chunks = partition_list_from_sentence_charactersum(
        amount, chunks, stences_list)
    for scene in sentence_chunks:
        scene_content = ' '.join(scene)
        # the while loop will leave a trailing space,
        scene_content = scene_content.strip()
        # so the trailing whitespace must be dealt with
        # before or after the while loop
        while '  ' in scene_content:
            scene_content = scene_content.replace('  ', ' ')
    return sentence_chunks


resentencesp = re.compile('([,﹒﹔﹖﹗．；。！？]["’”」』]{0,2}|：(?=["‘“「『]{1,2}|$))')


def splitsentence(sentence):
    s = sentence
    slist = []
    for i in resentencesp.split(s):
        if resentencesp.match(i) and slist:
            slist[-1] += i
        elif i:
            slist.append(i)
    return slist

# import doctest


SEPARATOR = r'@'
RE_SENTENCE = re.compile(
    r'(\S.+?[.!?])(?=\s+|$)|(\S.+?)(?=[\n]|$)', re.UNICODE)
AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)\s(\w)', re.UNICODE)
AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)\s(\w)', re.UNICODE)
UNDO_AB_SENIOR = re.compile(
    r'([A-Z][a-z]{1,2}\.)' + SEPARATOR + r'(\w)', re.UNICODE)
UNDO_AB_ACRONYM = re.compile(
    r'(\.[a-zA-Z]\.)' + SEPARATOR + r'(\w)', re.UNICODE)


def replace_with_separator(text, separator, regexs):
    replacement = r"\1" + separator + r"\2"
    result = text
    for regex in regexs:
        result = regex.sub(replacement, result)
    return result


def split_sentence(text, best=True):
    """@NLP Utils
    基于正则的分句
    Examples:
        >>> txt = '玄德幼时，与乡中小儿戏于树下。曰：“我为天子，当乘此车盖。”'
        >>> for s in split_sentence(txt):
        ...     print(s)
        玄德幼时，与乡中小儿戏于树下。
        曰：“我为天子，当乘此车盖。”
    References: https://github.com/hankcs/HanLP/blob/master/hanlp/utils/rules.py
    """

    text = re.sub(r'([。！？?])([^”’])', r"\1\n\2", text)
    text = re.sub(r'(\.{6})([^”’])', r"\1\n\2", text)
    text = re.sub(r'(…{2})([^”’])', r"\1\n\2", text)
    text = re.sub(r'([。！？?][”’])([^，。！？?])', r'\1\n\2', text)
    for chunk in text.split("\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if not best:
            yield chunk
            continue
        processed = replace_with_separator(
            chunk, SEPARATOR, [AB_SENIOR, AB_ACRONYM])
        for sentence in RE_SENTENCE.finditer(processed):
            sentence = replace_with_separator(
                sentence.group(), r" ", [UNDO_AB_SENIOR, UNDO_AB_ACRONYM])
            yield sentence


def long_cjk_text2paragraph_budouX(text, text_len, count, lang):
    parser = budoux.load_default_japanese_parser()
    if lang in ['zh', 'jp', 'kr']:
        text_len = text_len/2
        # 由于text_len实际上是word个数，但中文是没有空格的，英文词的个数相当于2倍
        results = parser.parse(text)
        words = spliteKeyWord_zh(text)
        print('budoux：', results)
    else:
        # 都是用句号分割的 但我要逗号也分开
        # results = tokenize.sent_tokenize(text)
        # print('nltk: ',results)
        rawresults = splitsentence(text)
        words = spliteKeyWord_en(text)

        results = []
        print('raw results;', rawresults)
        for r in rawresults:
            if len(r.split(' ')) > text_len:
                print('this line is too loog', r)
                wrapper = textwrap.TextWrapper(
                    width=text_len, break_long_words=False, replace_whitespace=False)
                text = wrapper.wrap(text=r)
                for t in text:
                    print('add line break', t)
                    results.append(t+' ')
            else:
                results.append(r)

    if count:
        chunks = count
    else:
        chunks = int(len(words)/text_len) + 1
    print('分成几段', len(words), chunks)

    chunked_list = list()
    if len(results) < chunks:
        chunk_size = 1
    else:
        chunk_size = int(len(results)/chunks)+1
    print('每段几句话', chunk_size)

    for i in range(0, len(results), chunk_size):
        chunked_list.append(results[i:i+chunk_size])
    final = []
    for r in chunked_list:
        if len(''.join(r))>5:
            final.append(''.join(r))
    return final


def longtext2paragraph(text, text_len, lang, count):

    if lang in ['zh', 'jp', 'kr']:

        return long_cjk_text2paragraph_budouX(text, text_len, count, lang)

    else:

        return long_cjk_text2paragraph_budouX(text, text_len, count, lang)


'''
Takses a string of text and breaks it up into a list of paragraphs.
@str: the string to be broken up
'''


def long_en_text2paragraph(str, text_len, count):
    if count:
        chunks = count
    else:
        chunks = int(len(str)/text_len) + 1
    print('分成几段', len(str), chunks)

    chunked_list = list()
    chunk_size = int(len(str.split(' '))/chunks)+1
    print('meiduanjijuhua', chunk_size)

    punctuation_list = ['.', '!', '?']
    WORDS_PER_PARAGRAPH = chunk_size
    words = str.split(' ')  # string text seperated into words
    paragraphs = []  # list of paragraphs
    npars = 0  # number of paragraphs created
    iter = 1  # word iteration number (starts at 1 for modulo math)
    offset = 0  # word offset for modulo
    pcount = 0  # punctuation count
    pflag = False  # punctuation flag
    cflag = False  # continuation flag
    new_par = True  # new paragraph flag

    # determine if wall of text contains any of the punctuation characters
    for p in punctuation_list:
        pf = p in str
        if pf:
            pcount += 1

    # pcount > 0 means punctuation characters found. assert punctuation flag
    if pcount > 0:
        pflag = True

    # iterate over the words in the wall of text
    for word in words:
        if new_par:  # create a new paragraph entry in the paragraph list
            paragraphs.append('>' + word)  # '>' adds quotation block on reddit
            new_par = False
        else:  # append to current paragraph
            paragraphs[npars] += ' ' + word

        # this condition detects if the word iter has covered enough words to contitute a new paragraph.
        # the offset is used to make up for longer paragraphs created by contiunuing sentance boundaries.
        if (iter % WORDS_PER_PARAGRAPH) == 0:
            if pflag:  # punctuation is present
                punc_count = 0

                for punc in punctuation_list:  # determine if current word contains punctuation.
                    punc_count += word.find(punc)

                if punc_count > (-len(punctuation_list)):  # word contains punctuation
                    npars += 1
                    new_par = True
                    iter += 1
                    #offset = 0
                else:  # word contains no punctuation. assert continuation flag to keep adding words to paragraph.
                    iter += 1
                    cflag = True
            else:  # no punctuation detected, seperate just on word boundaries of size WORDS_PER_PARAGRAPH
                npars += 1
                new_par = True
                iter += 1
        else:
            iter += 1
            if cflag:  # continuation flag asserted
                # offset += 1 #increase offset
                punc_count = 0

                for punc in punctuation_list:
                    punc_count += word.find(punc)

                if punc_count > (-len(punctuation_list)):  # word contains punctuation
                    npars += 1
                    new_par = True
                    iter += 1
                    cflag = False

    return paragraphs


def video_to_all_frames(input_loc, output_loc):
    """Function to extract frames from input video file
    and save them as separate frames in an output directory.
    Args:
        input_loc: Input video file.
        output_loc: Output directory to save the frames.
    Returns:
        None
    """
    IMAGE_FILES = []

    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.

        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        IMAGE_FILES.append(output_loc + "/%#05d.jpg" % (count+1))
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print("Done extracting frames.\n%d frames extracted" % count)
            print("It took %d seconds forconversion." % (time_end-time_start))
            break
    return IMAGE_FILES


def video_to_key_frames(input_loc, output_loc):
    pass


def text_ass2video(textcontent, setting, context, post_id, videopath, postvideodir):
    # split text to para
    lang = langid.classify(textcontent)[0]
    scenes = longtext2paragraph(textcontent, 25, lang, None)
    audio_list = []
    total_length = 0
    lip_video_template = random.choice(['marry', 'obama', 'nadella', 'mcstay'])
    if lip_video_template in ['marry']:
        accent_name='MAYA'
    else:
        accent_name='JUDGE'    
    if not postvideodir.endswith(os.sep):
        postvideodir = postvideodir+os.sep
    subs = pysubs2.load("assets/ace/ass/in.ass", encoding="utf-8")    
    for count, scene in enumerate(scenes):
        lines = split_str_into_newlines(
            scene, './assets/igiari/Galmuri11.ttf', 350)
        scene = TextCorrectorbeforeTTS(scene)

        post_selftext_scene_audiopath = tts_choice(scene, accent_name,postvideodir,count,'ibm',lang)   
        audio_list.append(post_selftext_scene_audiopath)
        voice_file = eyed3.load(post_selftext_scene_audiopath)
        secs_float = voice_file.info.time_secs
        total_length = total_length+secs_float
        e1 = SSAEvent()
        if count ==0:
            e1.start = pysubs2.make_time(s=total_length-secs_float)
        else:
            e1.start = pysubs2.make_time(s=total_length-secs_float)+1000

        e1.end = pysubs2.make_time(s=total_length)+1000
        e1.style='Romaji'
        e1.text = scene
        subs.append(e1)
    subs.save(postvideodir+post_id+'.ass')
    print('generation base ass done')
    asspath=postvideodir+post_id+'.ass'
    dirname = os.path.dirname(os.path.abspath(asspath))

    # io = Ass(dirname+os.sep+post_id+'-1.ass',dirname+os.sep+post_id+'.ass')
    # meta, styles, lines = io.get_data()
    # # Generating lines
    # CU = ColorUtility(lines)
    # for line in lines:
    #     # if line.styleref.alignment >= 7:
    #     print(line.styleref.alignment)
    #     if line.styleref.alignment >= 7:
    #         romaji(io,line, line.copy())
    #     elif line.styleref.alignment >= 4:
    #         kanji(io,line, line.copy())
    #     else:
    #         sub(io,line, line.copy(),CU)
    # print('finish kararoke style')
    # io.save()

    audio_clip = []
    for audio_file in audio_list:
        audio = AudioFileClip(audio_file)
        segments = AudioClip(make_frame = lambda t: 0, duration=0.25)
        audio_clip.append(segments)
        audio_clip.append(audio)
    final_audio = concatenate_audioclips(audio_clip)
    final_audio = final_audio.fx(afx.audio_normalize)
    # final_audio.write_audiofile('res.mp3')

    lip_video_clip = VideoFileClip(
        'assets/ace/lipvideotemplate/'+lip_video_template+'.mp4')
    lip_video_template_length = lip_video_clip.duration
    if total_length < lip_video_template_length:
        lip_video=lip_video_clip.set_duration(total_length+len(scenes)*1)
    else:
        num_clips_required = int(total_length/lip_video_template_length)+1        

        lip_video = vfx.make_loopable(lip_video_clip, cross=num_clips_required).subclip(0, total_length+len(scenes)*1)
    # bg_ace = ImageClip("assets/ace/GreatAceAttorney_HoldIt_072621.jpg")
    # final = CompositeVideoClip([bg_ace, lip_video.set_position((568, 208))]).set_duration(total_length)
    # has infinite duration

    final = lip_video.set_audio(final_audio)
    final.write_videofile(dirname+os.sep+post_id+'-tmp.mp4', codec='libx264', audio_codec='aac')
    print('dirname',dirname)


    video = ffmpeg.input(dirname+os.sep+post_id+'-tmp.mp4')
    audio = video.audio
    videopath=postvideodir+post_id+'.mp4'
    ffmpeg.concat(video.filter("subtitles", postvideodir+post_id+'.ass'), audio, v=1, a=1).output(videopath,acodec='aac',vcodec='libx264', ).run(overwrite_output=True)

    # if os.path.exists(dirname+os.sep+post_id+'.ass'):
    #     print('ass sub is ',dirname+os.sep+post_id+'.ass')
    #     sub = SubtitlesClip(postvideodir+post_id+'.ass',translation_subtitle_generator())
    # print('sub wrong???????/')
    # # ffmpeg -i 1.mp4 -vf ass=1.ass 2.mp4
    # final = CompositeVideoClip([final, sub])
    # final.write_videofile(videopath, codec='libx264', audio_codec='aac')
    return videopath


def default_subtitle_generator():
    return lambda txt: TextClip(
        txt.replace('\n', ''),
        font='assets/font/PingFang.ttf',
        fontsize=45,
        stroke_width=2,
        color='white',
        bg_color='#00000066'
    )


def translation_subtitle_generator():
    return lambda txt: TextClip(
        txt.replace('\n', ''),
        font='assets/igiari/Galmuri11.ttf',
        fontsize=36,
        color='white',
        bg_color='#00000066'
    )
def romaji(io,line, l):
    # Setting up a delay, we will use it as duration time of the leadin and leadout effects
    delay = 300
    # Setting up offset variables, we will use them for the \move in leadin and leadout effects
    off_x = 35
    off_y = 15

    star = Shape.star(5, 4, 10)
    # Leadin Effect
    for syl in Utils.all_non_empty(line.syls):
        l.layer = 0

        l.start_time = (
            line.start_time + 25 * syl.i - delay - 80
        )  # Remove 80 to start_time to let leadin finish a little bit earlier than the main effect of the first syllable
        l.end_time = line.start_time + syl.start_time
        l.dur = l.end_time - l.start_time

        l.text = (
            "{\\an5\\move(%.3f,%.3f,%.3f,%.3f,0,%d)\\blur2\\t(0,%d,\\blur0)\\fad(%d,0)}%s"
            % (
                syl.center + math.cos(syl.i / 2) * off_x,
                syl.middle + math.sin(syl.i / 4) * off_y,
                syl.center,
                syl.middle,
                delay,
                delay,
                delay,
                syl.text,
            )
        )

        io.write_line(l)

    # Main Effect
    for syl in Utils.all_non_empty(line.syls):
        l.layer = 1

        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.end_time + 100
        l.dur = l.end_time - l.start_time

        c1 = "&H81F4FF&"
        c3 = "&H199AAA&"
        # Change color if inline_fx is m1
        if syl.inline_fx == "m1":
            c1 = "&H8282FF&"
            c3 = "&H191AAA&"

        on_inline_effect_2 = ""
        # Apply rotation if inline_fx is m2
        if syl.inline_fx == "m2":
            on_inline_effect_2 = "\\t(0,%d,\\frz%.3f)\\t(%d,%d,\\frz0)" % (
                l.dur / 4,
                random.uniform(-40, 40),
                l.dur / 4,
                l.dur,
            )

        l.text = (
            "{\\an5\\pos(%.3f,%.3f)%s\\t(0,80,\\fscx105\\fscy105\\1c%s\\3c%s)\\t(80,%d,\\fscx100\\fscy100\\1c%s\\3c%s)}%s"
            % (
                syl.center,
                syl.middle,
                on_inline_effect_2,
                c1,
                c3,
                l.dur - 80,
                line.styleref.color1,
                line.styleref.color3,
                syl.text,
            )
        )
        io.write_line(l)

        # Animating star shape that jumps over the syllables
        # Jump-in to the first syl
        jump_height = 18
        if syl.i == 0:
            FU = FrameUtility(line.start_time - line.leadin / 2, line.start_time)
            for s, e, i, n in FU:
                l.start_time = s
                l.end_time = e
                frame_pct = i / n

                x = syl.center - syl.width * (1 - frame_pct)
                y = syl.top - math.sin(frame_pct * math.pi) * jump_height

                alpha = 255
                alpha += FU.add(0, syl.duration, -255)
                alpha = Convert.alpha_dec_to_ass(int(alpha))

                l.text = (
                    "{\\alpha%s\\pos(%.3f,%.3f)\\bord1\\blur1\\1c%s\\3c%s\\p1}%s"
                    % (alpha, x, y, c1, c3, star)
                )
                io.write_line(l)

        # Jump to the next syl or to the end of line
        jump_width = (
            line.syls[syl.i + 1].center - syl.center
            if syl.i != len(line.syls) - 1
            else syl.width
        )
        FU = FrameUtility(
            line.start_time + syl.start_time, line.start_time + syl.end_time
        )
        for s, e, i, n in FU:
            l.start_time = s
            l.end_time = e
            frame_pct = i / n

            x = syl.center + frame_pct * jump_width
            y = syl.top - math.sin(frame_pct * math.pi) * jump_height

            alpha = 0
            # Last jump should fade-out
            if syl.i == len(line.syls) - 1:
                alpha += FU.add(0, syl.duration, 255)
            alpha = Convert.alpha_dec_to_ass(int(alpha))

            l.text = "{\\alpha%s\\pos(%.3f,%.3f)\\bord1\\blur1\\1c%s\\3c%s\\p1}%s" % (
                alpha,
                x,
                y,
                c1,
                c3,
                star,
            )
            io.write_line(l)

    # Leadout Effect
    for syl in Utils.all_non_empty(line.syls):
        l.layer = 0

        l.start_time = line.start_time + syl.end_time + 100
        l.end_time = line.end_time - 25 * (len(line.syls) - syl.i) + delay + 100
        l.dur = l.end_time - l.start_time

        l.text = (
            "{\\an5\\move(%.3f,%.3f,%.3f,%.3f,%d,%d)\\t(%d,%d,\\blur2)\\fad(0,%d)}%s"
            % (
                syl.center,
                syl.middle,
                syl.center + math.cos(syl.i / 2) * off_x,
                syl.middle + math.sin(syl.i / 4) * off_y,
                l.dur - delay,
                l.dur,
                l.dur - delay,
                l.dur,
                delay,
                syl.text,
            )
        )
        print('writing====',l.text)

        io.write_line(l)


def kanji(io,line, l):
    # Setting up a delay, we will use it as duration time of the leadin and leadout effects
    delay = 300
    # Setting up offset variables, we will use them for the \move in leadin and leadout effects
    off_x = 35
    off_y = 15

    # Leadin Effect
    for syl in Utils.all_non_empty(line.syls):
        l.layer = 0

        l.start_time = (
            line.start_time + 25 * syl.i - delay - 80
        )  # Remove 80 to start_time to let leadin finish a little bit earlier than the main effect of the first syllable
        l.end_time = line.start_time + syl.start_time
        l.dur = l.end_time - l.start_time

        l.text = (
            "{\\an5\\move(%.3f,%.3f,%.3f,%.3f,0,%d)\\blur2\\t(0,%d,\\blur0)\\fad(%d,0)}%s"
            % (
                syl.center + math.cos(syl.i / 2) * off_x,
                syl.middle + math.sin(syl.i / 4) * off_y,
                syl.center,
                syl.middle,
                delay,
                delay,
                delay,
                syl.text,
            )
        )

        io.write_line(l)

    # Main Effect
    for syl in Utils.all_non_empty(line.syls):
        l.layer = 1

        l.start_time = line.start_time + syl.start_time
        l.end_time = line.start_time + syl.end_time + 100
        l.dur = l.end_time - l.start_time

        c1 = "&H81F4FF&"
        c3 = "&H199AAA&"
        # Change color if effect field is m1
        if line.effect == "m1":
            c1 = "&H8282FF&"
            c3 = "&H191AAA&"

        on_inline_effect_2 = ""
        # Apply rotation if effect field is m2
        if line.effect == "m2":
            on_inline_effect_2 = "\\t(0,%d,\\frz%.3f)\\t(%d,%d,\\frz0)" % (
                l.dur / 4,
                random.uniform(-40, 40),
                l.dur / 4,
                l.dur,
            )

        l.text = (
            "{\\an5\\pos(%.3f,%.3f)%s\\t(0,80,\\fscx105\\fscy105\\1c%s\\3c%s)\\t(80,%d,\\fscx100\\fscy100\\1c%s\\3c%s)}%s"
            % (
                syl.center,
                syl.middle,
                on_inline_effect_2,
                c1,
                c3,
                l.dur - 80,
                line.styleref.color1,
                line.styleref.color3,
                syl.text,
            )
        )

        io.write_line(l)

    # Leadout Effect
    for syl in Utils.all_non_empty(line.syls):
        l.layer = 0

        l.start_time = line.start_time + syl.end_time + 100
        l.end_time = line.end_time - 25 * (len(line.syls) - syl.i) + delay + 100
        l.dur = l.end_time - l.start_time

        l.text = (
            "{\\an5\\move(%.3f,%.3f,%.3f,%.3f,%d,%d)\\t(%d,%d,\\blur2)\\fad(0,%d)}%s"
            % (
                syl.center,
                syl.middle,
                syl.center + math.cos(syl.i / 2) * off_x,
                syl.middle + math.sin(syl.i / 4) * off_y,
                l.dur - delay,
                l.dur,
                l.dur - delay,
                l.dur,
                delay,
                syl.text,
            )
        )

        io.write_line(l)


def sub(io,line, l,CU):
    # Translation Effect
    l.layer = 0

    l.start_time = line.start_time - line.leadin / 2
    l.end_time = line.end_time + line.leadout / 2
    l.dur = l.end_time - l.start_time

    # Getting interpolated color changes (notice that we do that only after having set up all the times, that's important)
    colors = CU.get_color_change(l)

    # Base text
    l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(%d,%d)}%s" % (
        line.center,
        line.middle,
        line.leadin / 2,
        line.leadout / 2,
        line.text,
    )
    io.write_line(l)

    # Random clipped text colorated
    l.layer = 1
    for i in range(1, int(line.width / 80)):
        x_clip = line.left + random.uniform(0, line.width)
        y_clip = line.top - 5

        clip = (
            x_clip,
            y_clip,
            x_clip + random.uniform(10, 30),
            y_clip + line.height + 10,
        )

        l.text = "{\\an5\\pos(%.3f,%.3f)\\fad(%d,%d)\\clip(%d,%d,%d,%d)%s}%s" % (
            line.center,
            line.middle,
            line.leadin / 2,
            line.leadout / 2,
            clip[0],
            clip[1],
            clip[2],
            clip[3],
            colors,
            line.text,
        )
        io.write_line(l)



from sentence_splitter import SentenceSplitter, split_text_into_sentences

#
# Object interface
#
splitter = SentenceSplitter(language='en')
print(splitter.split(text='This is a paragraph. It contains several sentences. "But why," you ask?'))
# ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']

#
# Functional interface
#
print(split_text_into_sentences(
    text='This is a paragraph. It contains several sentences. "But why," you ask?',
    language='en'
))
# ['This is a paragraph.', 'It contains several sentences.', '"But why," you ask?']