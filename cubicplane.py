from visual import *
def drawborder(list1,list2,list3):
    l=paths.line(start=list1,end=list2)
    curve(pos=l.pos,color=color.yellow)
    l1=paths.line(start=list2,end=list3)
    curve(pos=l1.pos,color=color.yellow)
    l2=paths.line(start=list3,end=list1)
    curve(pos=l2.pos,color=color.yellow)
def drawborder1(list1,list2,list3,list4):
    l=paths.line(start=list1,end=list2)
    curve(pos=l.pos,color=color.yellow)
    l1=paths.line(start=list2,end=list3)
    curve(pos=l1.pos,color=color.yellow)
    l2=paths.line(start=list3,end=list4)
    curve(pos=l2.pos,color=color.yellow)
    l3=paths.line(start=list4,end=list1)
    curve(pos=l3.pos,color=color.yellow)
def drawline(list1,list2):
    l=paths.line(start=list1,end=list2,np=2)
    curve(pos=l.pos)
    return
def sc(x,y,z,l,w,h,a,b,c):
    if x==l and y==w and z==h:
        return
    if x<l and y<w and z<h:
        drawline([x,y,z],[x+a,y,z])
        drawline([x,y,z],[x,y+b,z])
        drawline([x,y,z],[x,y,z+c])

    if x==l and y==w :
        drawline([x,y,z],[x,y,z+c])
        return
    if x==l and z==h:
        drawline([x,y,z],[x,y+b,z])
        return
    if y==w and z==h:
        drawline([x,y,z],[x+a,y,z])
        return
    if x==l:
        drawline([x,y,z],[x,y+b,z])
        drawline([x,y,z],[x,y,z+c])
        
    if y==w:
        drawline([x,y,z],[x+a,y,z])
        drawline([x,y,z],[x,y,z+c])
        
    if z==h:
        drawline([x,y,z],[x+a,y,z])
        drawline([x,y,z],[x,y+b,z])
    
    return
def hcf(a,b):
    if(a<b):
        x=a
        a=b
        b=x
    if(a%b ==0):
        return b
        
    while(a>b and a%b!=0):
        r=a%b
        b=a
        a=r
    return r   

def main(a,b,c,h,k,l1):
   
   
   list=[[0,0,0]]    
   for x in range(0,2*a,a):
    for y in range(0,2*b,b):
        for z in range(0,2*c,c):
          sc(x,y,z,a,b,c,a,b,c)
         # s=sphere(pos=(x,y,z),radius=p*r)
   line1=paths.line(start=(0,0,0),end=(2*a,0,0),np=2)
   curve(pos=line1.pos,color=color.blue)

   line1=paths.line(start=(0,0,0),end=(0,2*b,0),np=2)
   curve(pos=line1.pos,color=color.red)
   line1=paths.line(start=(0,0,0),end=(0,0,2*c),np=2)
   curve(pos=line1.pos,color=color.cyan)
   
   if (h==0 and k==0):
       faces(pos=[(0,0,0),(0,0,c),(a,0,c)],color=color.cyan)
       faces(pos=[(a,0,c),(0,0,c),(0,0,0)],color=color.cyan)
       faces(pos=[(0,0,0),(a,0,0),(a,0,c)],color=color.cyan)
       faces(pos=[(a,0,c),(a,0,0),(0,0,0)],color=color.cyan)
       drawborder1([0,0,0],[0,0,c],[a,0,c],[a,0,0])
       return
  
   if (k==0 and l1==0):
       faces(pos=[(0,0,0),(0,b,0),(a,b,0)],color=color.cyan)
       faces(pos=[(a,b,0),(0,b,0),(0,0,0)],color=color.cyan)
       faces(pos=[(0,0,0),(a,0,0),(a,b,0)],color=color.cyan)
       
       faces(pos=[(a,b,0),(a,0,0),(0,0,0)],color=color.cyan)
       drawborder1([0,0,0],[a,0,0],[a,b,0],[0,b,0])
       return
   if (h==0 and l1==0):
       faces(pos=[(0,0,0),(0,0,c),(0,b,c)],color=color.cyan)
       faces(pos=[(0,b,c),(0,0,c),(0,0,0)],color=color.cyan)
       faces(pos=[(0,0,0),(0,b,0),(0,b,c)],color=color.cyan)
       faces(pos=[(0,b,c),(0,b,0),(0,0,0)],color=color.cyan)
       drawborder1([0,0,0],[0,b,0],[0,b,c],[0,0,c])
       return
    
       
   
   if (h==0):
       m=hcf(abs(k),abs(l1))
       k=k*1.0/m
       l1=l1*1.0/m
       
       #k=k*1.0/m
       #l1=l1*1.0/m
       
       k=b*1.0/k
       l1=c*1.0/l1
       faces(pos=[(0,k,0),(a,k,0),(a,0,l1)],color=color.cyan)
       faces(pos=[(a,0,l1),(a,k,0),(0,k,0)],color=color.cyan)
       faces(pos=[(0,k,0),(0,0,l1),(a,0,l1)],color=color.cyan)
       faces(pos=[(a,0,l1),(0,0,l1),(0,k,0)],color=color.cyan)
       drawborder1([0,0,l1],[0,k,0],[a,k,0],[a,0,l1])
       
       return
   if (k==0):
       m=hcf(abs(h),abs(l1))
       h=h*1.0/m
       l1=l1*1.0/m
      # h=1.0/h
      # l1=1.0/l1
       h=a*1.0/h
       l1=c*1.0/l1
       faces(pos=[(h,0,0),(h,b,0),(0,b,l1)],color=color.cyan)
       faces(pos=[(0,b,l1),(h,b,0),(h,0,0)],color=color.cyan)
       faces(pos=[(h,0,0),(0,0,l1),(0,b,l1)],color=color.cyan)
       faces(pos=[(0,b,l1),(0,0,l1),(h,0,0)],color=color.cyan)
       drawborder1([h,0,0],[0,0,l1],[0,b,l1],[h,b,0])
       #drawborder([h,0,0],[0,b,0],[h,0,l1])
       return
   if (l1==0):
       m=hcf(abs(h),abs(k))
       h=h*1.0/m
       k=k*1.0/m
       
       
       h=a*1.0/h
       k=b*1.0/k
       faces(pos=[(h,0,0),(0,k,0),(0,k,c)],color=color.cyan)
       faces(pos=[(0,k,c),(0,k,0),(h,0,0)],color=color.cyan)
       faces(pos=[(0,k,c),(h,0,c),(h,0,0)],color=color.cyan)
       faces(pos=[(h,0,0),(h,0,c),(0,k,c)],color=color.cyan)
       drawborder1([h,0,0],[0,k,0],[0,k,c],[h,0,c])
       #drawborder([h,0,c],[0,0,c],[h,k,0])
       return
   
   
   
   #print m
   m1=hcf(abs(h),abs(k))
   m2=hcf(abs(k),abs(l1))
   m=hcf(abs(m1),abs(m2))
   # m=min(m1,m2,m3)
    
   h=h*1.0/m
   k=k*1.0/m
   l1=l1*1.0/m
   
   h=a*1.0/h
   k=b*1.0/k
   l1=c*1.0/l1
   faces(pos=[(h,0,0),(0,k,0),(0,0,l1)],color=color.cyan)
   faces(pos=[(0,0,l1),(0,k,0),(h,0,0)],color=color.cyan)
   drawborder([h,0,0],[0,k,0],[0,0,l1])
   return



#main(1,1,1,2,3,0)


    

