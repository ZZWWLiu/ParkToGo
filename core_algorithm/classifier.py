import json
import os
# import random
from stemming import porter2
import re
from math import log
from math import sqrt

def read_data(filename):
    """
    Used to read all tweets from the json file.
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

class Classifier_NB():
    def __init__(self, classes, Traindata):
        self.classesTrainData = []
        for c in classes:
            d = []
            for idx in c:
                d.extend(Traindata[idx]['amenity'])
            self.classesTrainData.append(d)
        self.N = len(self.classesTrainData) # num of classes

    def extractVocabulary(self):
        """
        helper function
        tweets have 800 tweets, get 700 for training
        get a list of tweets, [{'a': 1.23, 'tamu': 2, ..},{...}]
        """
        # tweets_Houston = random.sample(tweets[:400], 350)
        # tweets_Dallas  = random.sample(tweets[401:], 350)
        # training_tweets = tweets_Houston.append(tweets_Dallas)
        vocabulary = []
        for data in self.classesTrainData:
            for word in data:
                vocabulary.extend(tokenize(word))
        s = set(vocabulary)
        vocabulary = list(s)
        return vocabulary 

    def concatenateTextOfAllDocsInClass(self, classnum):
        """
        helper function
        return a dict storing all the token in class c
        """
        text = {}
        for word in self.classesTrainData[classnum]:
            for token in tokenize(word):
                if token not in text:
                    text[token] = 0
                text[token] += 1
        return text

    def Train(self):
        V = self.extractVocabulary()  
        Prior = [ 1.0/self.N ] * self.N
        text_c = {}
        condprob = {}
        for idx, c in enumerate(self.classesTrainData):
            # Prior[c] = 1.0/5
            text_c[idx] = self.concatenateTextOfAllDocsInClass(idx)
            clen = sum([text_c[idx][t] for t in text_c[idx]])
            for token in V:
                if token in text_c[idx]:
                    Tct = text_c[idx][token]
                else:
                    Tct = 0
                if token not in condprob:
                    condprob[token] = {}
                condprob[token][idx] = float(Tct+1)/(clen+len(V))
        return V, Prior, condprob

    def extractTokenFromDoc(self, V, d):
        """
        helper function used in applyMultinomialNB to 
        extract tokens from doc d those tokens should 
        be shared by both V and d
        Input: V- vocabulary, d-stringList of doc being classified
        """
        Tokens = {}
        for string in d: 
            for token in tokenize(string):
                if token in V:
                    if token not in Tokens:
                        Tokens[token] = 0
                    Tokens[token] += 1
        return Tokens


    def applyMultinomialNB(self, V, Prior, condprob, d):
        """
        return class num c which doc d should belong
        """
        W = self.extractTokenFromDoc(V,d)
        score = [0] * self.N
        for c in xrange(0,len(self.classesTrainData)):
            # print "Prior", Prior[c]
            score[c] = log(Prior[c])
            for t in W:
                # print "condprob ",condprob[t][c]
                score[c] += log(condprob[t][c])
        return score.index(max(score))
    

if __name__ == "__main__":
    data = read_data(os.path.join(os.getcwd(),'NparkDetails.json'))
    docs = read_data(os.path.join(os.getcwd(),'parkDetails.json'))
    # skiing
    class1 = [2,5,7,11,15,21,23,50,57]

    # hunting, general tour
    class2 = [3,8,20,24,36,38,41,44,54,10,17,48,30,32,27]

    # caneoing, kayalaying
    class3 = [6,18,19,26,29,39,45,46,51,52, 56]

    # biking
    class4 = [16,28,31,33,37,42,43,49,53,50,10]

    # horse riding
    class5 = [0,1,4,9,12,13,22,25,55,34,35,40]

    classes = []
    classes.append(class1)
    classes.append(class2)
    classes.append(class3)
    classes.append(class4)
    classes.append(class5)
    # start classification
    print "start classification..."
    classifier = Classifier_NB(classes, data)
    V, Prior, condprob = classifier.Train()
    
    result = [[], [], [], [], []]
    for d in docs:
        num = classifier.applyMultinomialNB(V, Prior, condprob, d['amenity'])
        result[num].append(d)
    # print result

    filename = "classifiedParks.json"
    f = open(filename, "w")
    for line in result:
        f.write(json.dumps(line)+'\n')
    f.close()
    print "done..."






