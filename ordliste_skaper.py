#!/usr/bin/env python3

import os
import io
import sys
from nltk import tokenize

VERSION = "1.0"

# Currently not clear if API-key is needed
API_KEY = ''

def sentence_lister(f):
    chars = ['\\N', '-', '.' , '?', '!', ',', '(', ')', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    sentences = tokenize.sent_tokenize(f.read().replace('\\N', ''))
    print(type(sentences))
    return sentences


def word_lister(fw, fs):
    
    words = {""}
    chars = ['\\N', '-', '.' , '?', '!', ',', '(', ')', '"', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    temp = fw.read().replace(chars[0], '\n')
    temps = fs.read().replace(chars[0], '\n')
    
    for char in chars:
        temp = temp.replace(char, '')
        #temps = temps.replace(char, '')
    for word in temp.split():
        words.add(word)
    
    sentences = tokenize.sent_tokenize(temps)
    words = list(words)
    words = [s.replace("\\N", '') for s in words]
    words = [s for s in words if len(s)>=3 ]
    
    return words, sentences

def file_opener(fn):
    with open(fn,'r') as f:
        return f

def write_to_file(word_list, sent_list):
    fw = 'ord_list_s1_e1.txt'
    sw = 'sent_list_s1_e1.txt'
    try:
        f = open(fw, 'r+')
        f1 = open(sw, 'r+')
    except IOError:
        f = open(fw, 'w')
        f1 = open(sw, 'w')
    
    f.writelines("{}\n".format(x) for x in word_list)
    f1.writelines("{}\n".format(x) for x in sent_list)


fn = 'sos-s1-e1.txt'
fnn = 'sos-s1-e1-kopi.txt'
if os.path.exists(fn):
    f = open(fn, 'r+')
    fs = open(fnn, 'r+')
    wl, sl = word_lister(f, fs)
    write_to_file(wl, sl)
else:
    f = open(fn, 'w')
    fs = open(fnn, 'w')
    wl, sl = word_lister(f, fs)
    write_to_file(wl, sl)
