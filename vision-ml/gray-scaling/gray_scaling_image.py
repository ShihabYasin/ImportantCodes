import cv2
import numpy as np
import argparse
import cv2
import sys
import pytesseract
from pytesseract import Output
import glob
import os

################################################################
files = glob.glob ('GRAY_SCALE/out/*')
for f in files:
    os.remove (f)

img = cv2.imread ('GRAY_SCALE/test.jpg')
# get dimensions of image
dimensions = img.shape
img_height = img.shape[0]  # Original Image Width
img_width = img.shape[1]  # Original Image Height

# RESIZE:  https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
######### UpSizing
scale_percent = 140  # percent of original size
width = int (img.shape[1] * scale_percent / 100)
height = int (img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
img = cv2.resize (img, dim, interpolation=cv2.INTER_AREA)
#########

d = pytesseract.image_to_data (img, output_type=Output.DICT)

n_boxes = len (d['level'])
prev_x = -1
prev_y = -1
prev_w = -1
prev_h = -1

prev_line_height = 0;
cnt = 0
line = -1
word = 0
for i in range (n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    if (x == prev_x and y == prev_y and w == prev_w and h == prev_h):
        continue
    if (img_height * .18 < h):
        continue
    (prev_x, prev_y, prev_w, prev_h) = (x, y, w, h)
    #####################################  LINE FINDING & WORD IN LINE
    roi = img[y:y + h, x:x + w]
    curr_line_height = y + h
    if (curr_line_height > prev_line_height):
        line = line + 1
        cv2.imwrite ("/home/shihab/OCR_PRESCRIPTION/GRAY_SCALE/out/LINE_" + str (line) + ".jpg", roi)
        print (x, y, w, h, "/home/shihab/OCR_PRESCRIPTION/GRAY_SCALE/out/LINE_" + str (line) + ".jpg")
        word = 0
        prev_line_height = curr_line_height
    else:
        cv2.imwrite ("/home/shihab/OCR_PRESCRIPTION/GRAY_SCALE/out/LINE_" + str (line) + "_WORD_" + str (word) + ".jpg",
                     roi)
        print (x, y, w, h,
               "/home/shihab/OCR_PRESCRIPTION/GRAY_SCALE/out/LINE_" + str (line) + "_WORD_" + str (word) + ".jpg")
        word = word + 1
    ##################################################################

    # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # crop_img = img[y:y + h, x:x + w]
    # cv2.imshow("cropped", crop_img)
    cnt = cnt + 1

# cv2.imshow('img', img)

##################################    GRAY IMAGE CONVERSION START

img = cv2.imread ('GRAY_SCALE/test.jpg', cv2.IMREAD_UNCHANGED)

########## DownSizing

scale_percent = 71  # percent of original size
width = int (img.shape[1] * scale_percent / 100)
height = int (img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
image = cv2.resize (img, dim, interpolation=cv2.INTER_AREA)

###########################
cv2.imshow ("Down Sized Image", image)
##########################
# image = img
##########

gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold (gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur (gray, 3)

cv2.imwrite ('GRAY_SCALE/test_grayed.png', gray)

cv2.imshow ('Original image', image)
cv2.imshow ('Gray image', gray)

cv2.waitKey (0)
cv2.destroyAllWindows ()

##################################
