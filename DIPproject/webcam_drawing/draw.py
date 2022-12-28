import cv2
import numpy as np

cap = cv2.VideoCapture(0)
pic = np.zeros((480,640,3),np.uint8)
pic.fill(255)
pic_transparent = np.zeros((800,800,4),np.uint8)
# Blue[86, 121, 205, 111, 245, 255],[255, 0, 0],
# Green[46, 78, 204, 71, 255, 255],[0, 255, 0]
# Yellow blue green red gold
penColorHSV = [[14,155,142,26,255,255],
               [99,162,0,109,255,255],
               [35,66,108,92,240,255],
               [140,149,65,179,255,255],
               [0,143,118,31,242,164]]

penColorBGR = [[0,225,255],
               [198,151,44],
               [44,198,117],
               [40,60,250],
               [30,134,226]]

# [x, y, colorId]
drawPoints = []


def findPen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for i in range(len(penColorHSV)):
        lower = np.array(penColorHSV[i][:3])
        upper = np.array(penColorHSV[i][3:6])
        mask = cv2.inRange(hsv, lower, upper)
        penx, peny = findContour(mask)
        if peny!=-1:
            drawPoints.append([penx, peny, i])

def findContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = -1, -1, -1, -1
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            vertices = cv2.approxPolyDP(cnt, peri * 0.02, True)
            x, y, w, h = cv2.boundingRect(vertices)

    return x+w//2, y


def draw(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour, (640-point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)
        cv2.circle(pic, (640-point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)


while True:
    ret, frame = cap.read()
    if ret:
        imgContour = frame.copy()
        imgContour = cv2.flip(imgContour,1)
        # cv2.imshow('video', frame)
        findPen(frame)
        draw(drawPoints)
        cv2.imshow('contour', imgContour)
    else:
        break
    if cv2.waitKey(1) == ord('q'):
        cap.release()
        break
    if cv2.waitKey(1) == ord('s'):
        for x in range(640):
            for y in range(480):
                if pic[y,x,0]<=200 or pic[y,x,1]<=200 or pic[y,x,2]<=200:
                    pic_transparent[y+160,x+80] = [pic[y,x,0],pic[y,x,1],pic[y,x,2],255]
        cv2.imwrite('image.png', pic_transparent,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
