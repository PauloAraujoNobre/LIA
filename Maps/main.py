from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd

df = np.array(pd.read_csv('iris.data.csv', header=None))

target = df[:, -1]
for i in range(len(target)):
    if target[i] == 'Iris-setosa':
        target[i] = 0
    if target[i] == 'Iris-versicolor':
        target[i] = 1
    if target[i] == 'Iris-virginica':
        target[i] = 2

[row, col] = df.shape
DF = np.ones((row, col-1))

for i in range(col-1):
    DF[:, i] = df[:, i]


df = np.array(DF)

targetOneOfK = np.zeros((len(target),3))

for i in range(len(target)):
    targetOneOfK[i][target[i]] = 1

#print(df)

#print(target)

print(targetOneOfK)
model = Sequential()
model.add(Dense(3, activation='relu', input_dim=4))
model.add(Dense(3, activation='relu'))
model.compile(optimizer='adam', loss='mse')
model.fit(df, targetOneOfK, epochs=2500, verbose=0)

while True:
    x = input('Nº 1: ')
    y = input('Nº 2: ')
    z = input('Nº 3: ')
    w = input('Nº 4: ')

    lista = [float(x), float(y), float(z), float(w)]
    t = np.asmatrix(lista)

    result = model.predict(t)
    print("Resultado: ", result)
