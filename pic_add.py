import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

path = os.getcwd()


img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('hello.png')
img2 = cv2.resize(img2,(200,200))

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

large_img = img1
small_img = img2

x_offset=0
y_offset=0
large_img[y_offset:y_offset+small_img.shape[0],x_offset:x_offset+small_img.shape[1]] = small_img

cv2.imshow('sample image',large_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

status = cv2.imwrite(path+"/newpic.png", large_img)