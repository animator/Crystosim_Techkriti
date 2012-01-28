from visual import *
#f=frame()
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


def main(l,w,h,a,b,c,p):
   a=a*2
   b=b*2
   c=c*2
   r=min(a,b,c)/2.0
   
     
   for x in range(0,l+1):
    for y in range(0,w+1):
        for z in range(0,h+1):
          sc(x*a,y*b,z*c,l*a,w*b,h*c,a,b,c)
          s=sphere(pos=(x*a,y*b,z*c),radius=p*r,color=color.red)
          
   return

   


