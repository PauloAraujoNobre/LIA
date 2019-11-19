from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from numpy import float32
import numpy as np
batch_size = 128
num_classes = 10
epochs = 20

f = open("train_data.csv","r")
train_data = []
for i in f.readlines():
    train_data.append(np.array(str(i).replace('\n','').split(','),float32))

f.close()
train_data  = np.array(train_data)

f = open("test_data.csv","r")
test_data= []
for i in f.readlines():
    test_data.append(np.array(str(i).replace('\n','').split(','),float32))

f.close()
test_data  = np.array(test_data)
# the data, split between train and test sets

x_train = train_data[:,:-1]
y_train = train_data[:,-1]
x_test = test_data[:,:-1]
y_test = test_data[:,-1]

print(x_train.shape)

model = Sequential()
model.add(Dense(30, activation='sigmoid'))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(5, activation='sigmoid'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mean_squared_error',
              optimizer='sgd',
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    epochs=100000,
                    verbose=1,
                    validation_data=(x_test, y_test))


score = model.evaluate(x_test, y_test, verbose=0)
model.summary()

print('Test loss:', score[0])
print('Test accuracy:', score[1])
