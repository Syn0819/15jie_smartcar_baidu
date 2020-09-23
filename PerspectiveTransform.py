import os, re
import numpy as np
import cv2 as cv
import numpy.linalg as LA
from matplotlib import pyplot as plt



img_name='8543.jpg'
image =os.path.join("D:\programme\Python",img_name)
src = cv.imread(image)
"""
M矩阵系数即摄像头内参：摄像头广角度数、摄像头高度等等，实际使用需测定或凑
"""
pts1=np.float32([[0,70],[320,70],[0,240],[320,240]])
pts2=np.float32([[0,0],[250,0],[75,150],[175,150]])
M=cv.getPerspectiveTransform(pts1,pts2)
dst=cv.warpPerspective(src,M,(640,480),cv.INTER_LINEAR)
cv.imwrite("11.jpg",dst)



