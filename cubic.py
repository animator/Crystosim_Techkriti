from visual import *
#f=frame()
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


def main(l,w,h,a,p):
   r=a/2.0
   
   list=[[0,0,0]]    
   for x in range(0,l+1):
    for y in range(0,w+1):
        for z in range(0,h+1):
          sc(x*a,y*a,z*a,l*a,w*a,h*a,a)
          s=sphere(pos=(x*a,y*a,z*a),radius=r*p,color=color.red)
       
          
   return

   

#main(2,2,2,2,0.5)
