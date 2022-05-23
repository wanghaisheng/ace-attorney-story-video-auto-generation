import os
from posixpath import sep
import re
import requests
from bs4 import BeautifulSoup
from sympy import N
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import nltk
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException, WebDriverException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
import glob
import platform
import random
import pickle

from .utils import *
from .constants import *
from .language_detect import prediction
from json import loads, dumps
import langid

#https://lazypy.ro/tts/

# Make the Pool of workers


def getwebdriver_chrome():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_experimental_option('useAutomationExtension', False)

    prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    if url_ok('www.google.com'):
        pass
    else:
        chrome_options.add_argument("proxy-server=socks5://127.0.0.1:1080")
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])

    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    if 'Windows' in platform.system():
        web_driver = webdriver.Chrome(executable_path="assets/driver/chromedriver.exe", chrome_options=chrome_options)
        # print('windows system chrome driver ',web_driver)

    else:
        web_driver = webdriver.Chrome(executable_path="assets/driver/chromedriver", chrome_options=chrome_options)
    return web_driver


def tiny_file_rename(newname, folder_of_download, time_to_wait=60):
    finished = is_download_finished(folder_of_download)

    while not finished:

        finished = is_download_finished(folder_of_download)
        # print(' download finished?',finished)
        time.sleep(0.2)

        if finished == True:
            break

    if os.path.exists(folder_of_download+os.sep+'narration.mp3'):
        filename = max([f for f in os.listdir(folder_of_download)],
                       key=lambda xa:   os.path.getctime(os.path.join(folder_of_download, xa)))
        print("file is there",filename,'rename ',os.path.join(folder_of_download, filename),'to',os.path.join(folder_of_download, newname))

        if os.path.exists(os.path.join(folder_of_download, newname)):
            os.remove(os.path.join(folder_of_download, newname))
            os.rename(os.path.join(folder_of_download, filename),
                    os.path.join(folder_of_download, newname))            
        else:
            os.rename(os.path.join(folder_of_download, filename),
                    os.path.join(folder_of_download, newname))
        print('narration.mp3 renamed to',os.path.join(folder_of_download, newname))
    return os.path.join(folder_of_download, newname)

def is_download_finished(temp_folder):
    firefox_temp_file = sorted(Path(temp_folder).glob('*.part'))
    chrome_temp_file = sorted(Path(temp_folder).glob('*.crdownload'))
    downloaded_files = sorted(Path(temp_folder).glob('*.*'))

    if (len(firefox_temp_file) == 0) and \
       (len(chrome_temp_file) == 0) and \
       (len(downloaded_files) >= 1):
        return True
    else:
        return False


proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080'
}


#preferred voice name map 
male_languages = { 
  'da' : 'Mads',
  'nl' : 'Ruben',
  'en' : 'Joey',
  'fr' : 'Mathieu',
  'de' : 'Hans',
  'it' : 'Giorgio',
  'is' : 'Karl',
  'no' : 'Liv',
  'pt' : 'Cristiano',
  'ru' : 'Maxim',
  'es' : 'Enrique',
  'sv' : 'Astrid',
  'tr' : 'Filiz',
  'ro' : 'Carmen',
  'ja' : 'Mizuki',
  'pl' : 'Jacek',
}

female_languages = { 
  'da' : 'Naja',
  'nl' : 'Lotte',
  'en' : 'Joanna',
  'fr' : 'Céline',
  'de' : 'Marlene',
  'it' : 'Carla',
  'is' : 'Dóra',
  'no' : 'Liv',
  'pt' : 'Inês',
  'ru' : 'Tatyana',
  'es' : 'Conchita',
  'sv' : 'Astrid',
  'tr' : 'Filiz',
  'ro' : 'Carmen',
  'ja' : 'Mizuki',
  'pl' : 'Ewa',

}

