import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox
import cv2
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure




def part1():
    
    img = cv2.imread('BarTest.tif')	
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    newWindow=tk.Toplevel(window)
    newWindow.title('part1')    
    newWindow.geometry('900x600')
    ken1=np.ones((7,7),dtype=float)
    ken1/=np.sum(ken1)
    mean7=cv2.filter2D(img,-1,ken1)
    ken2=np.ones((3,3),dtype=float)
    ken2/=np.sum(ken2)
    mean3=cv2.filter2D(img,-1,ken2)
    x,y=img.shape
    med3=img.copy()
    for i in range(1,x-1):
        for j in range(1,y-1):
            nine=[img[i-1,j-1],img[i-1,j],img[i-1,j+1],img[i,j-1],img[i,j],img[i,j+1],img[i+1,j-1],img[i+1,j],img[i+1,j+1]]
            med=np.median(nine)
            med3[i,j]=med
            
    med7=img.copy()
    for i in range(3,x-3):
        for j in range(3,y-3):
            nine=[img[i-3,j-3],img[i-3,j-2],img[i-3,j-1],img[i-3,j],img[i-3,j+1],img[i-3,j+2],img[i-3,j+3],
            img[i-2,j-3],img[i-2,j-2],img[i-2,j-1],img[i-2,j],img[i-2,j+1],img[i-2,j+2],img[i-2,j+3],
            img[i-1,j-3],img[i-1,j-2],img[i-1,j-1],img[i-1,j],img[i-1,j+1],img[i-1,j+2],img[i-1,j+3],
            img[i,j-3],img[i,j-2],img[i,j-1],img[i,j],img[i,j+1],img[i,j+2],img[i,j+3],
            img[i+1,j-3],img[i+1,j-2],img[i+1,j-1],img[i+1,j],img[i+1,j+1],img[i+1,j+2],img[i+1,j+3],
            img[i+2,j-3],img[i+2,j-2],img[i+2,j-1],img[i+2,j],img[i+2,j+1],img[i+2,j+2],img[i+2,j+3],
            img[i+3,j-3],img[i+3,j-2],img[i+3,j-1],img[i+3,j],img[i+3,j+1],img[i+3,j+2],img[i+3,j+3],]
            med=np.median(nine)
            med7[i,j]=med

    photo1 = ImageTk.PhotoImage(image = Image.fromarray(img))
    p1 = tk.Label(newWindow,image = photo1)	
    p1.image = photo1
    p1.place(x=10,y=10)
    
    
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(mean7))
    p2 = tk.Label(newWindow,image = photo2)	
    p2.image = photo2
    p2.place(x=300,y=10)
    l2 = tk.Label(newWindow,text = 'mean 7*7',font = ('Arial',13))
    l2.place(x=300,y=270)

    photo3 = ImageTk.PhotoImage(image = Image.fromarray(med7))
    p3 = tk.Label(newWindow,image = photo3)	
    p3.image = photo3
    p3.place(x=300,y=300)
    l2 = tk.Label(newWindow,text = 'median 7*7',font = ('Arial',13))
    l2.place(x=300,y=560)

    photo4 = ImageTk.PhotoImage(image = Image.fromarray(mean3))
    p4 = tk.Label(newWindow,image = photo4)	
    p4.image = photo4
    p4.place(x=600,y=10)
    l2 = tk.Label(newWindow,text = 'mean 3*3',font = ('Arial',13))
    l2.place(x=600,y=270)

    photo5 = ImageTk.PhotoImage(image = Image.fromarray(med3))
    p5 = tk.Label(newWindow,image = photo5)	
    p5.image = photo5
    p5.place(x=600,y=300)
    l2 = tk.Label(newWindow,text = 'median 3*3',font = ('Arial',13))
    l2.place(x=600,y=560)


