import cv2
import os
#from tkinter.filedialog import *


# we will find number of blobs with pixel value 255 in the following image

# finding binary image
# Path to your image file (mounted or copied in container)
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "blobImg.png")

# Check if file exists
if not os.path.exists(IMAGE_PATH):
    raise FileNotFoundError(f"Image not found at {IMAGE_PATH}")

# Read image
image = cv2.imread(IMAGE_PATH, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise ValueError("Failed to load image. Make sure the file format is correct.")

img = cv2.resize(image, (300, 300))
n, l = img.shape
count = 0

# blur the image
ksize = (5, 5)  # kernel size
img = cv2.blur(img, ksize)

# thresholding the image
for i in range(n):
    for j in range(l):
        if (img[i, j] <= 127):
            img[i, j] = 0
        else:
            img[i, j] = 255


def dfs(i, j):
    img[i, j] = 127  # implying that we have visited this pixel for further reference
    if (i-1 >= 0):
        if (img[i-1, j] == 255):
            dfs(i-1, j)
    if (j-1 >= 0):
        if (img[i, j-1] == 255):
            dfs(i, j-1)
    if (j+1 < l):
        if (img[i, j+1] == 255):
            dfs(i, j+1)
    if (i+1 < n):
        if (img[i+1, j] == 255):
            dfs(i+1, j)
    if ((i-1 >= 0) and (j-1 >= 0)):
        if (img[i-1, j-1] == 255):
            dfs(i-1, j-1)
    if ((i-1 >= 0) and (j+1 < l)):
        if (img[i-1, j+1] == 255):
            dfs(i-1, j+1)
    if ((i+1 < n) and (j-1 >= 0)):
        if (img[i+1, j-1] == 255):
            dfs(i+1, j-1)
    if ((i+1 < n) and (j+1 < l)):
        if (img[i+1, j+1] == 255):
            dfs(i+1, j+1)


# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow("image", img)
# cv2.waitKey(1000)


for i in range(n):
    for j in range(l):
        if (img[i, j] == 255):
            count += 1  # to count number of white blobs
            dfs(i, j)

print("count is", count)
