import pickle
import numpy as np
import random
from keras.models import Sequential, model_from_json
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
import preProcessFiles as ppf

max_review_length = 130

def createModel():
	wordlist = pickle.load(open('wordlist.pkl', 'r'))
	len_words = len(wordlist)
	embedding_vecor_length = 30
	model = Sequential()
	model.add(Embedding(len_words, embedding_vecor_length, input_length=max_review_length))
	model.add(Dropout(0.5))
	model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
	model.add(Dropout(0.5))
	model.add(MaxPooling1D(pool_size=3))
	model.add(Dropout(0.5))
	model.add(LSTM(150))
	model.add(Dropout(0.5))
	model.add(Dense(1, activation='sigmoid'))
	json_file = open('model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)
	model.load_weights('model.h5')
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model, wordlist

def predict(model, wordlist, lines):
	lines = [lines]
	for line in lines:
	line = ppf.processLine(line)
	line = line.split()
	line = ppf.tokenize(line, wordlist)
	line = sequence.pad_sequences([line], maxlen=max_review_length)
	if model.predict(line)[0][0] > 0.8:
		return True
	else:
		return False