def tts_choice(text, character_name,ttsdir,index,tool,lang):
    character_idlist=[]
    polly_mapping = {"PHOENIX":'Justin',
"EDGEWORTH":'Geraint',
"GODOT":'Joey',
"FRANZISKA":'Salli',
"JUDGE":'Brian',
"LARRY":'Joey',
"MAYA":'Raveena',
"KARMA":'Brian',
"PAYNE":'Geraint',
"MAGGEY":'Aditi',
"PEARL":'Joanna',
"LOTTA":'Emma',
"GUMSHOE":'Matthew',
"GROSSBERG":'Matthew',
"APOLLO":'Russell',
"KLAVIER":'Brian',
"MIA":'Aria',
"WILL":'Russell',
"OLDBAG":'Aria',
"REDD":'Russell'}
    # tts text language detect and engine select
    if text =='' or text is None:
        return None
    if not lang in supported_languages:
        lang =langid.classify(text)[0]     
    short_lang= lang
    # 非常规语言暂时不支持 也可能是检测出错
    if not short_lang in supported_languages:
        return None
    lang =supported_languages[lang]

    if not lang in ["English","Arabic","Chinese","Dutch","French","German","Italian","Japanese","Korean","Portuguese","Spanish","Danish","Icelandic","Norwegian","Polish","Romanian","Russian","Swedish","Turkish","Welsh","Basque","Catalan","Czech","Esperanto","Finnish","Galician","Greek","Hindi","Hungarian","Indonesian","Thai"]:
        print(lang,' is not supported yet')
        return None
    if tool=='polly':
        tool_accents = [x for x in ttsvoicelist if x['tool'] == 'polly']
        tool_lang_accents = [x for x in tool_accents if x['lang'] == lang]        
        if not lang in ["English","Arabic","Chinese","Dutch","French","German","Italian","Japanese","Korean","Portuguese","Spanish","Danish","Icelandic","Norwegian","Polish","Romanian","Russian","Swedish","Turkish","Welsh"]:
            print(lang,' not supported in amazon polly')
            # tts_oddcast()
            return None
        else:                
            accent_name = get_polly_tts_accent(lang,short_lang,text,character_name,tool_accents,tool_lang_accents)
            ttsfile = streamlabs_polly_tts(text, accent_name,ttsdir,index) 
            return ttsfile
    elif tool=='ibm':
        tool_accents = [x for x in ttsvoicelist if x['tool'] == 'ibm']
        tool_lang_accents = [x for x in tool_accents if x['lang'] == lang]        
        print('accent candidates=',tool_lang_accents)
        print('character name After',character_name)
        if not lang in ["English","Arabic","Chinese","Dutch","French","German","Italian","Japanese","Korean","Portuguese","Spanish"]:
            print(lang,' not supported in ibm waston')
            tool_accents = [x for x in ttsvoicelist if x['tool'] == 'polly']
            tool_lang_accents = [x for x in tool_accents if x['lang'] == lang]                 
            accent_name = get_polly_tts_accent(lang,short_lang,text,character_name,tool_accents,tool_lang_accents)
            ttsfile = streamlabs_polly_tts(text, accent_name,ttsdir,index) 
            return ttsfile
        else:
            accent_name = get_ibm_tts_accent(lang,short_lang,text,character_name,tool_accents,tool_lang_accents)
            ttsfile = lazypy_ibm_tts(text, accent_name,ttsdir,index,short_lang)                
            if ttsfile is not None and os.path.exists(ttsfile) and  os.path.getsize(ttsfile)>0:

                pass
            else:
                tool_accents = [x for x in ttsvoicelist if x['tool'] == 'polly']
                tool_lang_accents = [x for x in tool_accents if x['lang'] == lang]                 
                accent_name = get_polly_tts_accent(lang,short_lang,text,character_name,tool_accents,tool_lang_accents)
                ttsfile = streamlabs_polly_tts(text, accent_name,ttsdir,index) 
            return ttsfile
    else:
        print('tts tool ',tool,' not supported yet')        
        return None
