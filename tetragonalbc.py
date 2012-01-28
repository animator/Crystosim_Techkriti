from visual import *
import math
#f=frame()
def drawline(list1,list2):
    l=paths.line(start=list1,end=list2,np=2)
    curve(pos=l.pos)
    return
def sc(x,y,z,l,b,h,a,c):
    if x==l and y==b and z==h:
        return
    if x<l and y<b and z<h:
        drawline([x,y,z],[x+a,y,z])
        drawline([x,y,z],[x,y+a,z])
        drawline([x,y,z],[x,y,z+c])

    if x==l and y==b :
        drawline([x,y,z],[x,y,z+c])
        return
    if x==l and z==h:
        drawline([x,y,z],[x,y+a,z])
        return
    if y==b and z==h:
        drawline([x,y,z],[x+a,y,z])
        return
    if x==l:
        drawline([x,y,z],[x,y+a,z])
        
        drawline([x,y,z],[x,y,z+c])
    if y==b:
        drawline([x,y,z],[x+a,y,z])
    
        drawline([x,y,z],[x,y,z+c])
    
    if z==h:
        drawline([x,y,z],[x+a,y,z])
    
        drawline([x,y,z],[x,y+a,z])
    
    return


def main(l,w,h,a,c,p):
   a=a*2
   b=a
   r=(math.sqrt(3))*a/4.0
   if(a>c):
       r=c/2.0
   
   for x in range(0,l+1):
    for y in range(0,w+1):
        for z in range(0,h+1):
          sc(x*a,y*a,z*c,l*a,w*a,h*c,a,c)
          s=sphere(pos=(x*a,y*a,z*c),radius=p*r,color=color.red)
   x=a/2.0
   y=b/2.0
   z=c/2.0
   for i in range(0,l):
       
       for j in range(0,w):
           for k in range(0,h):
               s=sphere(pos=(i*a+x,j*a+y,k*c+z),radius=r*p,color=color.red)
       
          
   return

   
#main(2,3,4,2.5,3.5,0.2)
