import matplotlib.pyplot as plt
from matplotlib.image import imread

# 画像の読み込み
img = imread('animal_kawauso.png')

plt.imshow(img)
plt.show()