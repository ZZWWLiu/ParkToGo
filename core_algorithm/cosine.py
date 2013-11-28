# from __future__ import division
import re
from stemming import porter2
import math
import json
import os
# from operator import itemgetter

from math import log
from math import sqrt

# {"282820": {"state": "FL", "amenity": ["Dump Station", "Picnic Shelter"]}}

def tokenize(text):
    """
    Take a string and split it into tokens on word boundaries.
      
    A token is defined to be one or more alphanumeric characters,
    underscores, or apostrophes.  Remove all other punctuation, whitespace, and
    empty tokens.  Do case-folding to make everything lowercase. This function
    should return a list of the tokens in the input string.
    """
    tokens = re.findall("[\w']+", text.lower())
    return [porter2.stem(token) for token in tokens]

def read_data(filename):
    """
    purpose: read all tweets from the json file.
    parameter: 
        filename - the path of json file in your local computer 
    return: a list containing all raw tweets each of which has the data structure of dictionary
    """
    data = []
    try:
        with open(filename) as f:
            for line in f:
                data.append(json.loads(line.strip()))
    except:
        print "Failed to read data!"
        return []
    print "The json file has been successfully read!"
    return data

class Search(object):
    """ A search engine for tweets. """
    def __init__(self, ranker=None, classifier=None):
        """
        purpose: Create the search engine for tweets
        parameters:
            database - store tweets information
        """
        # database will be used to store tweets
        self.mytweets = []
        # used to store the frequency of documents, df:the number of docs that t occurs in
        self.freq_docs = {}
        # you might need this to store all terms/tokens in our documents as vector space
        # self.word_list = []
        # used to store inverted index information for all terms/tokens
        self.inverted_index = {}
        # used to store vector for each doc
        self.vec_docs = []


    def _term_tf_idf(self, token, count):
        """
        purpose: Calculate tf-idf for a token in the document
        parameters:
            token - 
            count - the number of occurrence of a term/token in one document
        return: term/token's tf-idf
        """
        if count == 0:
            return 0
        else:
            N   = float(len(self.mytweets))
            df  = self.freq_docs[token]
            idf = log(N/df, 2)
            # print df
            # print "idf is " + str(idf)
            # print N
            return ((1+log(count, 2))*idf)


               
    def CosineSim(self, vec_query, vec_doc):
        """
        purpose: Calculate cosine similarity for two documents (vectors)
        parameters:
            vec_query - the vector with only raw term frequency for query
            vec_doc   - the vector of tf-idf for a document
        return: cosine similarity between the query and a document
        """
        # vec_doc = {'a': 0.xxx, 'aa':1.xx, ...}
        # vec_query = {'aggie': 1, 'football':2} // raw freq

        # compute length
        len_query = sqrt(sum(vec_query[x]**2 for x in vec_query))
        # print len_query
        len_doc = sqrt(sum(vec_doc[x]**2 for x in vec_doc))
        # print len_doc
        product = 0
        for term in vec_query:
            for token in vec_doc:
                if term == token:
                    product += vec_query[term]*vec_doc[token]
                    break
        return product/(len_query*len_doc)

        
    def index_tweets(self,parkDetails):
        """
        purpose: process raw parkDetails and calculate tf-idf for all terms/tokens in parkDetails
        parameters:
          parkDetails - an iterator of tweet dictionaries
        returns: none
        """

        for idx, detail in enumerate(parkDetails):
            self.mytweets.append(detail)            #store all tweets in mytweet
            for ID in detail:
                for token in detail['amenity']:
                # if token not in self.word_list:
                #     self.word_list.append(token) 
                    if token not in self.inverted_index:
                        self.inverted_index[token] = []
                    if idx not in self.inverted_index[token]:
                        self.inverted_index[token].append(idx)

        for token in self.inverted_index:
            self.freq_docs[token] = len(self.inverted_index[token])

        for detail in self.mytweets:
            vector = {}
            # get raw tf in each tweet
            for token in detail['amenity']:
                if token not in vector:
                    vector[token] = 1
                else:
                    vector[token] += 1

            # calculate tf-idf vector for each detail      
            for token in vector:
                vector[token] = self._term_tf_idf(token, vector[token])          
            self.vec_docs.append(vector)
        # print self.vec_docs[0]
                

if __name__=="__main__":
    print "Test is starting..."
    _searcher = Search()                                                   # create our searcher
    pd = read_data(os.path.join(os.getcwd(),'parkDetails.json'))   # read all parkDetails from json file
    _searcher.index_tweets(pd)                                              # index parkDetails and calculate tf-idf
    


