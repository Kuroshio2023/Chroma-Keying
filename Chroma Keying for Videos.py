import os
import cv2
from PIL import Image
import time
import numpy
video1=cv2.VideoCapture("C:\\Users\\Akanksha Das\\Desktop\\Chroma Keying\\pratyush video.mp4")
for i in range(295):
    ret,data=video1.read()
    cv2.imwrite(r"C:\\Users\\Akanksha Das\\Desktop\\Chroma Keying\\Pratyush frames\\"+str(i)+".png",data)

g50={0:[0,0],20:[0,0],40:[0,0]}
g60={0:[0,50],20:[0,50],40:[0,40]}
g80={0:[0,70],20:[0,70],40:[0,65],60:[0,65]}
g100={0:[0,90],20:[0,90],40:[0,85],60:[0,85],80:[0,85]}
g120={0:[0,110],20:[0,105],40:[0,100],60:[0,100],80:[0,110],100:[0,100]}
g140={0:[0,130],20:[0,125],40:[0,125],60:[0,120],80:[0,120],100:[0,120],120:[0,115]}
g160={0:[0,140],20:[0,135],40:[0,135],60:[0,135],80:[0,135],100:[0,130],120:[0,130],140:[0,120]}
g180={0:[0,150],20:[0,150],40:[0,155],60:[0,155],80:[0,150],100:[0,155],120:[0,145],140:[0,145],160:[0,130]}
g200={0:[0,170],20:[0,165],40:[0,165],60:[0,165],80:[0,160],100:[0,155],120:[0,160],140:[0,160],160:[0,155],180:[0,0]}
g220={0:[0,170],20:[0,170],40:[0,170],60:[0,165],80:[0,165],100:[0,160],120:[0,165],140:[0,160],160:[0,160],180:[100,165],200:[0,0]}
g240={0:[0,170],20:[0,170],40:[0,180],60:[0,180],80:[0,175],100:[0,180],120:[0,185],140:[0,185],160:[0,190],180:[0,200],200:[165,205],220:[0,0]}
g255={0:[0,180],20:[0,185],40:[0,190],60:[0,185],80:[0,175],100:[0,185],120:[0,190],140:[0,190],160:[0,210],180:[0,200],200:[145,215],220:[180,210],240:[0,0]}
g_list={50:g50,60:g60,80:g80,100:g100,120:g120,140:g140,160:g160,180:g180,200:g200,220:g220,240:g240,260:g255}
def list_check(r,g,b,g_list):
    if ((g>r) & (g>b)):
        g1=round(g/20)*20
        r1=round(r/20)*20
        if g1<=50:
            return False
        else:
            if (g1>r1):
                if ((b >= g_list[g1][r1][0]) & (b<=g_list[g1][r1][1])):
                    return True
        return False        

            
def frame_check(frame,g_list):
    for i in range(len(frame)):
        for j in range(len(frame[0])):
            #r,g,b,v=frame.getpixel((i,j)) USE THIS IN CASE OF IMAGE 4
            r,g,b = frame[i,j]
            if list_check(r,g,b,g_list):
                frame[i,j]=[255,255,255]
        
    return frame   
    
for i in range(295):
    frame = cv2.imread("C:\\Users\\Akanksha Das\\Desktop\\Chroma Keying\\Pratyush frames\\"+str(i)+".png")
    frame1 = frame_check(frame,g_list)
    cv2.imwrite("C:\\Users\\Akanksha Das\\Desktop\\Chroma Keying\\Pratyush frames\\new"+str(i)+".png",frame1)
cv2_fourcc=cv2.VideoWriter_fourcc(*"mp4v")
video=cv2.VideoWriter("C:\\Users\\Akanksha Das\\Desktop\\Chroma Keying\\pratyush new one.mp4",cv2_fourcc,1,[1080,1920])
for i in range(295):
    video.write(cv2.imread("C:\\Users\\Akanksha Das\\Desktop\\Chroma Keying\\Pratyush frames\\new"+str(i)+".png"))
video.release()    

    
