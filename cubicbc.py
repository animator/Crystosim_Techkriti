from visual import *

def drawline(list1,list2):
    l=paths.line(start=list1,end=list2,np=2)
    curve(pos=l.pos)
    return
def sc(x,y,z,l,b,h,a,w,c):
    if x==l and y==b and z==h:
        return
    if x<l and y<b and z<h:
        drawline([x,y,z],[x+a,y,z])
        drawline([x,y,z],[x,y+w,z])
        drawline([x,y,z],[x,y,z+c])

    if x==l and y==b :
        drawline([x,y,z],[x,y,z+c])
        return
    if x==l and z==h:
        drawline([x,y,z],[x,y+w,z])
        return
    if y==b and z==h:
        drawline([x,y,z],[x+a,y,z])
        return
    if x==l:
        drawline([x,y,z],[x,y+w,z])
        
        drawline([x,y,z],[x,y,z+c])
    if y==b:
        drawline([x,y,z],[x+a,y,z])
    
        drawline([x,y,z],[x,y,z+c])
    
    if z==h:
        drawline([x,y,z],[x+a,y,z])
    
        drawline([x,y,z],[x,y+w,z])
    
    return


def main(l,w,h,a,p):
   
   a=a*2
   r=sqrt(3)*a/4.0
   b=a
   c=a
   
  
       
   for x in range(0,l+1):
    for y in range(0,w+1):
        for z in range(0,h+1):
          sc(x*a,y*a,z*a,l*a,w*a,h*a,a,b,c)
          s=sphere(pos=(x*a,y*a,z*a),radius=p*r,color=color.red)

   x=a/2.0
   y=b/2.0
   z=c/2.0
   for i in range(0,l):
       
       for j in range(0,w):
           for k in range(0,h):
               s=sphere(pos=(i*a+x,j*a+y,k*a+z),radius=r*p,color=color.red)
              
  
       

   return

   
#main(2,2,2,1.5,0.2)

