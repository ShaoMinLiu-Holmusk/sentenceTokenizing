
import pandas as pd
import seaborn as sns

from itertools import chain
from pathlib import Path

import re

import os
os.environ["DB_PATH"]='../../db.json'
from neuroblu_postgres.databaseIO import pgIO

import spacy



nlp=spacy.load("en_core_sci_scibert")
def tokeniseUsingSciSpacy(sentence):
    doc = nlp(sentence)
    cleaned_data=list(item.text for item in doc.sents)
    return cleaned_data

from tqdm.notebook import tqdm
tqdm().pandas()


notesTableDfExploded = Path('notesTableDfExploded.csv')
notesTableDfExploded = pd.read_csv(notesTableDfExploded)
notesTableDfExplodedLong = notesTableDfExploded[notesTableDfExploded.postNLTK_tokenCnt>=250]


notesTableDfExplodedLong['SciSpaced'] = notesTableDfExplodedLong\
    .nltkCleanned\
    .progress_apply(tokeniseUsingSciSpacy)
    
notesTableDfExplodedLong = notesTableDfExplodedLong.explode('SciSpaced')
notesTableDfExplodedLong['SciSpacedSentenceIdex'] = notesTableDfExplodedLong\
    .groupby(['patient_encounter_id', 'sentenceIndex'])\
    .SciSpaced\
    .transform(lambda series: range(1,len(series)+1))

notesTableDfExplodedLong.to_csv('notesTableDfComnpleted.csv', 
                                index=False)