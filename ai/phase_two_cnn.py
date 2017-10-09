import pickle
import numpy as np
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.data_utils import pad_sequences
import ai.neuralnet.preProcessFiles as ppf
import ai.nlp.numtext_interconversion as ni
import random


def create_network(maxlen=15):
    convnet = None
    convnet = input_data(shape=[None, 2, maxlen, 1], name='input')

    convnet = conv_2d(convnet, 8, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = conv_2d(convnet, 16, 2, activation='relu')
    convnet = max_pool_2d(convnet, 2)

    convnet = fully_connected(convnet, 32, activation='relu')
    convnet = dropout(convnet, 0.8)

    convnet = fully_connected(convnet, 32, activation='relu')
    convnet = dropout(convnet, 0.7)

    convnet = fully_connected(convnet, 2, activation='softmax')
    convnet = regression(convnet, optimizer='adam', n_classes=2, learning_rate=0.01, loss='categorical_crossentropy', name='targets')

    model = tflearn.DNN(convnet)
    return model


positive = pickle.load(open('ai/neuralnet/trainingpositive.p', 'r'))
negative = pickle.load(open('ai/neuralnet/trainingnegative.p', 'r'))


globalArray = [positive, negative]
training = []
for array in globalArray:
    for subarray in array:
        training.append([ni.wrapper_normalizer(subarray[0].strip()), ni.wrapper_normalizer(subarray[1].strip()), subarray[2]])

for line in training:
    line[0] = ppf.processLine(str(line[0]))
    try:
        line[1] = ppf.processLine(str(line[1]))
    except:
        print line[1]
        z = line[1]
        break

wordlist = []
for array in training:
    temp = array[0].split()
    temp.extend(array[1].split())
    for word in temp:
        if word not in wordlist:
            wordlist.append(word)
    
pickle.dump(wordlist, open('word_list_for_phase_2_CNN.p', 'w'))

finalTraining = []
for array in training:
    finalTraining.append([ppf.tokenize(array[0].split(), wordlist), ppf.tokenize(array[1].split(), wordlist), np.array(array[2])])


pickle.dump(finalTraining, open('phase2_training_set.p', 'w'))
maxlen = 15

random.shuffle(finalTraining)
X_train, X_test, y_train, y_test = [], [], [], []
for i in range(int(0.9*len(finalTraining))):
    X_train.append(np.array([pad_sequences([finalTraining[i][0]], maxlen),pad_sequences([finalTraining[i][1]], maxlen)]))
    y_train.append(np.array(finalTraining[i][2]))
    
for i in range(int(0.9*len(finalTraining)), len(finalTraining)):
    X_test.append(np.array([pad_sequences([finalTraining[i][0]], maxlen),pad_sequences([finalTraining[i][1]], maxlen)]))
    y_test.append(np.array(finalTraining[i][2]))
X_train = np.array(X_train)
y_train = np.array(y_train)
X_test = np.array(X_test)
y_test = np.array(y_test)

X_train = X_train.reshape([-1, 2, maxlen, 1])
X_test = X_test.reshape([-1, 2, maxlen, 1])


model = create_network(maxlen)
model.fit({'input':X_train}, {'targets':y_train}, n_epoch=150)

model.save('ai/neuralnet/phase2CNN.model')