import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox
import cv2
import numpy as np
import math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



def open():
    global oriph1,pho2
    file_path = filedialog.askopenfilename(filetypes = [('tif files','*.tif'),('jpg files','*.jpg')])   
    if file_path is None:
        return
    img = cv2.imread(file_path)	
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    if img.shape[0]<512:
        img=img = cv2.resize(img,(512,512),interpolation = cv2.INTER_CUBIC) 
    oriph1=img.copy()
    photo = ImageTk.PhotoImage(image = Image.fromarray(img))
    pho2 = tk.Label(window,image = photo)	
    pho2.image = photo
    pho2.place(x=100,y=30)
    afterph=oriph1.copy()

def save():
    global afterph
    f = filedialog.asksaveasfile(initialfile = 'Untitled.jpg',defaultextension=".jpg",filetypes=[("jpg files","*.jpg"),('tif files','*.tif')])
    if f is None:
        return
    cv2.imwrite(f.name,afterph)

def histogram():
    global afterph,pho2
    x,y=oriph1.shape
    ph2=oriph1.copy()
    ak=[]
    for i in range(256):
        ak.append(np.count_nonzero(oriph1 == i))
    nk=np.array(ak)
    sk=255*np.cumsum(nk)//(x*y)
    for i in range(x):
        for j in range(y):
            ph2[i,j]=sk[ph2[i,j]]
    if pho2.winfo_exists()==1:
        pho2.destroy()              
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(ph2))
    pho2 = tk.Label(window,image = photo2,height=x,width=y)	
    pho2.image = photo2
    pho2.place(x=100,y=30)
    afterph=ph2.copy()
    newh=[]
    for i in range(256):
        newh.append(np.count_nonzero(afterph == i))
    fig = Figure(figsize = (10, 5),dpi = 100)
    plot1 = fig.add_subplot(121)
    plot1.bar(range(256),nk)
    plot2 = fig.add_subplot(122)
    plot2.bar(range(256),newh)
    newWindow=tk.Toplevel(window)
    newWindow.title('histogram')
    canvas = FigureCanvasTkAgg(fig,master = newWindow)  
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=tk.YES)

def bitPlane():
    global afterph,pho2
    ph2 = oriph1.copy()
    x,y = oriph1.shape
    img = np.zeros((8,x,y),np.uint8)

    for i in range(x):
        for j in range(y):
            tempbit=np.array(list(bin(ph2[i,j])[2:]))
            bn=['0','0','0','0','0','0','0','0']
            tnum=7
            for t in range(len(tempbit)):
                bn[tnum]=tempbit[len(tempbit)-t-1]
                tnum-=1
            for th in range(8):
                if bn[th]=='1':
                    img[th,i,j]=255
                else:
                    img[th,i,j]=0
    try:                
        if pho2.winfo_exists()==1:
            pho2.destroy()     
        if int(plane.get())<0 or int(plane.get())>7:
            messagebox.showinfo("warning", "invalid value")  
        else:
            photo2 = ImageTk.PhotoImage(image = Image.fromarray(img[7-int(plane.get())]))
            pho2 = tk.Label(window,image = photo2,height=x,width=y)	
            pho2.image = photo2
            pho2.place(x=100,y=30)
    except:
        messagebox.showinfo("warning", "invalid value")

def laplacian():    
    global pho2
    ph2 = oriph1.copy()
    x,y = oriph1.shape
    img = oriph1.copy()
    try:
        num=int(shatime.get())
    except:
        messagebox.showinfo("warning", "invalid value")
        return
    ken=np.ones((num,num),dtype=float)
    ken[(num-1)//2,(num-1)//2]=0-np.sum(ken)+1
    img=cv2.filter2D(img,-1,ken)
    img+=ph2
    if pho2.winfo_exists()==1:
            pho2.destroy()     
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(img))
    pho2 = tk.Label(window,image = photo2,height=x,width=y)	
    pho2.image = photo2
    pho2.place(x=100,y=30)

def smoothmean():
    global pho2
    ph2 = oriph1.copy()
    x,y = oriph1.shape
    img = oriph1.copy()
    try:
        num=int(smotime.get())
    except:
        messagebox.showinfo("warning", "invalid value")
        return
    ken=np.ones((num,num),dtype=float)
    ken/=np.sum(ken)
    img=cv2.filter2D(ph2,-1,ken)
    if pho2.winfo_exists()==1:
            pho2.destroy()     
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(img))
    pho2 = tk.Label(window,image = photo2,height=x,width=y)	
    pho2.image = photo2
    pho2.place(x=100,y=30)

def partBavg():
    global p1,p2
    img1=piratea.copy()
    img2=pirateb.copy()
    x,y=img1.shape
    ken=np.ones((3,3),dtype=float)
    ken/=np.sum(ken)
    img1=cv2.filter2D(img1,-1,ken)
    img2=cv2.filter2D(img2,-1,ken)
    if p1.winfo_exists()==1:
            p1.destroy()   
    if p2.winfo_exists()==1:
            p2.destroy()   
    photo1 = ImageTk.PhotoImage(image = Image.fromarray(img1))
    p1 = tk.Label(window,image = photo1,height=512,width=512)	
    p1.image = photo1
    p1.place(x=800,y=30)
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(img2))
    p2 = tk.Label(window,image = photo2,height=512,width=512)	
    p2.image = photo2
    p2.place(x=1320,y=30)

