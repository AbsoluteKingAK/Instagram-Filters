import cv2
import matplotlib.pyplot as plt

s = cv2.imread('snake.png')
blur = cv2.GaussianBlur(s,(5,5),cv2.BORDER_DEFAULT)
plt.imshow(blur)
plt.show()