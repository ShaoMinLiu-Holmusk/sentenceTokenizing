from nltk.tokenize import sent_tokenize
import re

def cleanNote(text:str):
    '''
    Given a clinician note, attempt to clean it by remove irrelevant 
    line breaks, characters that will affect sentence tokenization.
    '''
    pass

def sentenceTokenizer(
    paragraph:str,
    quickRun:bool=False,
    nltk:bool=True,
    scibert:bool=True,
):
    
    if quickRun:
        # turn off all tokenizer that takes too long to run
        scibert=False
        
    