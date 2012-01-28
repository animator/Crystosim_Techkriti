from visual import *
def drawline(list1,list2):
    line=paths.line(start=list1,end=list2,np=2)
    curve(pos=line.pos)
def polygon(list1,list2,list3,list4):
    drawline(list1,list2)
    drawline(list2,list3)
    drawline(list3,list4)
    drawline(list4,list1)
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
def main(c,b,a,l,w,h,h1,k,l1):
    x0=0
    y0=0
    z0=0
    l=pi*l/180
    w=w*pi/180
    h=h*pi/180
    list=[[]]
    q=(cos(h)*(1/sin(l))-cos(w)*(cos(l)/sin(l)))
    list[0]=[x0,y0,z0]
    list.append([x0+a*cos(w),y0+a*q,z0+a*sqrt((sin(w)*sin(w))+q*q)])
    list.append([x0+b*cos(l),y0+b*sin(l),z0])
    list.append([x0+c,y0,z0])
    list.append([list[1][0]+list[2][0],list[1][1]+list[2][1],list[1][2]+list[2][2]])
    list.append([list[1][0]+list[3][0],list[1][1]+list[3][1],list[1][2]+list[3][2]])
    list.append([list[2][0]+list[3][0],list[2][1]+list[3][1],list[2][2]+list[3][2]])
    list.append([list[1][0]+list[2][0]+list[3][0],list[1][1]+list[2][1]+list[3][1],list[1][2]+list[2][2]+list[3][2]])
    print list[5]
    polygon(list[0],list[1],list[5],list[3])
    polygon(list[0],list[1],list[4],list[2])
    polygon(list[0],list[2],list[6],list[3])
    polygon(list[1],list[4],list[7],list[5])
    polygon(list[3],list[5],list[7],list[6])
    polygon(list[2],list[4],list[7],list[6])

    line1=paths.line(start=(0,0,0),end=(2*c,0,0),np=2)
    curve(pos=line1.pos,color=color.blue)

    line1=paths.line(start=(0,0,0),end=(0,2*b,0),np=2)
    curve(pos=line1.pos,color=color.red)
    line1=paths.line(start=(0,0,0),end=(0,0,2*a),np=2)
    curve(pos=line1.pos,color=color.cyan)
    
    if (h1==0 and k==0):
       faces(pos=[(0,0,0),(0,0,c),(c,0,a)],color=color.red)
       faces(pos=[(c,0,a),(0,0,a),(0,0,0)],color=color.red)
       faces(pos=[(0,0,0),(c,0,0),(c,0,a)],color=color.red)
       faces(pos=[(c,0,a),(c,0,0),(0,0,0)],color=color.red)
       return
  
    if (k==0 and l1==0):
       faces(pos=[(0,0,0),(0,b,0),(c,b,0)],color=color.red)
       faces(pos=[(c,b,0),(0,b,0),(0,0,0)],color=color.red)
       faces(pos=[(0,0,0),(c,0,0),(c,b,0)],color=color.red)
       faces(pos=[(c,b,0),(c,0,0),(0,0,0)],color=color.red)
       return
    if (h1==0 and l1==0):
       faces(pos=[(0,0,0),(0,0,a),(0,b,a)],color=color.red)
       faces(pos=[(0,b,a),(0,0,a),(0,0,0)],color=color.red)
       faces(pos=[(0,0,0),(0,b,0),(0,b,a)],color=color.red)
       faces(pos=[(0,b,a),(0,b,0),(0,0,0)],color=color.red)
       return
    
    if (h1==0):
       m=hcf(k,l1)
       k=k/m
       l1=l1/m
       
       k=b*1.0/k
       l1=a*1.0/l1
       faces(pos=[(0,0,0),(0,k,0),(a,k,l1)],color=color.red)
       faces(pos=[(0,0,0),(a,0,l1),(a,k,l1)],color=color.red)
       faces(pos=[(a,k,l1),(0,k,0),(0,0,0)],color=color.red)
       faces(pos=[(a,k,l1),(a,0,l1),(0,0,0)],color=color.red)
       
       return
    if (k==0):
       m=hcf(h1,l1)
       h1=h1/m
       l1=l1/m
       h1=1.0*c/h1
       l1=a*1.0/l1
       faces(pos=[(0,b,0),(0,b,l1),(h1,0,l1)],color=color.red)
       faces(pos=[(h1,0,l1),(0,b,l1),(0,b,0)],color=color.red)
       faces(pos=[(h1,0,l1),(0,b,0),(h1,0,0)],color=color.red)
       faces(pos=[(h1,0,0),(0,b,0),(h1,0,l1)],color=color.red)
       return
    if (l1==0):
       m=hcf(h1,k)
       h1=h1/m
       k=k/m
       h1=1.0*c/h1
       k=b*1.0/k
       faces(pos=[(0,k,0),(h1,k,0),(0,0,c)],color=color.red)
       faces(pos=[(0,0,c),(h1,k,0),(0,k,0)],color=color.red)
       faces(pos=[(h1,k,0),(0,0,c),(h1,0,c)],color=color.red)
       faces(pos=[(h1,0,c),(0,0,c),(h1,k,0)],color=color.red)
       return
       
    m1=hcf(h1,k)
    m2=hcf(k,l1)
    m3=hcf(l1,h1)
    m=min(m1,m2,m3)
    print m
    h1=h1/m
    k=k/m
    l1=l1/m
    h1=(c*1.0)/h1
    k=b*1.0/k
    l1=a*1.0/l1
    faces(pos=[(h1,0,0),(h1,k,0),(0,0,l1)],color=color.red)
    faces(pos=[(0,0,l1),(0,k,0),(h1,0,0)],color=color.red)      
    return



#main(1,1,1,90,90,90,2,4,4)
