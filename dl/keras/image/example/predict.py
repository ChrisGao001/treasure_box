#!/usr/bin/python

import sys
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array


def get_img_feature(img_file_path, target_size=(150,150)):
	image = load_img(img_file_path, target_size=target_size)
	image = img_to_array(image)
	image = image / 255.0
	image = np.expand_dims(image, axis=0) 
	#image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
	return image

model = load_model("./birds_class.h5")
img_file_path=sys.argv[1]
x = get_img_feature(img_file_path)
y = model.predict(x)
y = np.argmax(y)
print(img_file_path, y)

