import numpy as np
import pickle
import string
import re

fileStats = 'Statistical.txt'
fileNoStats = 'Non Statistical.txt'
labelStats = np.array([1, 0])
labelNoStats = np.array([0, 1])
wordlist = []
table = string.maketrans("","")
punctuation = '!"#$%&\'()*+,/:;<=>?@[\\]^_`{|}~'

def processLine(line):
    line = str(line)
    line = line.replace('-', ' ')
    line = line.translate(table, punctuation)
    line = str.lower(line)
    numbers = re.findall(r'[0-9]+.[0-9]+', line)
    numbers.extend(re.findall(r'[0-9]+', line))
    for number in numbers:
        temp = ' '.join(e for e in number)
        temp = ' ' + temp + ' '
        line = line.replace(number, temp)
#         print line
    endings = re.findall(r'[a-z]+[.]', line)
#         print endings
    for ending in endings:
        line = line.replace(ending, ending[:-1])
    return line

files = ['ml/'+fileStats, 'ml/'+fileNoStats]
globalArray = []
for tempFile in files:
    obj = open(tempFile, 'r').readlines()
    for line in obj:
        line = processLine(line)
        line = line.split()
        for word in line:
            if word not in wordlist:
                wordlist.append(word)

def tokenize(line, wordlist):
    for i in range(len(line)):
        try:
            line[i] = wordlist.index(line[i])+1
        except:
            line[i] = 0
    return line

for tempFile in files:
    obj = open(tempFile, 'r').readlines()
    for line in obj:
        line = processLine(line)
        line = line.split()
        line = tokenize(line, wordlist)
        if tempFile == fileStats:
            globalArray.append([line, labelStats])
        else:
            globalArray.append([line, labelNoStats])

globalArray = np.array(globalArray)
pickle.dump(globalArray, open('training.pkl', 'w'))
pickle.dump(wordlist, open('wordlist.pkl', 'w'))




