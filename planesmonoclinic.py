from visual import *
def drawline(list1,list2):
    line=paths.line(start=list1,end=list2,np=2)
    curve(pos=line.pos)
def polygon(list1,list2,list3,list4):
    drawline(list1,list2)
    drawline(list2,list3)
    drawline(list3,list4)
    drawline(list4,list1)
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
def main(a,b,c,alpha,beta,gamma,h1,k,l1):
    list1=[[]]
    list1[0]=[0,0,0]
    
    list1.append([a,0,0])
    alpha=alpha*pi/180
    beta=beta*pi/180
    gamma=gamma*pi/180
    x1=b*cos(beta)
    y1=b*sin(beta)
    #z1=math.sqrt((b*b-x1*x1-y1*y1)
    z1=0
    list1.append([x1,y1,z1])
    

    x2=c*cos(gamma)
    y2=(b*c*cos(alpha)-x1*x2)/y1
    a1=(c*c)-(x2*x2)-(y2*y2)
    z2=math.sqrt(a1)
    list1.append([x2,y2,z2])
    
    x3=x1+a
    y3=y1
    z3=z1

    list1.append([x3,y3,z3])
    x4=a+x2
    y4=y2
    z4=z2
    list1.append([x4,y4,z4])

    x5=x1+x2
    y5=y1+y2
    z5=z1+z2
    list1.append([x5,y5,z5])

    x6=x1+x2+a
    y6=y1+y2
    z6=z1+z2
    list1.append([x6,y6,z6])
    
    polygon(list1[0],list1[1],list1[5],list1[3])
    polygon(list1[1],list1[5],list1[7],list1[4])
    polygon(list1[2],list1[4],list1[7],list1[6])
    polygon(list1[0],list1[3],list1[6],list1[2])
    polygon(list1[0],list1[1],list1[4],list1[2])
    polygon(list1[3],list1[5],list1[7],list1[6])
    line1=paths.line(start=list1[0],end=list1[1],np=2)
    curve(pos=line1.pos,color=color.blue)

    line1=paths.line(start=list1[0],end=list1[2],np=2)
    curve(pos=line1.pos,color=color.red)
    line1=paths.line(start=list1[0],end=list1[3],np=2)
    curve(pos=line1.pos,color=color.cyan)
    
    if (h1==0 and k==0):
       convex(pos=([list1[0],list1[1],list1[5],list1[3]]),color=color.red)
       drawborder1(list1[0],list1[1],list1[5],list1[3])
       return
  
    if (k==0 and l1==0):
       convex(pos=([list1[0],list1[1],list1[4],list1[2]]),color=color.red)
       drawborder1(list1[0],list1[1],list1[4],list1[2])
       return
    if (h1==0 and l1==0):
       convex(pos=([list1[0],list1[2],list1[6],list1[3]]),color=color.red)
       drawborder1(list1[0],list1[2],list1[6],list1[3])
       return
    
    if (h1==0):
       m=hcf(abs(k),abs(l1))
       k=k*1.0/m
       l1=l1*1.0/m
       
       
       k=1.0/k
       l1=1.0/l1
       
       n1=1-k
       x2=(k*list1[4][0]+n1*list1[1][0])
       y2=(k*list1[4][1]+n1*list1[1][1])
       z2=(k*list1[4][2]+n1*list1[1][2])
       x1=(k*list1[7][0]+n1*list1[5][0])
       y1=(k*list1[7][1]+n1*list1[5][1])
       z1=(k*list1[7][2]+n1*list1[5][2])
       
       n2=1-l1
       #l1=1-n2
       x3=(l1*list1[1][0]+n2*list1[0][0])
       y3=(l1*list1[1][1]+n2*list1[0][1])
       z3=(l1*list1[1][2]+n2*list1[0][2])
       x4=(l1*list1[5][0]+n2*list1[3][0])
       y4=(l1*list1[5][1]+n2*list1[3][1])
       z4=(l1*list1[5][2]+n2*list1[3][2])
       convex(pos=([x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4]),color=color.red)
       drawborder1([x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4])
       
       
       return
    if (k==0):
       m=hcf(abs(h1),abs(l1))
       h1=h1*1.0/m
       l1=l1*1.0/m
       h1=1.0/h1
       l1=1.0/l1
       n=1-h1
       x1=(h1*list1[2][0]+n*list1[0][0])
       y1=(h1*list1[2][1]+n*list1[0][1])
       z1=(h1*list1[2][2]+n*list1[0][2])
       x2=(h1*list1[4][0]+n*list1[1][0])
       y2=(h1*list1[4][1]+n*list1[1][1])
       z2=(h1*list1[4][2]+n*list1[1][2])
       n2=1-l1
       x3=(l1*list1[3][0]+n2*list1[0][0])
       y3=(l1*list1[3][1]+n2*list1[0][1])
       z3=(l1*list1[3][2]+n2*list1[0][2])
       x4=(l1*list1[5][0]+n2*list1[1][0])
       y4=(l1*list1[5][1]+n2*list1[1][1])
       z4=(l1*list1[5][2]+n2*list1[1][2])
       convex(pos=([x1,y1,z1],[x2,y2,z2],[x3,y3,z3],[x4,y4,z4]),color=color.red)
       drawborder1([x1,y1,z1],[x2,y2,z2],[x4,y4,z4],[x3,y3,z3])
       return
    if (l1==0):
       m=hcf(abs(h1),abs(k))
       h1=h1*1.0/m
       k=k*1.0/m
       
       h1=(1.0)/h1
       k=1.0/k
       
       n=1-h1
       x1=(h1*list1[5][0]+n*list1[1][0])
       y1=(h1*list1[5][1]+n*list1[1][1])
       z1=(h1*list1[5][2]+n*list1[1][2])
       x3=(h1*list1[7][0]+n*list1[4][0])
       y3=(h1*list1[7][1]+n*list1[4][1])
       z3=(h1*list1[7][2]+n*list1[4][2])
       n1=k
       k=1-n1
       x2=(k*list1[2][0]+n1*list1[4][0])
       y2=(k*list1[2][1]+n1*list1[4][1])
       z2=(k*list1[2][2]+n1*list1[4][2])
       x4=(k*list1[0][0]+n1*list1[1][0])
       y4=(k*list1[0][1]+n1*list1[1][1])
       z4=(k*list1[0][2]+n1*list1[1][2])
       convex(pos=([(x1,y1,z1),(x2,y2,z2),(x3,y3,z3),(x4,y4,z4)]),color=color.red)
       drawborder1([x1,y1,z1],[x3,y3,z3],[x2,y2,z2],[x4,y4,z4])
       
       return
       
    m1=hcf(abs(h1),abs(k))
    m2=hcf(abs(k),abs(l1))
    m3=hcf(abs(l1),abs(h1))
    m=min(m1,m2,m3)
    
    h1=h1*1.0/m
    k=k*1.0/m
    l1=l1*1.0/m
    h1=(1.0)/h1
    k=1.0/k
    l1=1.0/l1
    n=1-h1
    x1=(h1*list1[2][0]+n*list1[0][0])
    y1=(h1*list1[2][1]+n*list1[0][1])
    z1=(h1*list1[2][2]+n*list1[0][2])
    n1=1-k
    x2=(k*list1[1][0]+n1*list1[0][0])
    y2=(k*list1[1][1]+n1*list1[0][1])
    z2=(k*list1[1][2]+n1*list1[0][2])
    n2=1-l1
    x3=(l1*list1[3][0]+n2*list1[0][0])
    y3=(l1*list1[3][1]+n2*list1[0][1])
    z3=(l1*list1[3][2]+n2*list1[0][2])
    convex(pos=[(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)],color=color.red)
    drawborder([x1,y1,z1],[x2,y2,z2],[x3,y3,z3])
     #   faces(pos=[(0,0,l1),(0,k,0),(h1,0,0)],color=color.red)      
    return



#main(1,1,1,90,90,60,2,3,0)
