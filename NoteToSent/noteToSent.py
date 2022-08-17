from nltk.tokenize import sent_tokenize

import re
from itertools import chain

import spacy
from nltk.tokenize import sent_tokenize

spacyLoaded = [False,]
def tokeniseUsingSciSpacy(sentence):
    if not spacyLoaded[0]:
        nlp=spacy.load("en_core_sci_scibert")
        spacyLoaded[0]=True
        spacyLoaded.append(nlp)
    nlp = spacyLoaded[-1]
    
    doc = nlp(sentence)
    cleaned_data=list(item.text for item in doc.sents)
    return cleaned_data

def cleanNote(text:str):
    '''
    Given a clinician note, attempt to clean it by remove irrelevant 
    line breaks, characters that will affect sentence tokenization.
    '''
    text = re.sub(pattern=';',
                  repl="\n",
                  string=text)
    
    text = re.sub(pattern='[-_\s=+\r\n]{3,}',
                  repl="\n",
                  string=text)
    
    return text

def sentenceTokenizer(
    paragraph:str,
    quickRun:bool=False,
    splitNL:bool=True,
    nltk:bool=True,
    scibert:bool=True,
):
    
    if quickRun:
        # turn off all tokenizer that takes too long to run
        scibert=False
    sentences = [paragraph,]
        
    if splitNL:
        sentences = chain(*(sent.split('\n') for sent in sentences))
    if nltk:
        sentences = chain(*(sent_tokenize(sent) for sent in sentences))
    if scibert:
        sentences = chain(*(tokeniseUsingSciSpacy(sent) for sent in sentences))
    return list(sentences)