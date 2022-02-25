import cv2
import matplotlib.pyplot as plt

s = cv2.imread('snake.png')
d = cv2.Canny(s,100, 300)
plt.imshow(d)
plt.show()