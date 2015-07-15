__author__ = 'Ryan Ahn'

from collections import OrderedDict
from os import listdir, path

import fileio
import ngram


def ngram_analysis(n, contents):
    ngram_dictionary = OrderedDict()

    for i in range(0, len(contents) - n):
        word = ""

        for j in range(0, n):
            if contents[i+j] != "\n":
                word += contents[i+j]

        if word in ngram_dictionary:
            ngram_dictionary[word] += 1
        else:
            ngram_dictionary[word] = 1

    return ngram_dictionary


def wordgram_analyze(contents):

    wordgram_dictionary = OrderedDict()

    i = 0

    while i < len(contents):
        word = ""
        jmp_count = 1

        for j in range(1, len(contents) - i):
            if contents[i+j] == " " or contents[i+j] == "\r" or contents[i+j] == "\n":
                jmp_count = j
                break
            else:
                word += contents[i+j]
        if len(word) < 1:
            i += jmp_count
            continue
        if word in wordgram_dictionary:
            wordgram_dictionary[word] += 1
        else:
            wordgram_dictionary[word] = 1

        i += jmp_count

    return wordgram_dictionary


def wordgram_map(dirpath):
    file_list = listdir(dirpath)
    dict_map = []

    for file in file_list:
        extension = path.splitext(file)[1]
        if extension != ".txt":
            continue
        file = dirpath + file
        file_contents = fileio.read_file(file)
        file_dict = ngram.wordgram_analyze(file_contents)
        dict_map.append(file_dict)

    return dict_map

