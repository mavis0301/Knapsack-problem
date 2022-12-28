import cv2

import numpy as np

import matplotlib.pylab as plt
import math
img = cv2.imread('warrior.png')
pts=[]
M=[]
pic = []
rows,cols,ch = img.shape
pts.append(np.float32([[0,0],[rows,0],[0,cols]]))

#y2 = [0,0+10,0+15,0+20,0+30,0+30,0+30,0+20,0+15,0+10,0]  波浪

l = 60
r=400
c=400        
x1 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
y1 = [0,0-10,0-20,0-30,0-40,0-50,0-50,0-50,0-50,0-50,0-50]
x2 = [r,r,r,r,r,r,r,r,r,r,r]
y2 = [0,0,0,0,0,0,0,0,0,0,0]
x3 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
y3 = [c,c-10,c-20,c-30,c-40,c-50,c-50,c-50,c-50,c-50,c-50]

img = cv2.resize(img, (400, 400), interpolation=cv2.INTER_AREA)

m = np.array([[1.,0.,0.],[math.tan(60/180*math.pi),1.,0.]])
nnewimg = cv2.warpAffine(img,m,(c,r))
p1 = np.float32([[0,0],[r,0],[0,c]])
for i in range(1,11):
    p2 = np.float32([[x1[i],y1[i]],[x2[i],y2[i]],[x3[i],y3[i]]])
    M = cv2.getAffineTransform(p1,p2)
    print(M)
    print()
    newimg = cv2.warpAffine(img,M,(c,r))
    pic.append(newimg)
cv2.imshow('ori', img)
cv2.imshow('Result', nnewimg)



cv2.waitKey(0)





plt.show()