def part2():
    img = cv2.imread('lenna.tif')	
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    newWindow2=tk.Toplevel(window)
    newWindow2.title('part2')    
    newWindow2.geometry('1800x600')

    
    #f = np.fft.fft2(img)
    fshift = np.fft.fftshift(np.fft.fft2(img))	
    ff = 20*np.log(np.abs(fshift))
    phase = np.angle(fshift)
    phase = np.abs(np.fft.ifft2(np.fft.ifftshift(phase)))
    phase = 20*np.log(phase)
    iimg = np.fft.ifft2(np.fft.ifftshift(np.abs(fshift)))
    iimg = np.abs(iimg)
    photo5 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(ff)))
    p5 = tk.Label(newWindow2,image = photo5)	
    p5.image = photo5
    p5.place(x=10,y=10)
    photo4 = ImageTk.PhotoImage(image = Image.fromarray(np.uint8(phase)))
    p4 = tk.Label(newWindow2,image = photo4)	
    p4.image = photo4
    p4.place(x=1200,y=10)
    photo3 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(iimg)))
    p3 = tk.Label(newWindow2,image = photo3)	
    p3.image = photo3
    p3.place(x=600,y=10)
    l2 = tk.Label(newWindow2,text = '(a) spectrum image',font = ('Arial',13))
    l2.place(x=10,y=530)
    l2 = tk.Label(newWindow2,text = '(b) magnitude image (after inverse fft)',font = ('Arial',13))
    l2.place(x=600,y=530)
    l2 = tk.Label(newWindow2,text = '(b) phase image (after inverse fft)',font = ('Arial',13))
    l2.place(x=1200,y=530)


def part3():
    img = cv2.imread('DIP_image.tif',cv2.IMREAD_GRAYSCALE)	
    newWindow3=tk.Toplevel(window)
    newWindow3.title('part3')    
    newWindow3.geometry('1920x1080')
    dimg=img.copy()
    x,y=img.shape
    for i in range(x):
        for j in range(y):
            dimg[i,j]=img[i,j]*(-1)**(i+j)
    
    dft = np.fft.fftshift(cv2.dft(np.float32(dimg),flags=cv2.DFT_COMPLEX_OUTPUT))
    dftp= 10*np.log(cv2.magnitude(dft[:,:,0],dft[:,:,1]))
    dft[:,:,1]=dft[:,:,1]*(-1)
    dftcp = 10*np.log(cv2.magnitude(dft[:,:,0],dft[:,:,1]))    
    dfti = cv2.idft(np.fft.ifftshift(dft),flags=cv2.DFT_COMPLEX_OUTPUT)
    dftip = cv2.magnitude(dfti[:,:,0],dfti[:,:,1])
    
    for i in range(x):
        for j in range(y):
            dfti[i,j,0]=dfti[i,j,0]*(-1)**(i+j)
    
    photo3 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(dfti[:,:,0])))    #real
    p3 = tk.Label(newWindow3,image = photo3)	
    p3.image = photo3
    p3.place(x=600,y=450)
    photo4 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(dftip)))      #idft
    p4 = tk.Label(newWindow3,image = photo4)	
    p4.image = photo4
    p4.place(x=10,y=450)
    photo5 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(dftcp)))      #conjugate
    p5 = tk.Label(newWindow3,image = photo5)	
    p5.image = photo5
    p5.place(x=1200,y=0)
    photo6 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(dftp)))       #dft
    p6 = tk.Label(newWindow3,image = photo6)	
    p6.image = photo6
    p6.place(x=600,y=0)
    photo7 = ImageTk.PhotoImage(image = Image.fromarray(np.uint32(dimg)))       #-1
    p7 = tk.Label(newWindow3,image = photo7)	
    p7.image = photo7
    p7.place(x=10,y=0)
    l2 = tk.Label(newWindow3,text = '(1) multiply (-1)^(x+y)      (2) DFT      (3) take complex conjugate',font = ('Arial',13))
    l2.place(x=1200,y=550)
    l2 = tk.Label(newWindow3,text = '(4) inverse DFT      (5) real part multiply (-1)^(x+y) ',font = ('Arial',13))
    l2.place(x=1200,y=600)


