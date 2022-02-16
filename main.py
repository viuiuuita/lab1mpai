from skimage.io import imread, imsave
from matplotlib import pyplot as plt
from skimage.io import imshow, show
from skimage.filters import median
from skimage.exposure import match_histograms,histogram
from skimage.morphology import disk, diamond, star, rectangle
import numpy as np
import json
import matplotlib

uploaded= files.upload()

settings= {'parameter_0':'lab_1.jpg'}
with open('settings.json', 'w') as fp:
    json.dump(settings, fp)

with open('settings.json') as json_file:
    json_data = json.load(json_file)

for entry in json_data.keys():
  print(f'Название параметра: {entry}, тип параметра: {type(json_data[entry])}, значение параметра: {json_data[entry]}')

path = json_data['parameter_0']
img = imread(path)
#print(img)


