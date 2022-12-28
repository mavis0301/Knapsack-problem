import pygame as pg
from pygame.locals import *
from pygame.transform import smoothscale, rotozoom, flip
import numpy as np
import cv2


WIDTH = 800
HEIGHT = 600
FPS = 60
FILENAME = 'warrior.png'
r = 400         #圖片大小(r,c) 
c = 400 

# Blue[86, 121, 205, 111, 245, 255],[255, 0, 0],
# Green[46, 78, 204, 71, 255, 255],[0, 255, 0]
# Yellow blue green red gold
penColorHSV = [[14,155,142,26,255,255],
            [99,162,0,109,255,255],
            [35,66,108,92,240,255],
            [140,149,65,179,255,255]
            ]

penColorBGR = [[0,225,255],
            [198,151,44],
            [44,198,117],
            [40,60,250]]
pic = np.zeros((480,640,3),np.uint8)
pic.fill(255)
pic_transparent = np.zeros((800,800,4),np.uint8)
# [x, y, colorId]
drawPoints = []


class ch(pg.sprite.Sprite):
    
    def __init__(self,filename):
        super(ch, self).__init__()
        self.img = cv2.imread(filename,cv2.IMREAD_UNCHANGED)
        self.img = cv2.resize(self.img, (r, c), interpolation=cv2.INTER_AREA)

        
        self.image = []
        self.imager = []
        #--------------------------------------
        ### 往左走 3點定位(左上/右上/左下) 
        l = 50 
        
        x1 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y1 = [0,0-30,0-35,0-40,0-50,0-50,0-50,0-50,0-40,0-35,0-30]
        x2 = [r,r,r,r,r,r,r,r,r,r,r]
        y2 = [0,0,0,0,0,0,0,0,0,0,0]
        x3 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y3 = [c,c-30,c-35,c-40,c-50,c-50,c-50,c-50,c-40,c-35,c-30]
        ### 往右走 3點定位(左上/右上/左下) 
        x4 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y4 = [0,0,0,0,0,0,0,0,0,0,0]
        x5 = [r,r,r,r,r,r,r,r,r,r,r]
        y5 = [0,0-30,0-35,0-40,0-50,0-50,0-50,0-50,0-40,0-35,0-30]
        x6 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y6 = [c,c,c,c,c,c,c,c,c,c,c]
        #-------------------------------------- 
        p1 = np.float32([[0,0],[r,0],[0,c]])
        self.img_right=cv2.flip(self.img,1,dst=None)
        for i in range(1,11):
            p2 = np.float32([[x1[i],y1[i]],[x2[i],y2[i]],[x3[i],y3[i]]])
            M = cv2.getAffineTransform(p1,p2)
            newimg = cv2.warpAffine(self.img,M,(c,r))
            newimg[:, :, [0, 2]] = newimg[:, :, [2, 0]]
            self.image.append(newimg)

            p3 = np.float32([[x4[i],y4[i]],[x5[i],y5[i]],[x6[i],y6[i]]])
            M2 = cv2.getAffineTransform(p1,p3)
            newimg = cv2.warpAffine(self.img_right,M2,(c,r))
            newimg[:, :, [0, 2]] = newimg[:, :, [2, 0]]
            self.imager.append(newimg)


        self.size = self.img.shape[1::-1]
        self.img[:, :, [0, 2]] = self.img[:, :, [2, 0]]

        self.surf = (pg.image.frombuffer(self.img.flatten(), self.size, 'RGBA')).convert_alpha()
        self.rect = self.surf.get_rect(center=(300, 500))  # 中心定位
        self.now = 0
        self.direct = 0

    def update(self, keys):
        global testx,testy
        if keys[pg.K_LEFT]:
            self.rect.move_ip((-2, 0))
            if self.direct == 1:
                self.direct = 0
                self.now = 0
            self.surf = (pg.image.frombuffer(self.image[self.now].flatten(), self.size, 'RGBA')).convert_alpha()
            self.now +=1
            if self.now >7:
                self.now = 0
        elif keys[pg.K_RIGHT]:
            self.rect.move_ip((2, 0))
            if self.direct == 0:
                self.direct = 1
                self.now = 0
            self.surf = (pg.image.frombuffer(self.imager[self.now].flatten(), self.size, 'RGBA')).convert_alpha()
            self.now +=1
            if self.now >7:
                self.now = 0
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600


class button(pg.sprite.Sprite):
    def __init__(self,text,x,y):
        self.surf = font.render(text, True,(255,255,255))
        self.width = 200
        self.height = 100
        self.x = x
        self.y = y
        self.text = text
    def click(self,pos):
        x_match = pos[0] > self.x and pos[0] < self.x+200
        y_match = pos[1] > self.y and pos[1] < self.y+30
        if x_match and y_match:
            return True
        else:
            return False
    def touch(self,check = False):
        if check:
            self.surf = font.render(self.text,True,(255,0,0))
        else:
            self.surf = font.render(self.text,True,(255,255,255))


def initcamera():
    global pic ,pic_transparent,drawPoints
    pic = np.zeros((480,640,3),np.uint8)
    pic.fill(255)
    pic_transparent = np.zeros((800,800,4),np.uint8)
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


def drawpicture(drawpoints):
    for point in drawpoints:
        cv2.circle(imgContour, (640-point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)
        cv2.circle(pic, (640-point[0], point[1]), 10, penColorBGR[point[2]], cv2.FILLED)



if __name__ == '__main__':
    pg.init()
    pg.font.init()
    camera_mode = 0
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)    
    font_addr = pg.font.get_default_font()
    font = pg.font.Font(font_addr, 36)
    bg = smoothscale(pg.image.load("background.png"), (800, 600)).convert()
    clock = pg.time.Clock()
    running = True
    character = ch(FILENAME)
    draw = button('CREATE',200,200)
    
    try:
        while running:
            clock.tick(FPS)       
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            screen.blit(bg, (0,0))             
            key = pg.key.get_pressed()
            character.update(key)
            screen.blit(character.surf,character.rect)
            screen.blit(draw.surf,(draw.x,draw.y))
            pg.display.flip()
            if draw.click(pg.mouse.get_pos()):
                draw.touch(True)   
            else:
                draw.touch()
            if pg.mouse.get_pressed()[0]:
                if draw.click(pg.mouse.get_pos()):
                    cam = cv2.VideoCapture(0)
                    camera_mode = 1
                    initcamera()
            if camera_mode:                
                ret,frame = cam.read()
                if ret:
                    imgContour = frame.copy()
                    imgContour = cv2.flip(imgContour,1)
                    findPen(frame)
                    drawpicture(drawPoints)
                    cv2.imshow('contour', imgContour)
                else:
                    break
            if key[K_ESCAPE]:
                camera_mode = 0
                for x in range(640):
                    for y in range(480):
                        if pic[y,x,0]<=200 or pic[y,x,1]<=200 or pic[y,x,2]<=200:
                            pic_transparent[y+160,x+80] = [pic[y,x,0],pic[y,x,1],pic[y,x,2],255]
                cv2.imwrite('image.png', pic_transparent,[int(cv2.IMWRITE_PNG_COMPRESSION), 0])
                cam.release()
                cv2.destroyAllWindows()
                character = ch('image.png')

                       
            
    except:
        pg.quit()
        raise