def get_ibm_tts_accent(lang,short_lang,text,character_name,tool_accents,tool_lang_accents):
    chracter2accent={}


    if os.path.exists('assets/chracter2accent_ibm.pkl'):
        with open('assets/chracter2accent_ibm.pkl', 'rb') as f:
            chracter2accent = pickle.load(f)

    if short_lang in ['jp','it','pt'] and character_name.upper() in ace_male_character_list:
        character_name= random.choice(ace_female_character_list)   
    if short_lang in ['ar'] and character_name.upper() in ace_female_character_list:
        character_name= random.choice(ace_male_character_list)         
    print('character name After',character_name)
        
    if not character_name.upper() in chracter2accent:

        if character_name.upper() in ace_female_character_list:

            ibm_lang_accents_female =[x for x in tool_lang_accents if x['gender'] == 'female']
            print('candidates accents ibm female:',ibm_lang_accents_female,'\n',tool_lang_accents)
            if ibm_lang_accents_female:

                accent_name =random.choice(ibm_lang_accents_female)['accent']
            else:
                randomlist=[x for x in AllowedVoiceList_female_ibm if x['lang'] == lang]

                accent_name =random.choice(randomlist)['accent']

        elif  character_name.upper() in ace_male_character_list:
            ibm_lang_accents_male =[x for x in tool_lang_accents if x['gender'] == 'male']
            print('candidates accents ibm male:',ibm_lang_accents_male,'\n',tool_lang_accents)
            if ibm_lang_accents_male:
                accent_name =random.choice(ibm_lang_accents_male)['accent']
            else:
                randomlist=[x for x in AllowedVoiceList_male_ibm if x['lang'] == lang]

                accent_name =random.choice(randomlist)['accent']
        else:
            accent_name =random.choice(tool_lang_accents)['accent']
            print('===========1,accent_name',accent_name)
        chracter2accent[character_name]=accent_name
    else:
        accent_name=chracter2accent[character_name.upper()]
    with open('assets/chracter2accent_ibm.pkl', 'wb') as f:
        pickle.dump(chracter2accent, f)       
    print('you have choose accent',accent_name,' for lang ',lang) 
    return accent_name
    
def get_polly_tts_accent(lang,short_lang,text,character_name,tool_accents,tool_lang_accents):  

    chracter2accent={}


    if os.path.exists('assets/chracter2accent_polly.pkl'):
        with open('assets/chracter2accent_polly.pkl', 'rb') as f:
            chracter2accent = pickle.load(f)
    accent_name=''

    print('character name before',short_lang,short_lang in ['zh','kr','tr','ar','ro','no','sv'])
    if short_lang in ['zh','kr','ar','ro','no','sv'] and character_name.upper() in ace_male_character_list:
        print('there is only 1 voice for zh,kr,tr,ar,ro,no,sv ',)
        character_name= random.choice(ace_female_character_list)   
    if short_lang in ['tr'] and character_name.upper() in ace_female_character_list:
        character_name= random.choice(ace_male_character_list)        
    if not character_name.upper() in chracter2accent:
        print('character name After',character_name)
        if character_name.upper() in ace_female_character_list:
            polly_lang_accents_female =[x for x in tool_lang_accents if x['gender'] == 'female']
            print('candidates accents polly female:',polly_lang_accents_female,'\n',tool_lang_accents)

            accent_name =random.choice(polly_lang_accents_female)['accent']

        elif  character_name.upper() in ace_male_character_list:
            polly_lang_accents_male =[x for x in tool_lang_accents if x['gender'] == 'male']
            print('candidates accents polly male:',polly_lang_accents_male,'\n',tool_lang_accents)
            accent_name =random.choice(polly_lang_accents_male)['accent']
        else:
            accent_name =random.choice(tool_lang_accents)['accent']
            print('===========1,accent_name',accent_name)
        chracter2accent[character_name]=accent_name
    else:
        accent_name=chracter2accent[character_name.upper()]
    with open('assets/chracter2accent_polly.pkl', 'wb') as f:
        pickle.dump(chracter2accent, f)             
    return accent_name
