import numpy as np
import tensorflow as tf

array = np.array([1, 2, 3, 4, 5])
print(array)
print (array.ndim)
print (array.shape)
print (array.dtype)

tensor = tf.convert_to_tensor(array,tf.int32)
print(tensor)

