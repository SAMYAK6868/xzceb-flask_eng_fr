import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
def englishtofrench(englishtext):
    '''translation from english to french'''
    frenchtext = language_translator.translate(text=englishtext,model_id='en-fr').get_result()
    return frenchtext["translations"][0]["translation"]

def frenchtoenglish(frenchtext):
    '''translation from french to english'''
    englishtext = language_translator.translate(text=frenchtext,model_id='fr-en').get_result()
    return englishtext["translations"][0]["translation"]