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
    #print list1
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
    m=max(abs(h1),abs(k),abs(l1))
    h1=(h1*1.0)/m
    x1=(h1*list1[1][0]+(1-h1)*list1[0][0])
    y1=(h1*list1[1][1]+(1-h1)*list1[0][1])
    z1=(h1*list1[1][2]+(1-h1)*list1[0][2])
    
    k=(k*1.0)/m
    x2=(k*list1[2][0]+(1-k)*list1[0][0])
    y2=(k*list1[2][1]+(1-k)*list1[0][1])
    z2=(k*list1[2][2]+(1-k)*list1[0][2])
    l1=(l1*1.0)/m
    x3=(l1*list1[3][0]+(1-l1)*list1[0][0])
    y3=(l1*list1[3][1]+(1-l1)*list1[0][1])
    z3=(l1*list1[3][2]+(1-l1)*list1[0][2])
    
    a1=arrow(pos=(0,0,0),axis=(x1+x2+x3,y1+y2+y3,z1+z2+z3),color=color.red) 


#main(1,1,1,90,90,90,2,2,1)
