import cv2
import numpy as np
import os
import sys

filepath = sys.argv[1]
img_height = 40
img_width = 80

def shift(seq):
    return seq[0], seq[1:]+seq[:1]

img = cv2.imread(filepath)
img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_AREA)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

canvas = np.zeros(img.shape[:2]).astype(str)

for contour in contours:
    for point in contour:
        canvas[point[0][1], point[0][0]] = 1
        
canvas = canvas[:,1:-1]

letter = 'l'
letters = ['g', 't', 'm', 'l']

for j, row in enumerate(canvas):
    for i, val in enumerate(row):
        if val == "1":
            canvas[j][i] = letter
            letter, letters = shift(letters)
finalised = np.where(canvas == '0.0', ' ', canvas)
finalised2 = '\n'.join([''.join(row) for row in finalised])

print(finalised2)