def lazypy_ibm_tts(text, character_name,ttsdir,index,short_lang):
    TTSMP3_URL = "https://lazypy.ro/tts/proxy.php"
    

    print('======which language text is to tts=====\n',text,'\n',character_name)
    voice = ''
    if not character_name or character_name=="":
        print('character_name is null')
    else:
        if character_name in ["Allison" ,"Emily" ,"Henry" ,"Kevin","Lisa" ,"Michael" ,"Olivia" ]:
            voice ='en'+'-'+'US'.upper()+'_'+character_name+'V3Voice'
        elif character_name in ["Charlotte","James","Kate"]:
            voice ='en'+'-'+'GB'.upper()+'_'+character_name+'V3Voice'
        elif character_name in ["LiNa","WangWei","ZhangJing"]:
            voice ='zh'+'-'+'CN'.upper()+'_'+character_name+'Voice'
        elif character_name in ["Sofia"]:
            voice ='es'+'-'+'US'.upper()+'_'+character_name+'V3Voice'         
        elif character_name in ["Enrique","Laura"]:
            voice ='es'+'-'+'Enrique'.upper()+'_'+character_name+'V3Voice'
        else:
            if short_lang=='en':
                voice =short_lang+'-'+short_lang.upper()+'_'+random.choice(["Allison" ,"Emily" ,"Henry" ,"Kevin","Lisa" ,"Michael" ,"Olivia" ])+'V3Voice'
            elif short_lang=='fr':
                voice =short_lang+'-'+short_lang.upper()+'_'+random.choice(["Nicolas" ,"Renee" ])+'V3Voice'
                
    form_data = {
        "text": text,
        "voice": voice,
        "service": "IBM Watson"
    }
    print('===choose voice name====',voice)
    try:
        if url_ok(TTSMP3_URL):
            r = requests.post(TTSMP3_URL, form_data)

        else:

            r = requests.post(TTSMP3_URL, form_data, proxies=proxies)
        
        print('ibm tts status',r.status_code)

        if r.status_code == 200:
            json = r.json()
            try:
                url = json["speak_url"]
                success = json["success"]
                print('ibm mp3 url',url,type(success),success)

                if success==True:

                    mp3_file = requests.get(url, proxies=proxies)
                    outputdir = ttsdir
                    outputfilepath = outputdir+os.sep+str(index)+'.mp3'
                    if os.path.exists(outputdir):

                        print('sound directory exists', outputdir)
                    else:
                        os.makedirs(outputdir, exist_ok=True)
                        print('create sound directory', outputdir)
                    # print('tts', index, '----', outputfilepath)

                    with open(outputfilepath, "wb") as out_file:
                        out_file.write(mp3_file.content)

                        print('ibm tts ok', outputfilepath)
                    return outputfilepath
                else:
                    print('ibm plan b is not implemented yet')
                    return None
            # return mp3_file.content
            except:
                print('status code 200,but reponse result is not ok')
                return None
    except:
        print('we can not access lazypy.ro ibm waston tts,pls choose another tts tool')
        print('to do implement')
        return None        
def tts_oddcast(text, accent_name,ttsdir,index):

    # if not lang in ["English","Arabic","Chinese","Dutch","French","German","Italian","Japanese","Korean","Portuguese","Spanish","Danish","Icelandic","Norwegian","Polish","Romanian","Russian","Swedish","Turkish","Welsh","Basque","Catalan","Czech","Esperanto","Finnish","Galician","Greek","Hindi","Hungarian","Indonesian","Thai"]:
    return ''
def ttsmp3_polly_tts(text, accent_name,ttsdir,index):
    # print('tts',text)
