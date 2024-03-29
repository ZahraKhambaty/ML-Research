"""
COMP 551 - Assignment 2
Text Classification

Authors:
    Michael Golfi <michael.golfi@mail.mcgill.ca>
    Shruti Bhanderi <shruti.bhanderi@mail.mcgill.ca>
    Zahra Khambaty <zahra.khambaty@mail.mcgill.ca>
"""
import pandas as pd
from math import log
from collections import Counter
import numpy as np
import os.path

from sklearn.metrics import classification_report, confusion_matrix

def word_count(df, column_name):
    words = df[column_name].str.split().tolist()
    return pd.DataFrame(Counter(pd.DataFrame(words).stack()).items(), columns=["word", "count"])

def classify(model, testSet, totalWordCount, totalWordsInCategories):
    found = np.float(0.0)
    alpha = 0.009
    
    predictions = []
    for i, instance in testSet.iterrows():
        likelihood = {}
        for category in model.keys():
            pWC = 0

            for word in instance["conversation"].split():

                if word in model[category]:
                    pWC += log( (model[category][word] + alpha ) / ( len(model[category]) + totalWordCount + alpha ), 2)
                else:
                    pWC += log(alpha / ( len(model[category]) + totalWordCount + alpha ), 2 )

            #print "Category: %s length: %d, WordsInCat: %s, pWC: %f" % (category, len(model[category]), totalWordsInCategories, pWC)
            likelihood[category] = log(np.float64(len(model[category])) / np.float64(totalWordsInCategories), 2) + pWC  
        
        max_label = max(likelihood.iterkeys(), key=(lambda key: likelihood[key]))
        predictions.append(max_label)

        
        if instance["category"] == max_label:
            found += 1
    print "Accuracy: ", (found/float(len(testSet)) * 100.0)
    return predictions

def train(trainingSet):
    model = {}
    instancesInAllModels = 0
    for (name, category) in trainingSet.groupby(["category"]):
        model[name] = word_count(category, "conversation").set_index("word")["count"].to_dict()
        instancesInAllModels += len(model[name])
    return model, instancesInAllModels

def main():
    FILENAME = "data/train_input.csv"
    CATEGORY = "data/train_output.csv"
    
    TRAINING_THRESHOLD = 0.7

    train_input_X = pd.read_csv(FILENAME, usecols=["conversation"])
    train_input_Y = pd.read_csv(CATEGORY, usecols=["category"])
    train_input_XY = pd.concat([train_input_X, train_input_Y], axis=1)

    print "Splitting into training and testing"
    cutoff = np.random.rand(len(train_input_XY)) < TRAINING_THRESHOLD
    trainingSet = train_input_XY[cutoff]
    test = train_input_XY[~cutoff]

    print "Count all distinct words in vocabulary"
    vocab_word_count = word_count(train_input_XY, "conversation")["count"].sum()
    print "Found %d words in vocabulary" % vocab_word_count

    print "Calculating probabilities for all classes"
    model, instancesInAllModels = train(trainingSet)   
    
    print "Classifying and validating model output"
    predictions = classify(model, test, vocab_word_count, instancesInAllModels)

    report = classification_report(test["category"].values, predictions)
    print report

    confMatrix = confusion_matrix(test["category"].values, predictions)
    print confMatrix

if __name__ == "__main__":
    main()