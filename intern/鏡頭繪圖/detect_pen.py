import cv2
import numpy as np

def empty(v):
    pass


cap = cv2.VideoCapture(0)

#創建一個trackerbar的視窗 用來調整hsv的數值
#因為不知道所要過濾顏色的hsv 所以用這個方式可以即時改變hsv的值 即時看到是否符合結果
cv2.namedWindow('TrackBar')
#視窗大小
cv2.resizeWindow('TrackBar', 640, 320)

#hue的值最大值到179 s 跟 v 最大值到255
#創建trackebar
cv2.createTrackbar('Hue Min', 'TrackBar', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBar', 179, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBar', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBar', 0, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBar', 255, 255, empty)

#hsv比rgb更容易過濾顏色
#hue 色調 saturation 飽和度 value 亮度

while True:
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBar')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBar')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBar')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBar')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBar')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBar')
    print(h_min, h_max, s_min, s_max, v_min, v_max)

    ret , img = cap.read()
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #要是個陣列
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    #製作遮罩 (圖片,hsv的最小值,hsv的最大值)
    #變成黑色的地方是過濾掉的地方
    #變成白色的地方是我們要偵測的地方
    mask = cv2.inRange(hsv, lower, upper)

    #將遮罩套入原圖 產出 result 過濾掉的圖片
    #bitwise_and 計算方式
    # 0 0 =0
    # 1 0 =0
    # 0 1 =0
    # 1 1 =1
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('img', img)
    # cv2.imshow('hsv', hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('reslut', result)
    cv2.waitKey(1)