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
# fix random seed for reproducibility
TRAIN = False
np.random.seed(7)
# load the dataset but only keep the top n words, zero the rest
trainingSet = pickle.load(open('training.pkl', 'r'))
wordlist = pickle.load(open('wordlist.pkl', 'r'))
len_words = len(wordlist)
random.shuffle(trainingSet)
training = trainingSet[:400] 
testing = trainingSet[400:]
X_train, y_train, X_test, y_test = [], [], [], []
for train in training:
	X_train.append(train[0])
	y_train.append(train[1][0])
y_train = np.array(y_train)
# print y_train
# print y_train.shape
for test in testing:
	X_test.append(test[0])
	y_test.append(test[1][0])
y_test = np.array(y_test)
# truncate and pad input sequences

max_review_length = 130
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)
# create the model
embedding_vector_length = 30
model = Sequential()
model.add(Embedding(len_words, embedding_vector_length, input_length=max_review_length))
model.add(Dropout(0.5))
model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(Dropout(0.5))
model.add(MaxPooling1D(pool_size=3))
model.add(Dropout(0.5))
model.add(LSTM(150))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
if TRAIN:
	model.fit(X_train, y_train, epochs=25, batch_size=32)
else:
	try:
		json_file = open('model.json', 'r')
		loaded_model_json = json_file.read()
		json_file.close()
		model = model_from_json(loaded_model_json)
		model.load_weights('model.h5')
		model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	except:
		model.fit(X_train, y_train, epochs=25, batch_size=32)
# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1]*100))

#saves model
model_json = model.to_json()
with open('model.json', 'w') as json_file:
	json_file.write(model_json)
model.save_weights('model.h5')

#to test
lines = ["I got 96% in my boards", "I am a boy", "5 billion people", "500 rupees is discontinued", "5 out of 10 americans are gay"]
for line in lines:
	print line
	line = ppf.processLine(line)
	line = line.split()
	line = ppf.tokenize(line, wordlist)
	line = sequence.pad_sequences([line], maxlen=max_review_length)
	print model.predict(line)
	print ""