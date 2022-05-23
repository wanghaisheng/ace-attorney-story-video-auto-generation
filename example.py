# from renderer import render_comment_list
# from beans.comment import Comment
# import anim
from collections import Counter

from auto_motion_comic_video.anim import *
from auto_motion_comic_video.renderer import *
from auto_motion_comic_video.comment import *
from auto_motion_comic_video.ttstool import lazypy_ibm_tts
from auto_motion_comic_video.utils import *
comments = [
Comment(user_name = 'fowlraul', text_content='Its also absurd, disgusting, treasonous, dumb, stupid, lame, and totally not a surprise at all'),
Comment(user_name = 'coldstreamer59', text_content='Trump is a narcissistic traitor, a psycho'),
Comment(user_name = 'straygoat193', text_content='You are right Bernie He is a sick man and is using an international crisis to get the attention he so misses'),
Comment(user_name = 'newNull', text_content='Americans in name only Fuck the GOP!'),
Comment(user_name = 'wish1977', text_content='At a time when the country should be rallying around our president, Donald Trump seems to be rallying around his president or should I say dictator'),
Comment(user_name = 'dartie', text_content='Trump deserves prison'),
Comment(user_name = 'PURPLEPEE', text_content='Fuck Trump and Putin'),
Comment(user_name = 'cgilbertmc', text_content='and typical'),
Comment(user_name = 'Thatsayesfirsir', text_content='Yes it is Is the US now little Russia We like dictators now?'),
Comment(user_name = 'firemage22', text_content='Shower thought - Trump is Putin"s goldfish'),
Comment(user_name = 'BabylonianProstitue', text_content='Always nice to hear from Bernie His critiques are always sharp and his political instincts are top notch'),
Comment(user_name = 'Patient_Criticism231', text_content='Partners in crime Antichrist Man of lawlessness'),
Comment(user_name = 'Nonemous', text_content='Dont forget that he fully supported Xi Jipings solution to his Muslim problem: -china-detention-camp-xinjiang-2020-6'),
Comment(user_name = 'WhyWorryAboutThat', text_content='And said he might try being president for life like Xi Jinping, then tried it'),
Comment(user_name = 'calaquin', text_content='The fact that he can be re-elected tells me the system needs work'),
Comment(user_name = 'Namboman', text_content='> But what happens when the asshole in charge has an IQ not in the single digits? That"s why DeSantis scares the shit out of me'),
Comment(user_name = 'SaveTheDells', text_content='The general populace did not vote for Trump'),
Comment(user_name = 'Edge-master', text_content='Half? Dont know about that'),
Comment(user_name = 'hiverfrancis', text_content='And its crazy how many ethnic Chinese and non-US citizen Chinese who are anti CCP had praised him :'),
Comment(user_name = 'Snarfsicle', text_content='Trump is essentially the personification and amalgamation of the 7 Deadly Sins'),
Comment(user_name = 'Antishill_Artillery', text_content='Faster to say republican'),
Comment(user_name = 'Snarfsicle', text_content='I just meant that trump is a comically exponential level compared to the average Republican Though lack of empathy is very common throughout it seems for them'),
Comment(user_name = 'cmack', text_content='&#x200B;'),
Comment(user_name = 'dumbfuckmagee', text_content='I feel like they could get rid of "emotional" and it would still fit'),
Comment(user_name = 'OLightning', text_content='You do know this is his tactic to claim if he was still President then Russia would never have invaded Ukraine'),
Comment(user_name = 'Tasgall', text_content='I mean, obviously Hes been saying that about anything bad that happens during Biden term'),
Comment(user_name = 'sephkane', text_content='And that tells you all you need to know about the Christians that support him'),
Comment(user_name = 'Comfortable-Wrap-723', text_content='He is behaving like a Russian asset'),
Comment(user_name = 'Yertzi1234567', text_content='he has been russian asset for decades, just like moscow mitch, and the other gop'),
Comment(user_name = 'BaronVonStevie', text_content='we already took a bullet electing Trump, we dodged another by not reelecting him, but we need to be careful or gangrene will set in Because Trump will never stop trying to poison the country'),
Comment(user_name = 'whelmedoxen', text_content='I am pretty sure that was his plan too It was a Hail Mary that Trump did not get reelected And almost totally a result of his terrible handling of the random pandemic that struck'),
    # Comment(user_name = 'جالكسي', text_content='حاب أذكركم انه باقي كم يوم وينتهي عرض الطلب المسبق على جالكسي Z فليب', user_id="id2"),
    # Comment(user_name = 'd', text_content='Bonjout mâ fìlle. Coment ça-va'),
    # Comment(user_name = 'e', text_content='Türkiye Türkçesi, dil ailesi sınıflandırmasında, Doğu Avrupa, Orta Asya ve Sibirya’da konuşulan 30 kadar yaşayan dili kapsayan'),
    # Comment(user_name = 'f', text_content='б, г, ґ, д, ж, з, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ), ten vowels (а, е, є, и, і, ї, о, у, ю, я), and two semivowels (й/yot, and в'),
    # Comment(user_name = 'g', text_content='Hello OwO'),
    # Comment(user_name = 'h', text_content='Hello OwO'),
    # Comment(user_name = 'i', text_content='Hello OwO'),
    # Comment(user_name = 'j', text_content='Hello OwO'),
    # Comment(user_name = 'k', text_content='Hello OwO'),
    # Comment(user_name = 'l', text_content='Hello OwO'),
    # Comment(user_name = 'm', text_content='Hello OwO'),
    # Comment(user_name = 'n', text_content='Trump Calls Putin’s Ukraine Moves “Genius” Because He’s a Sick Man Who Hates Democracy'),
    Comment(user_name = 'o', text_content='《长征》第1集 The Long March 01震惊世界的二万五千里长征（唐国强/陈道明）【CCTV电视剧】Highlights：毛泽东针对奔袭湘江的作战命令会给数万红军带来的严重损失，连夜找“三人团”请示复议作战计划，李德不耐烦地指责毛泽东是在危言耸听。')
]  *  1
if os.path.exists('assets/chracter2accent_ibm.pkl'):
    os.remove('assets/chracter2accent_ibm.pkl')
