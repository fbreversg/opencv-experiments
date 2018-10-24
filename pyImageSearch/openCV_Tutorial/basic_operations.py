""" Ejemplos de transformacion con opencv """

"""

cv2.imread(image)
cv2.imshow(title, image)
cv2.resize(image, (height, width)
cv2.getRotationMatrix2D(center, angle, scale)
cv2.warpAffine(image, M, (w, h))
cv2.GaussianBlur(image, (k, k), 0) - (k, k) = kernel ej (11,11)
cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])
cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) 
cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

"""

import imutils
import cv2

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("vaultofdoom.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image", image)
cv2.waitKey(0)

# extract a 100x100 pixel square ROI (Region of Interest) from the input image
# # image[startY:endY, startX:endX]
roi = image[144:500, 200:650]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv2.resize(image, (200, 200))
cv2.imshow("Fixed Resizing", resized)
cv2.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
cv2.imshow("Aspect Ratio Resize", resized)
cv2.waitKey(0)

# # manually computing the aspect ratio can be a pain so let's use the
# # imutils library instead
resized = imutils.resize(image, width=300)
cv2.imshow("Imutils Resize", resized)
cv2.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
""" cv2.getRotationMatrix2D(center, angle, scale) """
M = cv2.getRotationMatrix2D(center, -45, 1.0)
""" cv2.warpAffine(src, M, dsize[, dst[, flags[, borderMode[, borderValue]]]]) """
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated)
cv2.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
""" cv2.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]])kSize es  """
blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
""" cv.Rectangle(img, pt1, pt2, color, thickness=1, lineType=8, shift=0) """
output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
""" cv.Circle(img, center, radius, color, thickness=1, lineType=8, shift=0) """
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)
cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
""" cv.Line(img, pt1, pt2, color, thickness=1, lineType=8, shift=0) """
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# draw green text on the image
output = image.copy()
cv2.putText(output, "Texto", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)
