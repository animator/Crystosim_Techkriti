from visual import *
f=frame()
def drawline(list1,list2):
    
    line=paths.line(start=list1,end=list2,np=2)
    curve(frame=f,pos=line.pos)
def polygon(list1,list2,list3,list4):
    drawline(list1,list2)
    drawline(list2,list3)
    drawline(list3,list4)
    drawline(list4,list1)

def main(a,b,c,l,w,h,h1,k,l1):
    x0=0
    y0=0
    z0=0
     
    l=pi*l/180
    w=pi*w/180
    h=pi*h/180
    list=[[]]
    q=(cos(h)*(1/sin(l))-cos(w)*(cos(l)/sin(l)))
    list[0]=[x0,y0,z0]
    list.append([x0+a*cos(w),y0+a*q,z0+a*sqrt((sin(w)*sin(w))+q*q)])
    list.append([x0+b*cos(l),y0+b*sin(l),z0])
    list.append([x0+c,y0,z0])
    list.append([list[1][0]+list[2][0],list[1][1]+list[2][1],list[1][2]+list[2][2]])
    list.append([x0+c+a*cos(w),y0+a*q,z0+a*sqrt((sin(w)*sin(w))+q*q)])
    list.append([x0+b*cos(l)+c,y0+b*sin(l),z0])
    list.append([x0+c+a*cos(w),y0+a*q+b,z0+a*sqrt((sin(w)*sin(w))+q*q)])
   # print list[5]
    polygon(list[0],list[1],list[5],list[3])
    polygon(list[0],list[1],list[4],list[2])
    polygon(list[0],list[2],list[6],list[3])
    polygon(list[1],list[4],list[7],list[5])
    polygon(list[3],list[5],list[7],list[6])
    polygon(list[2],list[4],list[7],list[6])
    line=paths.line(start=(0,0,0),end=(2*a,0,0),np=2)
    curve(frame=f,pos=line.pos,color=color.red)
    line=paths.line(start=(0,0,0),end=(0,2*b,0),np=2)
    curve(frame=f,pos=line.pos,color=color.blue)
    line=paths.line(start=(0,0,0),end=(0,0,2*c),np=2)
    curve(frame=f,pos=line.pos,color=color.cyan)
    #for w in range(0,len(list)):
       # s=sphere(pos=(list[w][0],list[w][1],list[w][2]),radius=r*p)
    m=max(abs(h1),abs(k),abs(l1))
    h1=(h1*a)/m
    k=(k*b)/m
    l1=(l1*c)/m
    
    a1=arrow(pos=(0,0,0),axis=(h1,k,l1))   
main(2,3,2,90,90,90,1,2,1)
