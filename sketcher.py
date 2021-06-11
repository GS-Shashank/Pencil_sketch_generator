# -*- coding: utf-8 -*-
"""
Project: Pencil Sketch Generator
By: GSS
"""

import cv2 #importing the openCV library

img=cv2.imread("input.jpeg");#importing the image

#code to generate the sketch of the input image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY);
inv_gray_img=255-gray_img;
blur_img=cv2.GaussianBlur(inv_gray_img,(21,21),0);
inv_blur_img=255-blur_img;
sketch=cv2.divide(gray_img,inv_blur_img,scale=240.0);

#printing the sketch file
cv2.imwrite("output.jpg",sketch);
