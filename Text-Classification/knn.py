import pandas as pd
from collections import Counter
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from math import log
import numpy as np

# Assumes that nltk stopwords and lemmatizer are downloaded.

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(df)
tfidf_transformer = TfidfTransformer()
vectX_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
vectX_train_tfidf.shape

# Determining weight matrix vectW

def weightmatrix(vectX_train_tfidf)

    for (i=0;i<numOfuniquewords;i++):
       fij=numberofwordiinarticlej
       tdiftemp= fij*math.log(numberoFArticles/articlefreqofi)
       summTfidf+=pow(tdiftemp,2) 
    Wij=vectX_train_tfidf/summTfidf

def euclideanDistance()
    distance = []
    for i in range(numberOfArticles):
        for j in range(numberOfUniqueovocabcc)
        distance[i] += pow(W[j,i]-(W[j,(numberOfArticles-1),2)
    return math.sqrt(distance)

##X is the test document, represented as a vector;
##Dj is the jth training document;
#ti is a word shared by X and  Dj;
#xi is the weight of word ti in X;
#d{ij} is the weight of word ti in document Dj;  
#||X||^2= sqrt{x_1^2 + x_2^2 + x_3^2 + .. is the norm of X, and 
#||Dj||^2 is the norm of Dj
def ClassifyCosineSim(testsetX, trainingSetD)

X = np.array(vectX_train_tfidf) 
normX= np.array(testsetX.euclideanDistance()) 
Dj= np.array(vectWTraining)
normD=np.array(trainingSetD.euclideanDistance())
denominator = pow(normX,2)+pow(normD,2)  
for i in range(numberOfArticles):
    for j in range (numberofarticlesinTestset):
       total+=np.cross(X[j],D[i])

return total/denominator



