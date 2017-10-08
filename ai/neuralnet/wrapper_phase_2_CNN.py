import pickle
import numpy as np
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.data_utils import pad_sequences
import preProcessFiles as ppf
import random

def create_network(maxlen=15):
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
	wordlist = pickle.load(open('ai/neuralnet/word_list_for_phase_2_CNN.p', 'r'))
	model.load('ai/neuralnet/phase2CNN.model')
	return model, wordlist

def predict(model, wordlist, text1, text2, maxlen=15):
	arr = np.array([pad_sequences([ppf.tokenize(ppf.processLine(str(text1)).split(), wordlist)], maxlen), pad_sequences([ppf.tokenize(ppf.processLine(str(text2)).split(), wordlist)], maxlen)])
	arr = arr.reshape([-1, 2, maxlen, 1])
	return model.predict(arr)[0]