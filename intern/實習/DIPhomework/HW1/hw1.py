import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog,messagebox
import cv2
import numpy as np
import math


def open():
    global oriph1,pho2
    file_path = filedialog.askopenfilename(filetypes = [('tif files','*.tif'),('jpg files','*.jpg')])   
    if file_path is None:
        return
    img = cv2.imread(file_path)	
    img = cv2.resize(img,(300,300),interpolation = cv2.INTER_CUBIC)     #type=nparray
    oriph1=img.copy()
    photo = ImageTk.PhotoImage(image = Image.fromarray(img))
    ph1 = tk.Label(window,image = photo)	
    ph1.image = photo
    ph1.place(x=100)
    pho2 = tk.Label(window,image = photo)	
    pho2.image = photo
    pho2.place(x=400)
    afterph=oriph1.copy()
	

def save():
    f = filedialog.asksaveasfile(initialfile = 'Untitled.jpg',defaultextension=".jpg",filetypes=[("jpg files","*.jpg"),('tif files','*.tif')])
    if f is None:
        return
    cv2.imwrite(f.name,afterph)

def contrast():
    global afterph,pho2
    x,y,c=oriph1.shape
    ph2=oriph1.copy()
    try:
        if not(mod.get() == 'logarithmically' and float(valb.get())<=1):
            for i in range(x):
                for j in range(y):
                    for k in range(c):
                        if mod.get() == 'linearly':
                            new = oriph1[i,j,k]*float(vala.get())+float(valb.get())
                        elif mod.get() == 'exponentially':
                            new = math.exp(oriph1[i,j,k]*float(vala.get())+float(valb.get()))
                        else :
                            new = math.log((oriph1[i,j,k]*float(vala.get())+float(valb.get()))/255)*255
                        if new > 255:
                            ph2[i,j,k]=255
                        elif new < 0:
                            ph2[i,j,k]=0
                        else:
                            ph2[i,j,k]=new            
        else:
            messagebox.showinfo("warning", "b must be greater than 1")
        afterph=ph2.copy()    
    except:
        messagebox.showinfo("warning", "invalid value")
        afterph=oriph1.copy()

def zoom():
    global afterph,pho2
    h,w,c = afterph.shape
    ori=np.pad(afterph,((0,1),(0,1),(0,0)),'constant')
    nh = int(h*float(valz.get()))
    nw = int(w*float(valz.get()))
    img = np.zeros((nh,nw,3),np.uint8)
    for k in range(3):
        for i in range(nh):
            for j in range(nw):
                x = (i+0.5)*(h/nh)-0.5
                y = (j+0.5)*(w/nw)-0.5
                p1 = (math.floor(x),math.floor(y))
                p2 = (p1[0],p1[1]+1)
                p3 = (p1[0]+1,p1[1])
                p4 = (p1[0]+1,p1[1]+1)
                l = x-p1[0]
                m = u=p1[1]
                img[i,j,k] = (p3[0]-x)*((p2[1]-y)*ori[p1[0],p1[1],k]+(y-p1[1])*ori[p2[0],p2[1],k])+(x-p1[0])*((p2[1]-y)*ori[p3[0],p3[1],k]+(y-p1[1])*ori[p4[0],p4[1],k])
    #img=img[:300,:300,:]
    afterph=img.copy()            

def rotate():
    global afterph,pho2
    h,w,c=afterph.shape
    center= (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, float(rot.get()), 1.0)
    img = cv2.warpAffine(afterph, M, (w, h))
    afterph=img.copy()  
    



def gray():
    global afterph,pho2
    contrast()
    zoom()
    rotate()
    x,y,c=afterph.shape
    ph2=afterph.copy()
    
    for i in range(x):
        for j in range(y):
            for k in range(c):
                if ph2[i,j,k] < int(minr.get()) or ph2[i,j,k] > int(maxr.get()):
                    if(mod2.get()=='black'):
                        ph2[i,j,k]=0
    if pho2.winfo_exists()==1:
        pho2.destroy()              
    photo2 = ImageTk.PhotoImage(image = Image.fromarray(ph2))
    pho2 = tk.Label(window,image = photo2,height=300,width=300)	
    pho2.image = photo2
    pho2.place(x=400)
    afterph=ph2.copy()
    



window=tk.Tk()
window.title('hw1')
window.geometry('800x600')
bt1=tk.Button(window,text='open',width=2,height=1,command=open)
bt1.place(x=0,y=0)
bt2=tk.Button(window,text='save',width=2,height=1,command=save)
bt2.place(x=45,y=0)
optionList = ['linearly','exponentially','logarithmically']   
mod = tk.StringVar()                                        
mod.set('linearly')
menu = tk.OptionMenu(window, mod, *optionList)                
menu.place(x=150,y=395)
vala=tk.Entry(window,width=10)
vala.place(x=330,y=400)
valb=tk.Entry(window,width=10)
valb.place(x=460,y=400)
lbla=tk.Label(window,text='a= ')
lbla.place(x=300,y=400)
lblb=tk.Label(window,text='b= ')
lblb.place(x=430,y=400)
valz=tk.Scale(window,from_=0.5,to_=1.5,resolution=0.1,length=215,orient=tk.HORIZONTAL)
valz.set(1.0)
valz.place(x=330,y=430)
minr=tk.Entry(window,width=10)
minr.insert(0,0)
minr.place(x=330,y=550)
maxr=tk.Entry(window,width=10)
maxr.insert(0,255)
maxr.place(x=460,y=550)
optionList2 = ['original','black']   
mod2 = tk.StringVar()                                        
mod2.set('original')
menu2 = tk.OptionMenu(window, mod2, *optionList2)                
menu2.place(x=150,y=545)
confirm=tk.Button(window,text='confirm',width=5,height=2,command=gray)
confirm.place(x=630,y=500)
rot=tk.Scale(window,from_=0.0,to_=360.0 ,length=215,orient=tk.HORIZONTAL)
rot.place(x=330,y=480)
one=tk.Label(window,text='contrast/brightness')
one.place(x=10,y=400)
two=tk.Label(window,text='zoom')
two.place(x=10,y=450)
three=tk.Label(window,text='rotate')
three.place(x=10,y=500)
four=tk.Label(window,text='gray level')
four.place(x=10,y=550)

window.mainloop()