def part4():
    global aimg
    img = cv2.imread('Lenna_512_color.tif',cv2.IMREAD_COLOR)
    newWindow4=tk.Toplevel(window)
    newWindow4.title('part4')    
    newWindow4.geometry('1920x1080')
    imgg=img.copy()
    imgg[:,:,2]=img[:,:,0]
    imgg[:,:,0]=img[:,:,2]
    imgr = imgg.copy()
    imgr[:,:,1:] = 0
    imgG = imgg.copy()
    imgG[:,:,0] = 0
    imgG[:,:,2] = 0
    imgb = imgg.copy()
    imgb[:,:,:2] = 0
    imgg=cv2.resize(imgg,(450,450),interpolation = cv2.INTER_LINEAR)
    imgr=cv2.resize(imgr,(200,200),interpolation = cv2.INTER_LINEAR)
    imgG=cv2.resize(imgG,(200,200),interpolation = cv2.INTER_LINEAR)
    imgb=cv2.resize(imgb,(200,200),interpolation = cv2.INTER_LINEAR)
    photo1 = ImageTk.PhotoImage(image = Image.fromarray(imgg))
    p1 = tk.Label(newWindow4,image = photo1)	
    p1.image = photo1
    p1.place(x=10,y=0)
    l1 = tk.Label(newWindow4,text = '(a) origin image',font = ('Arial',13))
    l1.place(x=10,y=450)
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(imgr))
    p2 = tk.Label(newWindow4,image = photo2)	
    p2.image = photo2
    p2.place(x=550,y=0)
    l2 = tk.Label(newWindow4,text = '(b) red, grean, blue component',font = ('Arial',13))
    l2.place(x=550,y=200)
    photo3 = ImageTk.PhotoImage(image = Image.fromarray(imgG))
    p3 = tk.Label(newWindow4,image = photo3)	
    p3.image = photo3
    p3.place(x=750,y=0)
    photo4 = ImageTk.PhotoImage(image = Image.fromarray(imgb))
    p4 = tk.Label(newWindow4,image = photo4)	
    p4.image = photo4
    p4.place(x=950,y=0)

    imgone = cv2.cvtColor(imgg, cv2.COLOR_RGB2GRAY)
    imgi = imgone.copy()
    aimg = imgg.copy()
    imgg = imgg/255
    imgi = ((imgg[:,:,0]+imgg[:,:,1]+imgg[:,:,2])/3)*255
    imgs = imgone.copy()
    imgh = imgone.copy()
    x,y=imgone.shape 
    for i in range(x):
        for j in range(y):
            rgb=imgg[i,j,0]+imgg[i,j,1]+imgg[i,j,2]
            if rgb == 0 :
                imgs[i,j] = 0
            else :
                imgs[i,j] = 1-(3*min(imgg[i,j,0],imgg[i,j,1],imgg[i,j,2])/rgb)*255
                
            thm = np.sqrt((imgg[i,j,0]-imgg[i,j,1])**2+(imgg[i,j,0]-imgg[i,j,2])*(imgg[i,j,1]-imgg[i,j,2]))
            if thm == 0:
                theta = 0
            else : 
                theta = math.degrees(np.arccos(0.5 * ((imgg[i,j,0]-imgg[i,j,1])+(imgg[i,j,0]-imgg[i,j,2]))/thm))
            if imgg[i,j,2]<=imgg[i,j,1]:
                imgh[i,j] = theta/360*255
            else:
                imgh[i,j] = (360-theta)/360*255
    dmg = 255-aimg[:,:,:]


    imgip=cv2.resize(imgi,(200,200),interpolation = cv2.INTER_LINEAR)
    photo5 = ImageTk.PhotoImage(image = Image.fromarray(imgip))
    p5 = tk.Label(newWindow4,image = photo5)	
    p5.image = photo5
    p5.place(x=950,y=250)
    l3 = tk.Label(newWindow4,text = '(c) hue, saturation, intensity component',font = ('Arial',13))
    l3.place(x=550,y=450)
    imgsp=cv2.resize(imgs,(200,200),interpolation = cv2.INTER_LINEAR)
    photo6 = ImageTk.PhotoImage(image = Image.fromarray(imgsp))
    p6 = tk.Label(newWindow4,image = photo6)	
    p6.image = photo6
    p6.place(x=750,y=250)
    imghp=cv2.resize(imgh,(200,200),interpolation = cv2.INTER_LINEAR)
    photo7 = ImageTk.PhotoImage(image = Image.fromarray(imghp))
    p7 = tk.Label(newWindow4,image = photo7)	
    p7.image = photo7
    p7.place(x=550,y=250)
    dmg=cv2.resize(dmg,(450,450),interpolation = cv2.INTER_LINEAR)
    photo8 = ImageTk.PhotoImage(image = Image.fromarray(dmg))
    p8 = tk.Label(newWindow4,image = photo8)	
    p8.image = photo8
    p8.place(x=1230,y=0)
    l3 = tk.Label(newWindow4,text = '(d) color complements',font = ('Arial',13))
    l3.place(x=1230,y=450)    

    btn1 = tk.Button(newWindow4,text = 'go to part (e)',command = parte)
    btn1.place(x=20,y=550)
    limg=aimg.copy()
    
    x2,y2,c2=aimg.shape
    for i in range(x2):
        for j in range(y2):
            if imgh[i,j]<175 or imgh[i,j]>225:
                limg[i,j,:]=0
            if imgs[i,j] < 35 or imgs[i,j] > 165:
                limg[i,j,:]=0

    
    limg=cv2.resize(limg,(300,300),interpolation = cv2.INTER_LINEAR)
    lphoto = ImageTk.PhotoImage(image = Image.fromarray(limg))
    lp = tk.Label(newWindow4,image = lphoto)	
    lp.image = lphoto
    lp.place(x=550,y=500)
    l3 = tk.Label(newWindow4,text = '(f) feather',font = ('Arial',13))
    l3.place(x=550,y=800) 

