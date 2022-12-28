import pygame as pg
from pygame.locals import *
from pygame.transform import smoothscale, rotozoom, flip
import numpy as np
import cv2


WIDTH = 800
HEIGHT = 600
FPS = 60
FILENAME = 'warrior.png'
r = 400         #圖片大小(r,c) 感覺用400*400比較適合，先改用400*400來測
c = 400


class ch(pg.sprite.Sprite):
    
    def __init__(self):
        super(ch, self).__init__()
        self.img = cv2.imread(FILENAME,cv2.IMREAD_UNCHANGED)
        self.img = cv2.resize(self.img, (r, c), interpolation=cv2.INTER_AREA)
        #self.surf = smoothscale(pg.image.load(FILENAME), (200, 200)).convert_alpha()
        #self.surf = pg.image.load(FILENAME).convert_alpha()
        
        self.image = []
        self.imager = []
        #--------------------------------------
        ### 往左走 3點定位(左上/右上/左下) 每個陣列第一個先當原圖的點，不要改 
        l = 80 # 可依自己方便新增變數
        x1 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y1 = [0,0-30,0-40,0-50,0-50,0-50,0-50,0-40,0-30]
        x2 = [r,r,r,r,r,r,r,r,r]
        y2 = [0,0,0,0,0,0,0,0,0]
        x3 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y3 = [c,c-30,c-40,c-50,c-50,c-50,c-50,c-40,c-30]
        ### 往右走 3點定位(左上/右上/左下) 每個陣列第一個先當原圖的點，不要改 
        x4 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y4 = [0,0,0,0,0,0,0,0,0]
        x5 = [r,r,r,r,r,r,r,r,r]
        y5 = [0,0-30,0-40,0-50,0-50,0-50,0-50,0-40,0-30]
        x6 = [0,0+l,0+l,0+l,0+l,0+l,0+l,0+l,0+l]
        y6 = [c,c,c,c,c,c,c,c,c]
        #-------------------------------------- 
        p1 = np.float32([[0,0],[r,0],[0,c]])
        for i in range(1,9):
            p2 = np.float32([[x1[i],y1[i]],[x2[i],y2[i]],[x3[i],y3[i]]])
            M = cv2.getAffineTransform(p1,p2)
            newimg = cv2.warpAffine(self.img,M,(c,r))
            newimg[:, :, [0, 2]] = newimg[:, :, [2, 0]]
            self.image.append(newimg)
            p3 = np.float32([[x4[i],y4[i]],[x5[i],y5[i]],[x6[i],y6[i]]])
            M2 = cv2.getAffineTransform(p1,p3)
            newimg = cv2.warpAffine(self.img,M2,(c,r))
            newimg[:, :, [0, 2]] = newimg[:, :, [2, 0]]
            self.imager.append(newimg)


        self.size = self.img.shape[1::-1]
        self.img[:, :, [0, 2]] = self.img[:, :, [2, 0]]
        #image[1][:, :, [0, 2]] = image[1][:, :, [2, 0]]
        self.surf = (pg.image.frombuffer(self.img.flatten(), self.size, 'RGBA')).convert_alpha()
        #self.surf = pg.surfarray.make_surface(img)
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
        elif keys[pg.K_UP]:
            self.rect.move_ip((0, -5))
            self.surf = (pg.image.frombuffer(self.img.flatten(), self.size, 'RGBA')).convert_alpha()
        elif keys[pg.K_DOWN]:
            self.rect.move_ip((0, 5))
            self.surf = (pg.image.frombuffer(self.img.flatten(), self.size, 'RGBA')).convert_alpha()

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
 


if __name__ == '__main__':
    pg.init()
    pg.font.init()
    camera_mode = 0
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)    
    font_addr = pg.font.get_default_font()
    font = pg.font.Font(font_addr, 36)
    #bg = pg.Surface(screen.get_size())
    #bg = bg.convert()
    bg = smoothscale(pg.image.load("background.png"), (800, 600)).convert()
    #bg.fill((255,255,255))
    clock = pg.time.Clock()
    running = True
    character = ch()
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
            if camera_mode:
                ret,frame = cam.read()
                cv2.imshow('draw a character',frame)
            if key[K_ESCAPE]:
                camera_mode = 0
                cam.release()
                cv2.destroyAllWindows()

                       
            
    except:
        pg.quit()
        raise