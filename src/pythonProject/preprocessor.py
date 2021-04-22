"""
This is a pre-processor which will clean tweets and create a bag of words before they are used in the CHkS algorithm
"""

#Importing package
import json
import pandas as pd
import re
import preprocessor as p
import string
from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from textblob import TextBlob
import numpy as np
import scipy

def remove_non_ascii(string):
    """
    Removes non_ascii characters
    :param string:
    :return:
    """
    if string != string:
        return "404"
    return "".join(i for i in string if ord(i) < 128)


def clean_text(text):
    """
    Cleans text by lowering the text and stripping white space, as well as removing links and tags
    :param text:
    :return:
    """
    text = p.clean(text)
    if(not text):
        return "404"

    #makes everything lower case
    text = text.lower()

    #removes non ascii values, just in case
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    #removes trailing white space
    text = text.strip()

    #removing small words that make it through
    i = 0
    for x in text:
        if x != " ":
            i = i + 1
        if x == " " and i < 4:
            return "404"
    if len(text) < 4:
        return "404"

    return text


def stopwords_removed(text):
    """
    Removes stopwords and words with little meaning from the text
    :param text:
    :return:
    """
    #Defining stopwords
    stopWords = set(stopwords.words('english'))
    tokenised = word_tokenize(text)

    #Words which make it through the filter are added to this list
    wordsFiltered = []
    for w in tokenised:
        if w not in stopWords:
            wordsFiltered.append(w)

    return wordsFiltered


def lemmatizer(text):
    """
    Lemmatizes words by morphing them to their most basic form
    :param text:
    :return:
    """
    lemmatizer = WordNetLemmatizer()

    #Iterate through words and lemmatize
    i = 0
    for word in text:
        text[i] = lemmatizer.lemmatize(word)
        i = i + 1
    return text


def pos_tagger(text):
    """
    Detects different parts of senetences and only returns nouns and verbs
    :param text:
    :return:
    """
    string_pos = ""

    #Iterate through text
    for x in text:
        string_pos += x + " "

    #Perform POS tagging
    result = TextBlob(string_pos)

    #Filter out everything apart from nouns and verbs
    a = []
    i = 0
    for x in result.tags:
        if result.tags[i][1] == 'NN':
            a.append(x[0])
        if result.tags[i][1] == 'VB':
            a.append(x[0])

    #If nothing in a then error
    if(not a):
        return "404"
    return a


def string_converter(aList):
    """
    Converts a list to a string
    :param aList:
    :return:
    """

    str1 = ""
    i = 0
    for x in aList:
        str1 += x + " "
        i = i + 1
    return str1


def bag_of_words(string, frequency):
    """
    Creates a vector out of a string of words
    :param string:
    :return:
    """
    vectoriser = CountVectorizer(strip_accents= 'ascii',lowercase = True, min_df = frequency)
    x = vectoriser.fit_transform(string)

    return x, vectoriser




#Main function
def preprocessor(text, frequency):
    """
    Cleans and prepares data, so that the best possible sample of words can be vectorised
    :param text:
    :return:
    """

    #Define string
    str2 = []

    #Iterate through text
    for x in text:
        #Remove non ascii characters
        non_asc = remove_non_ascii(x)
        if non_asc == "404":
            continue

        #Removing stopwords
        stopped = stopwords_removed(non_asc)

        #Lemmatise words
        lemmatized_words = lemmatizer(stopped)

        #POS tagging
        pos_tagged = pos_tagger(lemmatized_words)
        if pos_tagged == "404":
            continue

        #Convert list to string
        str1 = string_converter(pos_tagged)

        #Add string to overall list
        str2 += [str1]

    #Bag of words vectoriser
    bow, vector = bag_of_words(str2, frequency)


    #print(vector.get_feature_names())
    vocab = vector.vocabulary_

    #Get bag of words shapes
    bow.maxprint = bow.count_nonzero()
    bow_shape = bow.shape
    bow = str(bow)
    bow = bow.translate(str.maketrans('','',string.punctuation))

    # Open file
    f = open("/Users/niallcollinson/Desktop/bow.txt", "w")
    f.write(bow)

    return vocab, bow_shape





