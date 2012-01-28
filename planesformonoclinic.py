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

    line1=paths.line(start=list[0],end=list[1],np=2)
    curve(pos=line1.pos,color=color.blue)

    line1=paths.line(start=list[0],end=list[2],np=2)
    curve(pos=line1.pos,color=color.red)
    line1=paths.line(start=list[0],end=list[3],np=2)
    curve(pos=line1.pos,color=color.cyan)
    
    if (h1==0 and k==0):
       convex(pos=([list[0],list[1],list[5],list[3]]),color=color.red)
       return
  
    if (k==0 and l1==0):
       convex(pos=([list[0],list[1],list[4],list[2]]),color=color.red)
       return
    if (h1==0 and l1==0):
       convex(pos=([list[0],list[2],list[6],list[3]]),color=color.red)
       return
    
    if (h1==0):
       m=hcf(abs(k),abs(l1))
       k=k/m
       l1=l1/m
       
       k=k/m
       l1=l1/m
       k=1.0/k
       l1=1.0/l1
       
       n1=1-k
       x2=(k*list[4][0]+n1*list[1][0])
       y2=(k*list[4][1]+n1*list[1][1])
       z2=(k*list[4][2]+n1*list[1][2])
       x1=(k*list[7][0]+n1*list[5][0])
       y1=(k*list[7][1]+n1*list[5][1])
       z1=(k*list[7][2]+n1*list[5][2])
       
       n2=l1
       l1=1-n2
       x3=(l1*list[1][0]+n2*list[0][0])
       y3=(l1*list[1][1]+n2*list[0][1])
       z3=(l1*list[1][2]+n2*list[0][2])
       x4=(l1*list[5][0]+n2*list[3][0])
       y4=(l1*list[5][1]+n2*list[3][1])
       z4=(l1*list[5][2]+n2*list[3][2])
       convex(pos=([x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4]),color=color.red)
       
       
       
       return
    if (k==0):
       m=hcf(abs(h1),abs(l1))
       h1=h1/m
       l1=l1/m
       h1=1.0/h1
       l1=1.0/l1
       n=1-h
       x1=(h*list[2][0]+n*list[0][0])
       y1=(h*list[2][1]+n*list[0][1])
       z1=(h*list[2][2]+n*list[0][2])
       x2=(h*list[4][0]+n*list[1][0])
       y2=(h*list[4][1]+n*list[1][1])
       z2=(h*list[4][2]+n*list[1][2])
       n2=1-l1
       x3=(l1*list[3][0]+n2*list[0][0])
       y3=(l1*list[3][1]+n2*list[0][1])
       z3=(l1*list[3][2]+n2*list[0][2])
       x4=(l1*list[5][0]+n2*list[1][0])
       y4=(l1*list[5][1]+n2*list[1][1])
       z4=(l1*list[5][2]+n2*list[1][2])
       convex(pos=([x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4]),color=color.red)
       return
    if (l1==0):
       m=hcf(abs(h1),abs(k))
       h1=h1/m
       k=k/m
       
       h1=(1.0)/h1
       k=1.0/k
       
       n=1-h1
       x1=(h*list[5][0]+n*list[1][0])
       y1=(h*list[5][1]+n*list[1][1])
       z1=(h*list[5][2]+n*list[1][2])
       x3=(h*list[7][0]+n*list[4][0])
       y3=(h*list[7][1]+n*list[4][1])
       z3=(h*list[7][2]+n*list[4][2])
       n1=1-k
       x2=(k*list[2][0]+n1*list[4][0])
       y2=(k*list[2][1]+n1*list[4][1])
       z2=(k*list[2][2]+n1*list[4][2])
       x4=(k*list[0][0]+n1*list[1][0])
       y4=(k*list[0][1]+n1*list[1][1])
       z4=(k*list[0][2]+n1*list[1][2])
       convex(pos=([(x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4)]),color=color.red)                            
       
       return
       
    m1=hcf(abs(h1),abs(k))
    m2=hcf(abs(k),abs(l1))
    m3=hcf(abs(l1),abs(h1))
    m=min(m1,m2,m3)
    print m
    h1=h1/m
    k=k/m
    l1=l1/m
    h1=(1.0)/h1
    k=1.0/k
    l1=1.0/l1
    n=1-h1
    x1=(h*list[2][0]+n*list[0][0])
    y1=(h*list[2][1]+n*list[0][1])
    z1=(h*list[2][2]+n*list[0][2])
    n1=1-k
    x2=(k*list[1][0]+n1*list[0][0])
    y2=(k*list[1][1]+n1*list[0][1])
    z2=(k*list[1][2]+n1*list[0][2])
    n2=1-l1
    x3=(l1*list[3][0]+n2*list[0][0])
    y3=(l1*list[3][1]+n2*list[0][1])
    z3=(l1*list[3][2]+n2*list[0][2])
    convex(pos=[(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)],color=color.red)
     #   faces(pos=[(0,0,l1),(0,k,0),(h1,0,0)],color=color.red)      
    return



#main(1,1,1,90,90,60,1,1,1)