# Add a break
# Mary had a little lamb <break time="1s"/> Whose fleece was white as snow.
# Emphasizing words
# I already told you I <emphasis level="strong">really like </emphasis> that person. 
    TTSMP3_URL = "https://ttsmp3.com/makemp3_new.php"

    print('======which language text is to tts=====\n',text,'\n',accent_name)
    if not accent_name or accent_name=="":
        accent_name = 'Brian'
    form_data = {
        "msg": text,
        "lang": accent_name,
        "source": "ttsmp3"
    }
    print('===choose voice name====',accent_name)
    if url_ok(TTSMP3_URL):
        r = requests.post(TTSMP3_URL, form_data)

    else:

        r = requests.post(TTSMP3_URL, form_data, proxies=proxies)    
    if r.status_code == 200:
        # print(r.status_code)
        json = r.json()
        # print(json)
        try:
            url = json["URL"]
            filename = json["MP3"]
            mp3_file = requests.get(url, proxies=proxies)

            outputdir = ttsdir
            outputfilepath = outputdir+os.sep+str(index)+'.mp3'
            if os.path.exists(outputdir):

                print('sound directory exists', outputdir)
            else:
                os.makedirs(outputdir, exist_ok=True)
                print('create sound directory', outputdir)
            # print('tts', index, '----', outputfilepath)

            with open(outputfilepath, "wb") as out_file:
                out_file.write(mp3_file.content)

                print('ttsmp3 ok', outputfilepath)
            return outputfilepath
        # return mp3_file.content
        except:
            print('https://ttsmp3.com  polly tts not accessible,pls choose another tts tool')
            outputfilepath = streamlabs_polly_tts(text, accent_name,ttsdir,index)
            print('ttsmp3 result',outputfilepath)
            if not outputfilepath ==None and os.path.exists(outputfilepath):

                return outputfilepath
            else:
                return synthentic_audio_ttstool(text,accent_name,index,ttsdir)    
    else:
        print('https://ttsmp3.com polly tts not accessible,status not 200 pls choose another tts tool')
        outputfilepath = streamlabs_polly_tts(text, accent_name,ttsdir,index)
        if os.path.exists(outputfilepath):

            return outputfilepath
        else:
            return synthentic_audio_ttstool(text,accent_name,index,ttsdir)    

def streamlabs_polly_tts(text, accent_name,ttsdir,index):
    outputdir = ttsdir
    mp3outputfilepath = outputdir+os.sep+str(index)+'.mp3'    
    if accent_name in ['Ayanda','Aria']:
        accent_name ='Emma'
    temp = {'text': text, 'voice': accent_name}
    json_dump = dumps(temp)
    print('===streamlabs tts start==',accent_name,'====',text)
    if ttsdir is None:
        directory = './'

    try:
        url = 'https://streamlabs.com/polly/speak'
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

        if url_ok(url):
            r = requests.post(url, data=json_dump, headers=headers)

        else:

            r = requests.post(url, data=json_dump, headers=headers,proxies=proxies)

        # print('streamlab results',r.text)
        if r.status_code == 200:
            resp = requests.get(loads(r.text)['speak_url'],proxies=proxies)
            if resp.status_code == 200:
                with open(mp3outputfilepath, 'wb') as f:
                    f.write(resp.content)
                print('streamlabs polly  tts file for ',str(index),'is done')
                if os.path.exists(mp3outputfilepath) and  os.path.getsize(mp3outputfilepath)>0:

                    return mp3outputfilepath
                else:
                    return streamelements_polly_tts(text, accent_name, index, ttsdir)
        else:
            print(f'Could not download clip: Response-{r.status_code}')
            print('last try steamelements')
            return streamelements_polly_tts(text, accent_name, index, ttsdir)
        # print(f'Could not download clip: Response-{r.status_code}')
        # return streamelements_polly_tts(text, accent_name, index, ttsdir)
    except Exception as e:
        # print(e)
        print('last try streamelements')

        return streamelements_polly_tts(text, accent_name, index, ttsdir)

