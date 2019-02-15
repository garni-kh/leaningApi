
from pylab import rcParams
import os
import seaborn as sns
import heapq
import sys
import pickle
import matplotlib.pyplot as plt
from keras.optimizers import RMSprop
from keras.layers.core import Dense, Activation, Dropout, RepeatVector
from keras.layers import TimeDistributed
from keras.layers import LSTM, Dropout
from keras.layers import Dense, Activation
from keras.models import Sequential, load_model
import numpy as np
np.random.seed(42)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
LEARN_MODEL = os.path.join(APP_ROOT, 'static/model')
LEARN_TEXT = os.path.join(APP_ROOT, 'static/cleantext')


sns.set(style='whitegrid', palette='muted', font_scale=1.5)

rcParams['figure.figsize'] = 12, 5




path = LEARN_TEXT + "/" + "comments9.txt"
text1 = open(path).read().lower()


chars = sorted(list(set(text1)))
char_indices = dict((c, i) for i, c in enumerate(chars))
indices_char = dict((i, c) for i, c in enumerate(chars))


SEQUENCE_LENGTH = 40
step = 3
sentences = []
next_chars = []
for i in range(0, len(text1) - SEQUENCE_LENGTH, step):
    sentences.append(text1[i: i + SEQUENCE_LENGTH])
    next_chars.append(text1[i + SEQUENCE_LENGTH])


X = np.zeros((len(sentences), SEQUENCE_LENGTH, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

print("------------sentences[161]-------------------")
print(sentences[161])
print(y.shape)

model = Sequential()
model.add(LSTM(128, input_shape=(SEQUENCE_LENGTH, len(chars))))
model.add(Dense(len(chars)))
model.add(Activation('softmax'))

#start learning very imported comment and un comment
optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy',
             optimizer=optimizer, metrics=['accuracy'])
history = model.fit(X, y, validation_split=0.05,
                  batch_size=128, epochs=40, shuffle=True).history
#model save
model.save(LEARN_MODEL + "/" + 'keras_model_theano_4.h5')
pickle.dump(history, open(LEARN_MODEL + "/" + "history4_theano_5.p", "wb"))


model = load_model(LEARN_MODEL + "/" + "keras_model_theano_4.h5")
history = pickle.load(open(LEARN_MODEL + "/" + "history4_theano_5.p", "rb"))


def prepare_input(text):
    x = np.zeros((1, SEQUENCE_LENGTH, len(chars)))
    for t, char in enumerate(text):
        x[0, t, char_indices[char]] = 1.

    return x


def sample(preds, top_n=1):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds)
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)

    return heapq.nlargest(top_n, range(len(preds)), preds.take)


def predict_completion(text):
    original_text = text
    generated = text
    completion = ''
    while True:
        x = prepare_input(text)
        preds = model.predict(x, verbose=0)[0]
        next_index = sample(preds, top_n=1)[0]
        next_char = indices_char[next_index]
        text = text[1:] + next_char
        completion += next_char

        if len(original_text + completion) + 2 > len(original_text) and next_char == ' ':
            return completion


def predict_completions(text, n=10):
    x = prepare_input(text)
    preds = model.predict(x, verbose=0)[0]
    next_indices = sample(preds, n)
    return [indices_char[idx] + predict_completion(text[1:] + indices_char[idx]) for idx in next_indices]


def testa(quotes):
        seq = quotes
        print("-------last -40--leran----")
        print(seq)
        return predict_completions(seq, 10)
