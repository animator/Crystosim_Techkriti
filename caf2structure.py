from visual import *
import math

def drawline(list1,list2):
    l=paths.line(start=list1,end=list2,np=2)
    curve(pos=l.pos)
    return
def sc(x,y,z,l,b,h,a):
    if x==l and y==b and z==h:
        return
    if x<l and y<b and z<h:
        drawline([x,y,z],[x+a,y,z])
        drawline([x,y,z],[x,y+a,z])
        drawline([x,y,z],[x,y,z+a])

    if x==l and y==b :
        drawline([x,y,z],[x,y,z+a])
        return
    if x==l and z==h:
        drawline([x,y,z],[x,y+a,z])
        return
    if y==b and z==h:
        drawline([x,y,z],[x+a,y,z])
        return
    if x==l:
        drawline([x,y,z],[x,y+a,z])
        
        drawline([x,y,z],[x,y,z+a])
    if y==b:
        drawline([x,y,z],[x+a,y,z])
    
        drawline([x,y,z],[x,y,z+a])
    
    if z==h:
        drawline([x,y,z],[x+a,y,z])
    
        drawline([x,y,z],[x,y+a,z])
    
    return
def trans(list1,list2,p,r):
    m1=(list1[0]-list2[0])
    m1=m1*m1
    m2=(list1[1]-list2[1])
    m2=m2*m2
    m3=(list1[2]-list2[2])
    m3=m3*m3
    x1=math.sqrt(m1)
    y1=math.sqrt(m2)
    z1=math.sqrt(m3)
    s=sphere(pos=(x1,y1,z1),radius=p*r,color=color.blue)
    return


def main(l,w,h,a,p):
   a=a*2
   r=(math.sqrt(2))*a/4.0
   

      
   for x in range(0,l+1):
    for y in range(0,w+1):
        for z in range(0,h+1):
          sc(x*a,y*a,z*a,l*a,w*a,h*a,a)
          s=sphere(pos=(x*a,y*a,z*a),radius=r*p,color=color.red)
          trans([x*a,y*a,z*a],[a*0.25,a*0.25,a*0.25],p,r)


   x,y,z=a/2.0,a/2.0,0
   for j in range(0,w):
      for i in range(0,l):
          for k in range(0,h+1):
              s=sphere(pos=(x+i*a,y+j*a,z+k*a),radius=r*p,color=color.red)
              trans([x+i*a,y+j*a,z+k*a],[a*0.25,a*0.25,a*0.25],p,r)
              
          
      
   x,y,z=a/2.0,0,a/2.0
   for i in range(0,l):
      for j in range(0,w+1):
          for k in range(0,h):
              s=sphere(pos=(x+i*a,y+j*a,z+k*a),radius=r*p,color=color.red)
              trans([x+i*a,y+j*a,z+k*a],[a*0.25,a*0.25,a*0.25],p,r)

   x,y,z=0,a/2.0,a/2.0
   for k in range(0,h):
      for i in range(0,l+1):
          for j in range(0,w):
              s=sphere(pos=(x+i*a,y+j*a,z+k*a),radius=r*p,color=color.red)
              trans([x+i*a,y+j*a,z+k*a],[a*0.25,a*0.25,a*0.25],p,r)

   return

   
#main(1,1,1,1.5,0.2)