if os.path.exists('assets/chracter2accent_polly.pkl'):
    os.remove('assets/chracter2accent_polly.pkl')
if os.path.exists('tts-tmp'):
    clear_folder('tts-tmp')

render_comment_list(comments,"hello.mp4","PWR",320,15,True,30,0,'ibm',20,20)

#def render_comment_list(comment_list: List[Comment], output_filename = 'hello.mp4', music_code = 'PWR',scene_line_character_limit=85,scene_character_limit=240,tts_enabled=True,db_lounder=30,tts_lag=1000,tts_tool='polly'):

# r = get_all_music_available()
# print(r)
# # counter = Counter()
# # counter={'a': 1, 'id1': 1, 'c': 1}
# utils.get_characters(counter)

# text='《长征》第1集 The Long March 01震惊世界的二万五千里长征（唐国强/陈道明）【CCTV电视剧】Highlights：毛泽东针对奔袭湘江的作战命令会给数万红军带来的严重损失，连夜找“三人团”请示复议作战计划，李德不耐烦地指责毛泽东是在危言耸听。'
# text ='we already took a bullet electing Trump, we dodged another by not reelecting him, but we need to be careful or gangrene will set in Because Trump will never stop trying to poison the country'
# lazypy_ibm_tts(text, 'Nicolas','.',0,'fr')
# print(split_comment2scene(text,45))
# print(format_line(text,45))
# ht0 = HarvestText()

text='《长征》第1集 The Long March 01震惊世界的二万五千里长征（唐国强/陈道明）,【CCTV电视剧】Highlights：毛泽东针对奔袭湘江的作战命令会给数万红军带来的严重损失，连夜找“三人团”请示复议作战计划，李德不耐烦地指责毛泽东是在危言耸听。'
# print('fenduanqian==',text)
# predicted_paras = ht0.cut_paragraphs(text, num_paras=3) 
# for i in predicted_paras:
#     print('duan==',i)

# English text has many clues, like spacing and hyphenation, that enable beautiful and legible line breaks. Some CJK languages lack these clues, and so are notoriously more difficult to process. Without a more careful approach, breaks can occur randomly and usually in the middle of a word. This is a long-standing issue with typography on the web and results in a degradation of readability.

# res = long_cjk_text2paragraph_budouX(text,50)
# print(res)
for  comment in comments:
    # text ='we already took a bullet electing Trump, we dodged another by not reelecting him, but we need to be careful or gangrene will set in Because Trump will never stop trying to poison the country'
# text='Türkiye Türkçesi, dil ailesi sınıflandırmasında, Doğu Avrupa, Orta Asya ve Sibirya’da konuşulan 30 kadar yaşayan dili kapsayan'
    print((comment.text_content,15,'','en'))
# print(splitsentence(text))
# r =format_line(text,85,'en')
# print(r)
# print(final)
# import budoux
# parser = budoux.load_default_japanese_parser()
# results = parser.parse(text)
# print(len(text))
# text_len=45
# chunks = int(len(text)/text_len) + 1        
# print(chunks)
# chunked_list = list()
# chunk_size = int(len(results)/chunks)+1
# for i in range(0, len(results), chunk_size):
#     chunked_list.append(results[i:i+chunk_size])

# for i in chunked_list:
#     print(i)
