#import neessary libraries

import os 
import sys
from pathlib import Path
import codecs
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer

path_to_instagram = "./NLP/instagram/"
path_to_patents = "./NLP/patents/"
path_to_stackoverflow ="./NLP/stackoverflow/"

# Necessary downloads
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

ps = PorterStemmer()
#From instagram 
# with os.scandir(path_to_instagram) as entries:
#     count = 0 
#     for entry in entries:
#         if entry.is_file():
#             count += 1
#             current_file = codecs.open(entry, "r", encoding = "latin-1")
#             #This will print out the outputt
#             txt = current_file.read()
#             print(txt)
#             print("=================++++++++++++++++++=============\n")
#             tokenized_words = word_tokenize(txt)
#             print(tokenized_words)
#             print("=================" + str(count) + "=============\n")
#             stemming_words = []
#             #Performing stemming on the file and printing out stemming results
#             for i in range(len(tokenized_words)):
#                 stemming_words.append(ps.stem(tokenized_words[i]))
#             print(stemming_words)
#             print("================================================\n")

            #Now, tokenized_words contains the tokens before stemming and stemming_words contains the tokens that had stemming applied
            #Next thing we have to do is to use visualization to compare between the two list of tokens 


# #Sentence Segmentation 
# with os.scandir(path_to_instagram) as entries:
#     count = 0 
#     for entry in entries:
#         if entry.is_file():
#             count += 1
#             current_file = codecs.open(entry, "r", encoding = "latin-1")
#             #This will print out the outputt
#             txt = current_file.read()

#             tokenized_sentences = sent_tokenize(txt)
#             print(tokenized_sentences)
#             print("=================" + str(count) + "=============\n")

#POS Tagging 

#From patents

#From stackoverflow 
with os.scandir(path_to_stackoverflow) as entries:
    count = 0 
    for entry in entries:
        if entry.is_file():
            count += 1
            current_file = codecs.open(entry, "r", encoding = "latin-1")
            #This will print out the outputt
            txt = current_file.read()
            print(txt)
            print("=================++++++++++++++++++=============\n")
            tokenized_words = word_tokenize(txt)
            print(tokenized_words)
            print("=================" + str(count) + "=============\n")
            stemming_words = []
            #Performing stemming on the file and printing out stemming results
            for i in range(len(tokenized_words)):
                stemming_words.append(ps.stem(tokenized_words[i]))
            print(stemming_words)
            print("================================================\n")