#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def build_corpus(data):
    corpus=data.to_numpy().tolist()
    return corpus
def creating_set(corpus):
    bows=[]

    for doc in corpus:
        bows.append(doc.split(" "))
    sets=[]
    for s in bows:
        sets.append(set(s))
    wordSet=set().union(*sets)
    
    return bows, wordSet

def worddictionnary(bows):
    wordDicts=[]
    for bow in bows:
        wordDict =dict.fromkeys(wordSet,0)
        for word in bow:
            wordDict[word]+=1
            wordDicts.append(wordDict)
    return wordDicts


def computeTF(wordDict,bow):
    tfDict = {}
    bowCount = len(bow)
    for word,count in wordDict.items():
        #TF = No.of reps words in a sentence/ Total words in a sentence
        tfDict[word] = count/float(bowCount)
    return tfDict


def tf_outputs(wordDicts,bows):
    tfBows=[]
    for i in range(len(bows)):
        tfBows.append(computeTF(wordDicts[i],bows[i]))
    return tfBows


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    #{'girl':0 ,'good':0,'boy':0}
    idfDict = dict.fromkeys(docList[0].keys(),0)
    
    #Lets find the number of docs which contain word(Wi)
    for doc in docList:
        for word,val in doc.items():
            if val >0:
                idfDict[word]+=1
    #{'girl':2 ,'good':3,'boy':2}
    #IDF calculation
    for word,val in idfDict.items():
#         idfDict[word] = math.log10(N/float(val)) 
        idfDict[word] = math.log10((N+1)/(float(val)+1.0))+1
    return idfDict



def IDFoutput(wordDicts):
    idfs = computeIDF([wordDict for wordDict in wordDicts])
    return idfs


def computeTFIDF(tfBow,idfs):
    tfidf ={}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf



def TFIDF_output(bows):
    tfidfBows=[]
    for i in range(len(bows)):
        tfidfBows.append(computeTFIDF(tfBows[i],idfs))
        
    return tfidfBows


import pandas as pd
def finalresult(tfidfBows):
    Finaldata=pd.DataFrame([tfidfBow for tfidfBow in tfidfBows])
    return Finaldata

