polyglot_available = True
from charset_normalizer import detect
from google.cloud import translate_v2 as translate

try:
    from polyglot.detect import Detector
    from polyglot.detect.base import UnknownLanguage
    from polyglot.text import Text
except Exception as e:
    print("Warning! Polyglot couldn't start: " + str(e))
    polyglot_available = False
from textblob import TextBlob
from collections import Counter
import random
import os
from .utils import url_ok
from .language_detect import prediction
import langid
class Analizer:
    def __init__(self):
        self.official_api = True
        self.language_counter = Counter()
        if url_ok('http://www.google.com'):
            print('network is fine,there is no need for proxy ')
            try:
                self.translate_client = translate.Client()
            except Exception as e:
                print('Warning! Translator couldn\'t be initialized, fallbacking to unofficial translation engine: ' + str(e))
                self.official_api = False            
        else:
            print('google can not be access ')        
            self.official_api = False            

    def get_sentiment_offline(self,text,fmodel,language):
        if len(os.getenv('oe_bypass_sentiment', '')) > 0:
            return 'N'
        try:
            print('==========sentiment analysis==========')
            # language = prediction(text,fmodel)
            if language =='' or language is None:   
                language =langid.classify(text)[0]

            print('language detecting result:',language,'\n original:',text)
            # if not language =='en':

            self.language_counter.update({language: 1})
            # print(self.language_counter)
            
            if (language == 'English' or language =='en'):
                return self.proccess_eng(text)

            if (language == 'google'):
                return self.process_google(text)
            
            try:
                return self.process_poly(text)
            except ZeroDivisionError:
                return 'N'
            except Exception as e:
                # print(e)
                return self.process_google(text)
        except Exception as e:
            # print(e)
            return self.proccess_eng(text)
        


    def get_sentiment(self, text):
        if len(os.getenv('oe_bypass_sentiment', '')) > 0:
            return 'N'
        try:
            try:
                if (polyglot_available):
                    # detector = Detector(text)
                    # language = detector.language.code
                    language = prediction(text)
                    # print('language detecting result:',language,'\n original:',text)
                    # if not language =='en':
                    #     language =langid.classify(text)[0]                    
                else:
                    language = self.detect_language_heuristic(text)
            except UnknownLanguage:
                language = self.detect_language_heuristic(text)

            self.language_counter.update({language: 1})
            # print(self.language_counter)
            
            if (language == 'en'):
                return self.proccess_eng(text)

            if (language == 'google'):
                return self.process_google(text)
            
            try:
                return self.process_poly(text)
            except ZeroDivisionError:
                return 'N'
            except Exception as e:
                # print(e)
                return self.process_google(text)
        except Exception as e:
            # print(e)
            return self.proccess_eng(text)
        

    def process_google(self, text):
        if (self.official_api):
            result = self.translate_client.translate(text, target_language="en")
            return self.proccess_eng(result["translatedText"])
        else: 
            return self.proccess_eng(str(TextBlob(text).translate()))
        

    
    def proccess_eng(self, text):

        blob = TextBlob(text)
        if (blob.sentiment.polarity > 0.05):
            return '+'
        if (blob.sentiment.polarity < -0.05):
            return '-'
        return 'N'

    def process_poly(self, text):
        poly_text = Text(text)
        if (poly_text.polarity > 0.35):
            return '+'
        # If polarity is -1 there isn't enough information to determine if it's negative therefore we introduce randomness
        if (poly_text.polarity < -0.35 and (poly_text.polarity > -1 or random.random() > 0.25)):
            return '-'
        return 'N'

    def detect_language_heuristic(self, text):
        if (len(text) <=2):
            language = 'en'
        else:
            language = 'google'
        return language
