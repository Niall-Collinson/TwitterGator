#Main file to contorl the program
from data_loader import data_loader
from preprocessor import preprocessor
from j_caller import j_caller
import pandas as pd
import json
import csv

def generate(size, query, time_request):
    """
    Generates the data, parses it and then gives what is feeded to the gui

    :return:
    """

    #Get data from elk stack transform to json
    data_loader(size, query, time_request)

    #Open the data that has just been queried to be processed
    f = open('data.json', )
    data = json.load(f)

    # Loading the data into a pandas data frame for easy processing
    df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')

    # Getting the tweets from the data from, ignoring other meta data
    if df.empty:
        terms = "No results to return"
        return terms

    text = df['_source.text']

    #Pre-process data and translates into bow
    vocab, bow_shape = preprocessor(text, 1)

    return vocab, bow_shape

def graph_generator(k_number, frequency, algo ):
    """
    Generates graph

    :param k_number:
    :param frequency:
    :param algo:
    :return:
    """

    #Opens json file
    f = open('data.json', )
    data = json.load(f)

    # Loading the data into a pandas data frame for easy processing
    df = pd.DataFrame.from_dict(pd.json_normalize(data), orient='columns')


    # Getting the tweets from the data from, ignoring other meta data
    if df.empty:
        terms = "No results to return"
        return terms

    text = df['_source.text']

    vocab, bow_shape = preprocessor(text, frequency)

    #Call chks to operate on the data
    j_caller(k_number, algo)

    dataset = pd.read_csv("/Users/niallcollinson/Desktop/CHkS_output.csv")


    #Converts data to acceptable readable format
    if dataset.size == 0:
        return "No results to return"

    vertices = []
    vertices.append("Vertices: ")
    for i in dataset["Vertices"]:
        vertices.append(i)

    terms = []

    for i in vocab:
        for j in vertices:
            if vocab[i] == j:
                terms.append(i)


    result = ""
    terms = str(terms)
    for i in terms:
        print(i)
        #if i != "{" and i != "}" and i != "[" and i != "]" and (i != r'\ ' and i+1 != "n") and i != ",":
        if i != "[" and i != "]" and i != "," and i != "'" and i != r'/':
            result = result + str(i)

    return result