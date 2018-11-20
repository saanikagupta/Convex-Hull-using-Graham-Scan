#Convex Hull
import numpy as np
import cv2 as cv
src = cv.imread("conhull.png", 1)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY) # convert to grayscale
points = np.array([[100,224],[265,122],[367,150],[484,125],[256,372],[151,316],[144,146],[457,267],[396,345]])
hull = []
hull.append(cv.convexHull(points))

"""
for i in range(len(hull)):
	print(hull[i])
"""

color = (0, 255, 255) # color for convex hull
for i in range(len(hull)):
	cv.drawContours(src, hull, i, color, 2, 8)
cv.imshow('Convex Hull',src)
k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('ConvexHull.png',src)
    cv.destroyAllWindows()
