import cv2
import numpy as np
num_down = 2 #downsampling steps
num_bilateral = 7 #bilateral filtering steps

img_rgb = cv2.imread("C:/Users/DELL/Desktop/pyr3.jpg")

# downsample 
img_color = img_rgb
for _ in range(num_down):
   img_color = cv2.pyrDown(img_color)

#repeatedly apply bilateral filter 
for _ in range(num_bilateral):
   img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)

#upsample image to original size
for _ in range(num_down):
   img_color = cv2.pyrUp(img_color)
cv2.imshow("Bilateral Filter ", img_color)
   
#median filter to reduce noise convert to grayscale and apply median blur
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
cv2.imshow("Gray Scale", img_gray)
img_blur = cv2.medianBlur(img_gray, 7)
cv2.imshow("Blurred", img_blur)


img_laplace= cv2.Laplacian(img_blur,cv2.CV_8U,5)
cv2.imshow("LaPlace", img_laplace)

#adaptive thresholding to create an edge mask detect and enhance edges
#img_edge = cv2.adaptiveThreshold(img_laplace, 255,
   #cv2.ADAPTIVE_THRESH_MEAN_C,
   #cv2.THRESH_BINARY,
   #blockSize=9,
   #C=3)

#first attempt at thresholding but bad results
img_edge = cv2.threshold(img_laplace,125,255,1)
print(img_edge[1])
img_edge =cv2.UMat(img_edge[1])
cv2.imshow("edge", img_edge)

# Combine color image with edge mask & display picture convert back to color
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
height,width,channel = img_color.shape
img_edge=cv2.resize(img_edge,(width,height))
print(img_color.shape,img_edge)
img_cartoon = cv2.bitwise_and(img_color,img_edge)
print(img_cartoon)


#Final Cartoonized Image
cv2.imshow("Cartooned Image", img_cartoon)

cv2.waitKey(0)