def parte():
    global aimg,rhme,rhla
    newWindow5=tk.Toplevel(window)
    newWindow5.title('part(e)')    
    newWindow5.geometry('1920x1080')
    hsim = cv2.cvtColor(aimg, cv2.COLOR_RGB2HSV)
    ker=np.ones((5,5),dtype=float)
    ker/=np.sum(ker)
    rgbmean5=cv2.filter2D(aimg,-1,ker)
    hsimean5=cv2.filter2D(hsim,-1,ker)
    lap=[[0,0,1,0,0],[0,1,2,1,0],[1,2,-16,2,1],[0,1,2,1,0],[0,0,1,0,0]]
    lap=np.asarray(lap)
    rgblap=cv2.filter2D(aimg,-1,lap)
    hsimlap=cv2.filter2D(hsim,-1,lap)
    rgbmp=cv2.resize(aimg,(250,250),interpolation = cv2.INTER_LINEAR)
    photo8 = ImageTk.PhotoImage(image = Image.fromarray(rgbmp))
    p8 = tk.Label(newWindow5,image = photo8)	
    p8.image = photo8
    p8.place(x=100,y=30)
    l8 = tk.Label(newWindow5,text = 'RGB',font = ('Arial',13))
    l8.place(x=30,y=130) 
    hsimp=cv2.cvtColor(hsim, cv2.COLOR_HSV2RGB)
    hsimp=cv2.resize(hsimp,(250,250),interpolation = cv2.INTER_LINEAR)
    
    photo9 = ImageTk.PhotoImage(image = Image.fromarray(hsimp))
    p9 = tk.Label(newWindow5,image = photo9)	
    p9.image = photo9
    p9.place(x=100,y=280)
    l9 = tk.Label(newWindow5,text = 'HSI',font = ('Arial',13))
    l9.place(x=30,y=400) 
    l10 = tk.Label(newWindow5,text = 'origin',font = ('Arial',13))
    l10.place(x=195,y=0) 
    l11 = tk.Label(newWindow5,text = '5*5 mean',font = ('Arial',13))
    l11.place(x=445,y=0) 
    l12 = tk.Label(newWindow5,text = 'laplacian',font = ('Arial',13))
    l12.place(x=695,y=0) 
    rgbmean5=cv2.resize(rgbmean5,(250,250),interpolation = cv2.INTER_LINEAR)
    photo10 = ImageTk.PhotoImage(image = Image.fromarray(rgbmean5))
    p10 = tk.Label(newWindow5,image = photo10)	
    p10.image = photo10
    p10.place(x=350,y=30)
    hsimean5=cv2.cvtColor(hsimean5, cv2.COLOR_HSV2RGB)
    hsimean5=cv2.resize(hsimean5,(250,250),interpolation = cv2.INTER_LINEAR)

    photo11 = ImageTk.PhotoImage(image = Image.fromarray(hsimean5))
    p11 = tk.Label(newWindow5,image = photo11)	
    p11.image = photo11
    p11.place(x=350,y=280)
    rgblap=cv2.resize(rgblap,(250,250),interpolation = cv2.INTER_LINEAR)
    photo12 = ImageTk.PhotoImage(image = Image.fromarray(rgblap))
    p12 = tk.Label(newWindow5,image = photo12)	
    p12.image = photo12
    p12.place(x=600,y=30)

    hsimlap=cv2.cvtColor(hsimlap, cv2.COLOR_HSV2RGB)
    hsimlap=cv2.resize(hsimlap,(250,250),interpolation = cv2.INTER_LINEAR)
    photo13 = ImageTk.PhotoImage(image = Image.fromarray(hsimlap))
    p13 = tk.Label(newWindow5,image = photo13)	
    p13.image = photo13
    p13.place(x=600,y=280)
    l12 = tk.Label(newWindow5,text = 'origin vs. 5*5mean',font = ('Arial',13))
    l12.place(x=1155,y=0) 
    l13 = tk.Label(newWindow5,text = 'origin vs. laplacian',font = ('Arial',13))
    l13.place(x=1395,y=0) 
    photo1 = ImageTk.PhotoImage(image = Image.fromarray(rgbmp-rgbmean5))
    p1 = tk.Label(newWindow5,image = photo1)	
    p1.image = photo1
    p1.place(x=1100,y=30)
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(rgbmp-rgblap))
    p2 = tk.Label(newWindow5,image = photo2)	
    p2.image = photo2
    p2.place(x=1350,y=30)
    photo3 = ImageTk.PhotoImage(image = Image.fromarray(hsimp-hsimean5))
    p3 = tk.Label(newWindow5,image = photo3)	
    p3.image = photo3
    p3.place(x=1100,y=280)
    photo4 = ImageTk.PhotoImage(image = Image.fromarray(hsimp-hsimlap))
    p4 = tk.Label(newWindow5,image = photo4)	
    p4.image = photo4
    p4.place(x=1350,y=280)

    rhme=rgbmean5-hsimean5
    photo7 = ImageTk.PhotoImage(image = Image.fromarray(rhme))
    p7 = tk.Label(newWindow5,image = photo7)	
    p7.image = photo7
    p7.place(x=350,y=530)
    rhla=rgblap-hsimlap
    photo88 = ImageTk.PhotoImage(image = Image.fromarray(rhla))
    p88 = tk.Label(newWindow5,image = photo88)	
    p88.image = photo88
    p88.place(x=600,y=530)
    l20 = tk.Label(newWindow5,text = 'RGB mean vs. HSI mean -->',font = ('Arial',13))
    l20.place(x=100,y=600) 
    l21 = tk.Label(newWindow5,text = '<-- RGB laplacian vs. HSI laplacian',font = ('Arial',13))
    l21.place(x=860,y=600) 
    l22 = tk.Label(newWindow5,text = 'RGB',font = ('Arial',13))
    l22.place(x=1060,y=130) 
    l23 = tk.Label(newWindow5,text = 'HSI',font = ('Arial',13))
    l23.place(x=1060,y=400) 


window=tk.Tk()
window.title('hw3')
window.geometry('150x300')	

bt1=tk.Button(window,text='part1',width=2,height=1,command=part1)
bt1.place(x=50,y=50)
bt2=tk.Button(window,text='part2',width=2,height=1,command=part2)
bt2.place(x=50,y=100) 
bt2=tk.Button(window,text='part3',width=2,height=1,command=part3)
bt2.place(x=50,y=150) 
bt2=tk.Button(window,text='part4',width=2,height=1,command=part4)
bt2.place(x=50,y=200) 

window.mainloop()
