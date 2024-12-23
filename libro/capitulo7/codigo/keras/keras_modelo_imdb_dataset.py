from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow import keras
import numpy as np
imdb = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=10000)
print("Entradas de entrenamiento: {}, etiquetas: {}". format(len (train_data), len
(train_labels)))
print(train_data[0])
len(train_data[0]), len(train_data[1])

# Un diccionario que mapea palabras a un índice entero
word_index = imdb.get_word_index()
# Los primeros índices están reservados
word_index = {k:(v+3) for k,v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2 # unknown
word_index["<UNUSED>"] = 3
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

def decode_review(text):
    return ' '.join([reverse_word_index.get(i, '?') for i in text])

decode_review(train_data[0])


train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding='post', maxlen=256)

test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding='post',
maxlen=256)

vocabulary_size = 10000
model = keras.Sequential()
model.add(keras.layers.Embedding(vocabulary_size, 16))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation=tf.nn.relu))
model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
model.summary()

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
x_val = train_data[:10000]
partial_x_train = train_data[10000:]
y_val = train_labels[:10000]
partial_y_train = train_labels[10000:]

history = model.fit(partial_x_train, partial_y_train, epochs=40, batch_size=512,
validation_data=(x_val, y_val), verbose=1)

resultados = model.evaluate(test_data, test_labels)
print(resultados)
