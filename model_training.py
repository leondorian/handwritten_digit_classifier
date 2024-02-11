import math

import numpy as np
import tensorflow as tf

# Load dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), _ = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
ceil_func = np.vectorize(math.ceil)
x_train = ceil_func(x_train)

# Create model
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(x_train, y_train, epochs=5)

# Save model
model.save('digit.model')
