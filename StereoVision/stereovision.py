import numpy as np
import cv2
from matplotlib import pyplot as plt
from code import interact

imgL = cv2.imread('Left3.jpg',0)
imgR = cv2.imread('Right3.jpg',0)

stereo = cv2.StereoBM(0,ndisparities=16,SADWindowSize=17)
disparity = stereo.compute(imgL, imgR)
disparity -= disparity.min()
disparity *= (255.0/(disparity.max() - disparity.min()))
#interact(local=locals())
plt.imshow(disparity, 'gray')
plt.show()