def partBmed():
    global p1,p2,last1,last2
    img1=piratea.copy()
    img2=pirateb.copy()
    x,y=img1.shape
    for i in range(1,x-1):
        for j in range(1,y-1):
            nine=[piratea[i-1,j-1],piratea[i-1,j],piratea[i-1,j+1],piratea[i,j-1],piratea[i,j],piratea[i,j+1],piratea[i+1,j-1],piratea[i+1,j],piratea[i+1,j+1]]
            med=np.median(nine)
            img1[i,j]=med
            nine2=[pirateb[i-1,j-1],pirateb[i-1,j],pirateb[i-1,j+1],pirateb[i,j-1],pirateb[i,j],pirateb[i,j+1],pirateb[i+1,j-1],pirateb[i+1,j],pirateb[i+1,j+1]]
            med2=np.median(nine2)
            img2[i,j]=med2
    if p1.winfo_exists()==1:
            p1.destroy()   
    if p2.winfo_exists()==1:
            p2.destroy()   
    photo1 = ImageTk.PhotoImage(image = Image.fromarray(img1))
    p1 = tk.Label(window,image = photo1,height=512,width=512)	
    p1.image = photo1
    p1.place(x=800,y=30)
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(img2))
    p2 = tk.Label(window,image = photo2,height=512,width=512)	
    p2.image = photo2
    p2.place(x=1320,y=30)
    last1=img1.copy()
    last2=img2.copy()

def partBlap():
    global p1,p2,last1,last2
    partBmed()
    img1=last1.copy()
    img2=last2.copy()

    x,y=img1.shape
    ken=np.ones((3,3),dtype=float)
    ken[1,1]=-8
    img1=cv2.filter2D(img1,-1,ken)
    img2=cv2.filter2D(img2,-1,ken)
    
    if p1.winfo_exists()==1:
            p1.destroy()   
    if p2.winfo_exists()==1:
            p2.destroy()    
    photo1 = ImageTk.PhotoImage(image = Image.fromarray(img1))
    p1 = tk.Label(window,image = photo1,height=512,width=512)	
    p1.image = photo1
    p1.place(x=800,y=30)
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(img2))
    p2 = tk.Label(window,image = photo2,height=512,width=512)	
    p2.image = photo2
    p2.place(x=1320,y=30)

window=tk.Tk()
window.title('hw1')
window.geometry('1920x900')	
piratea= np.fromfile('pirate_a.raw',dtype='uint8')
piratea=piratea.reshape(512,512)
pir1 = ImageTk.PhotoImage(image = Image.fromarray(piratea))
p1 = tk.Label(window,image = pir1)	
p1.image = pir1
p1.place(x=800,y=30)
pirateb = np.fromfile('pirate_b.raw',dtype='uint8')
pirateb=pirateb.reshape(512,512)
pir2 = ImageTk.PhotoImage(image = Image.fromarray(pirateb))
p2 = tk.Label(window,image = pir2)	
p2.image = pir2
p2.place(x=1320,y=30)
medfilter=tk.Button(window,text='average mask',width=10,height=1,command=partBavg)
medfilter.place(x=800,y=600)
medfilter=tk.Button(window,text='median filter',width=10,height=1,command=partBmed)
medfilter.place(x=800,y=630)
sha=tk.Button(window,text='laplacian',width=10,height=1,command=partBlap)
sha.place(x=800,y=660)
t4=tk.Label(window,text='(using median filter)')
t4.place(x=920,y=665)
bt1=tk.Button(window,text='open',width=2,height=1,command=open)
bt1.place(x=0,y=0)
bt2=tk.Button(window,text='save',width=2,height=1,command=save)
bt2.place(x=45,y=0)  

plane=tk.Entry(window,width=10)
plane.place(x=200,y=640)
confirm=tk.Button(window,text='auto-level',width=7,height=1,command=histogram)
confirm.place(x=500,y=600)
bitplane=tk.Button(window,text='bit-plane',width=7,height=1,command=bitPlane)
bitplane.place(x=500,y=640)
smo=tk.Button(window,text='smoothing',width=7,height=1,command=smoothmean)
smo.place(x=500,y=680)
smotime=tk.Entry(window,width=10)
smotime.place(x=200,y=680)
sha=tk.Button(window,text='sharpening',width=7,height=1,command=laplacian)
sha.place(x=500,y=720)
shatime=tk.Entry(window,width=10)
shatime.place(x=200,y=720)

partA=tk.Label(window,text='Part A',font=('Arail',18))
partA.place(x=100)
partB=tk.Label(window,text='Part B',font=('Arail',18))
partB.place(x=800)

l1=tk.Label(window,text='histogram : ')
l1.place(x=100,y=600)
l2=tk.Label(window,text='Bit-Plane : ')
l2.place(x=100,y=640)
l3=tk.Label(window,text='Smoothing : ')
l3.place(x=100,y=680)
l4=tk.Label(window,text='Sharpening : ')
l4.place(x=100,y=720)
t1=tk.Label(window,text='(0~7th plane)')
t1.place(x=300,y=640)
t2=tk.Label(window,text='(x*x size)')
t2.place(x=300,y=680)
t3=tk.Label(window,text='(x*x size)')
t3.place(x=300,y=720)



window.mainloop()
