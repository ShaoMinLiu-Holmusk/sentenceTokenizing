
import pandas as pd
import seaborn as sns

from itertools import chain
from pathlib import Path

import re

import os
os.environ["DB_PATH"]='../../../db.json'
from neuroblu_postgres.databaseIO import pgIO

import spacy

nlp=spacy.load("en_core_sci_scibert")
def tokeniseUsingSciSpacy(sentence):
    doc = nlp(sentence)
    cleaned_data=list(item.text for item in doc.sents)
    return cleaned_data

from tqdm import tqdm
tqdm().pandas()

responSectionTextsDf_nltk_break = Path('responSectionTextsDf_nltk_break.csv')
responSectionTextsDf_nltk_break = pd.read_csv(responSectionTextsDf_nltk_break)
responSectionTextsDf_nltk_break = responSectionTextsDf_nltk_break[
    responSectionTextsDf_nltk_break.nltk_break.str.count(' ') > 250
    ].copy()


responSectionTextsDf_nltk_break['sciSpacy_break'] = responSectionTextsDf_nltk_break\
    .nltk_break\
    .progress_apply(tokeniseUsingSciSpacy)

responSectionTextsDf_nltk_break = responSectionTextsDf_nltk_break.explode('sciSpacy_break')
responSectionTextsDf_nltk_break['SciSpacedSentenceIdex'] = responSectionTextsDf_nltk_break\
    .groupby(['patient_encounter_id', 'header', 'nltk_break_order'])\
    .sciSpacy_break\
    .transform(lambda series: range(1,len(series)+1))

responSectionTextsDf_nltk_break.to_csv('responSectionTextsDf_nltkSciSpacy_break.csv', 
                                       index=False)