def streamelements_polly_tts(text, accent_name, index, ttsdir):
    outputdir = ttsdir
    mp3outputfilepath = outputdir+os.sep+str(index)+'.mp3'  

    if url_ok("https://streamelements.com"):
        tts = requests.get("https://api.streamelements.com/kappa/v2/speech?voice="+accent_name+"&text=%s" % text)

    else:

        tts = requests.get("https://api.streamelements.com/kappa/v2/speech?voice="+accent_name+"&text=%s" % text,proxies=proxies)


    with open(mp3outputfilepath, "wb") as f:
        f.write(tts.content)
    if os.path.exists(mp3outputfilepath) and  os.path.getsize(mp3outputfilepath)>0:

        return mp3outputfilepath
    else:
        outputfilepath = ttsmp3_polly_tts(text, accent_name,ttsdir,index)
        print('ttsmp3 result',outputfilepath)
        if not outputfilepath ==None and os.path.exists(outputfilepath):

            return outputfilepath
        else:
            return synthentic_audio_ttstool(text,accent_name,index,ttsdir)       
def synthentic_audio_ttstool(text, character_name, index, ttsdir):
    # dir = r'D:\Download\audio-visual\auto_video-jigsaw\tts\readaloud'
    try:
        web_driver = getwebdriver_chrome()
        print('====initiliaze webdriver=====')
        url = 'https://ttstool.com/'
        out = web_driver.get(url)
        # print('========',out)
        # options = out.find_element_by_xpath("//select")
        # print("-----------\n",web_driver.page_source)

        wait = WebDriverWait(web_driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[1]/table[1]/tbody/tr[2]/td[2]/select/option[4]")))
        while not web_driver.find_element_by_xpath("//table[1]/tbody/tr[1]/td[2]/select"):
            print('page not show')
            time.sleep(0.1)
            finished = web_driver.find_element_by_xpath(
                "//table[1]/tbody/tr[1]/td[2]/select")
            if finished == True:
                break

        select_tool = Select(web_driver.find_element_by_xpath(
            "//table[1]/tbody/tr[1]/td[2]/select"))

        # select by visible text
        print('====choose amazon or microsoft=====')

        select_tool.select_by_visible_text('Amazon')

        while not web_driver.find_element_by_xpath("//table[1]/tbody/tr[2]/td[2]/select") :
                print('page not show correctly')
                time.sleep(0.1)
                finished= web_driver.find_element_by_xpath("//table[1]/tbody/tr[2]/td[2]/select")
                if finished ==True:
                    break

        time.sleep(0.2)
        select_language = Select(web_driver.find_element_by_xpath(
            " /html/body/div[1]/table[1]/tbody/tr[2]/td[2]/select"))
        # /html/body/div[1]/table[1]/tbody/tr[2]/td[2]/select
        print('====select voice=====')
        # select_language.select_by_visible_text('English')
        select_language.select_by_value('English')
        wait = WebDriverWait(web_driver, 10)
        download = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[1]/i[1]')))
        # print('2222',download)
        character_idlist=[]
        AllowedVoiceList_en=["Justin","Salli","Ivy","Kendra","Matthew","Joanna",
        "Russell", "Nicole", "Amy", "Brian", "Emma", "Aditi", "Raveena",
                            "Aria", "Joey", "Kimberly"]

        mapping = {"PHOENIX":'Russell',
    "EDGEWORTH":'Geraint',
    "GODOT":'Joey',
    "FRANZISKA":'Salli',
    "JUDGE":'Brian',
    "LARRY":'Joey',
    "MAYA":'Raveena',
    "KARMA":'Brian',
    "PAYNE":'Geraint',
    "MAGGEY":'Aditi',
    "PEARL":'Joanna',
    "LOTTA":'Emma',
    "GUMSHOE":'Matthew',
    "GROSSBERG":'Matthew',
    "APOLLO":'Russell',
    "KLAVIER":'Brian',
    "MIA":'Aria',
    "WILL":'Russell',
    "OLDBAG":'Ayanda',
    "REDD":'Russell'}
        options ={"Nicole":"0",
            "Russell":"1",
            "Amy":"2",
            "Brian":"3",
            "Emma":"4",
            "Raveena":"5",
            "Ivy":"6",
            "Joey":"7",
            "Justin":"8",
            "Kendra":"9",
            "Kimberly":"10",
            "Salli":"11",
            "Geraint":"12"}
        if character_name not in character_idlist:
            character_idlist.append(character_name)
        accent_name=mapping[character_name.upper()]
        if accent_name in options:
            option="3"
        else:
            option=options[accent_name] 

        if download:
            select_voice = Select(web_driver.find_element_by_xpath(
                "//table[2]/tbody/tr[1]/td/div[2]/div[2]/select[1]"))

            select_voice.select_by_value(option)
            # print('146,',select_voice)
        inputElement = web_driver.find_element_by_xpath(
            "//table[2]/tbody/tr[1]/td/div[2]/div[3]/textarea")
        text = TextCorrectorbeforeTTS(text)
        inputElement.send_keys(text)
        ttsdirabsolute = os.getcwd()+os.sep+ttsdir
        tmp_outputdir = ttsdirabsolute+os.sep+'tmp'
        # print('-----',ttsdir)
        if os.path.exists(tmp_outputdir):

            # print('tmp sound directory exists',tmp_outputdir)

            files = glob.glob(tmp_outputdir+os.sep+'*')
            if files:
                for f in files:
                    print('remove tmp previous files', f)
                    os.remove(f)
        else:
            os.makedirs(tmp_outputdir, exist_ok=True)
        print('create tmp sound directory',tmp_outputdir)
        # Initializing the Chrome webdriver with the options

        # Setting Chrome to trust downloads
        web_driver.command_executor._commands["send_command"] = (
            "POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior', 'params': {
            'behavior': 'allow', 'downloadPath': tmp_outputdir}}
        command_result = web_driver.execute("send_command", params)
        print('----\n',command_result)

        # Click on the button and wait for 10 seconds

        web_driver.find_element_by_xpath(
            "/html/body/div[1]/div/div[1]/i[2]").click()
        time.sleep(2)
        # outputdir = ttsdirabsolute+os.sep+str(index)
        # if os.path.exists(outputdir):
        #     pass
        #     # print('sound directory exists',outputdir)
        # else:
        #     os.makedirs(outputdir, exist_ok=True)
        #     # print('create sound directory',outputdir)
        # # print('chongmingming')
        newfile =tiny_file_rename(str(index)+'.mp3', tmp_outputdir)
        web_driver.close()
        web_driver.quit()
        return newfile
    except:
        print('plan b tts service')
        # outputfilepath =ttsmp3_polly_tts(text, character_name,ttsdir,index)
        # return outputfilepath
# synthentic_audio_ttstool('','',1,dir)

# real person syn
# https://vo.codes/

def waitFor(maxSecond, runFunction, param):
    while maxSecond:
        try:
            return runFunction(param)
        except:
            time.sleep(0.5)
            maxSecond -= 0.5
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from ibm_watson import TextToSpeechV1
# def ibm_api_tts():
#     url = "https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/51d2629a-5c70-4a8e-ae64-06ac0b089c91"
#     apikey = "GiFLTDMBeRg0MQeKck3qEKP2JzwcaYaODgxP9LQqqTGg"

#     authenticator = IAMAuthenticator(apikey)
#     tts = TextToSpeechV1(authenticator=authenticator)
#     tts.set_service_url(url)

#     with open('tts/speech.mp3', 'wb') as audio_file:
#         res = tts.synthesize('P.O.V you just sold a N F T for over $65,000 & earned your professors entire salary after finishing college', accept='audio/mp3', voice = 'en-US_AllisonV3Voice').get_result()
#         audio_file.write(res.content)