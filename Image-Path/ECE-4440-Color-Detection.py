# Source: https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/

import sys
import cv2
import numpy as np

# Define the list of colors to be detected
# TODO: Make it three shades instead of five
boundaries = [
    ([0], [50]),    # black
    ([51], [101]),  # dark gray
    ([102], [152]), # gray
    ([153], [203]), # light gray
    ([204], [255])  # white
]

# Read the original image
name = sys.argv[1]
img_path = 'Edge-Detection-Test-' + name + '.jpg'
try:
    img = cv2.imread(img_path)
except OSError:
    print("Could not read file: " + img_path)
    exit(1)

# Resize the image to decrease the resolution
img_resize = img
scale_percent = 80 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# TODO: Do math to erase need for loop silly
while (width > 300 or height > 300):
    img_resize = cv2.resize(img_resize, dim, interpolation = cv2.INTER_AREA)
    width = int(img_resize.shape[1] * scale_percent / 100)
    height = int(img_resize.shape[0] * scale_percent / 100)
    dim = (width, height)

# TODO: Contrast colors in image for better color detection

# Convert to graycsale
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_BGR2GRAY)
# Blur the image for better color detection
# TODO: Play around with blurring and see what produces the best result!
#       Use bilateral blurring?
img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
# img_blur = cv2.medianBlur(img_blur, 3)

# TODO: Apply background erosion to remove unnecessary background colors

# loop over the boundaries
for (lower, upper) in boundaries:
	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(img_blur, lower, upper)
	# show the images
	cv2.imshow("images", np.hstack([img_blur, mask]))
	cv2.waitKey(0)

cv2.destroyAllWindows()
