#Convex Hull
import numpy as np
import cv2 as cv
src = cv.imread("conhull.png", 1)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY) # convert to grayscale
blur = cv.blur(gray, (3, 3)) # blur the image
ret, thresh = cv.threshold(blur, 50, 255, cv.THRESH_BINARY)
points = np.array([[100,224],[265,122],[367,150],[484,125],[256,372],[151,316],[144,146],[457,267],[396,345]])
hull=[]
hull = cv.convexHull(points);

"""
for i in range(len(hull)):
	print(hull[i])
"""

hull = hull.reshape((-1,1,2))
src = cv.polylines(src,[hull],True,(0,0,255))
cv.imshow('Convex Hull',src)

k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('ConvexHull.png',src)
    cv.destroyAllWindows()


"""
img = cv.imread('conhull.png',0)
cv.imshow('image',img)
img2=cv.circle(img,(144,146), 2, (0,0,255), -1)
img2=cv.circle(img2,(100,224), 2, (0,0,255), -1)
img2=cv.circle(img2,(151,316), 2, (0,0,255), -1)
img2=cv.circle(img,(256,372), 2, (0,0,255), -1)
img2=cv.circle(img,(396,345), 2, (0,0,255), -1)
img2=cv.circle(img,(457,267), 2, (0,0,255), -1)
img2=cv.circle(img,(484,125), 2, (0,0,255), -1)
img2=cv.circle(img,(367	,150), 2, (0,0,255), -1)
img2=cv.circle(img,(265,122), 2, (0,0,255), -1)
"""
