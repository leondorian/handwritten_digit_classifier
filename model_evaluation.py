import math

import numpy as np
import tensorflow as tf

# Load dataset
mnist = tf.keras.datasets.mnist
_, (x_test, y_test) = mnist.load_data()

x_test = tf.keras.utils.normalize(x_test, axis=1)
ceil_func = np.vectorize(math.ceil)
x_test = ceil_func(x_test)

# Load model
model = tf.keras.models.load_model('digit.model')

# Evaluate model
loss, accuracy = model.evaluate(x_test, y_test)

print(f'Loss: {loss}')
print(f'Accuracy: {accuracy}')
