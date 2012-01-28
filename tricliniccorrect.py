from visual import *
def drawline(list11,list12):
    
    line=paths.line(start=list11,end=list12,np=2)
    curve(pos=line.pos)
def polygon(list11,list12,list13,list14):
    drawline(list11,list12)
    drawline(list12,list13)
    drawline(list13,list14)
    drawline(list14,list11)

    
def main(a,b,c,alpha,beta,gamma,ma,mb,mc,p):
    
    r=(min(a,b,c))/2.0
    a=a*ma
    b=b*mb
    c=c*mc
    oma=ma
    omb=mb
    omc=mc
  
    
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
    for w in range(0,len(list1)):
        s=sphere(pos=(list1[w][0],list1[w][1],list1[w][2]),radius=r*p,color=color.red)

#start dividing the main cube
    m=1
    n=mc-1
    
    while (mc>1):
        i=0
        x=(m*list1[0][0]+n*list1[3][0])/(m+n)
        y=(m*list1[0][1]+n*list1[3][1])/(m+n)
        z=(m*list1[0][2]+n*list1[3][2])/(m+n)
        x1=(m*list1[1][0]+n*list1[5][0])/(m+n)
        y1=(m*list1[1][1]+n*list1[5][1])/(m+n)
        z1=(m*list1[1][2]+n*list1[5][2])/(m+n)
        x2=(m*list1[2][0]+n*list1[6][0])/(m+n)
        y2=(m*list1[2][1]+n*list1[6][1])/(m+n)
        z2=(m*list1[2][2]+n*list1[6][2])/(m+n)
        x3=(m*list1[4][0]+n*list1[7][0])/(m+n)
        y3=(m*list1[4][1]+n*list1[7][1])/(m+n)
        z3=(m*list1[4][2]+n*list1[7][2])/(m+n)
        s=sphere(pos=(x,y,z),radius=r*p,color=color.red)
        s=sphere(pos=(x1,y1,z1),radius=r*p,color=color.red)
        s=sphere(pos=(x2,y2,z2),radius=r*p,color=color.red)
        s=sphere(pos=(x3,y3,z3),radius=r*p,color=color.red)
        polygon([x,y,z],[x1,y1,z1],[x3,y3,z3],[x2,y2,z2])
        for i in range(1,mb):
            n=mb-i
            xx=(i*x+n*x2)/(i+n)
            yy=(i*y+n*y2)/(i+n)
            zz=(i*z+n*z2)/(i+n)
            xx1=(i*x1+n*x3)/(i+n)
            yy1=(i*y1+n*y3)/(i+n)
            zz1=(i*z1+n*z3)/(i+n)
            s=sphere(pos=(xx,yy,zz),radius=r*p,color=color.red)
            s=sphere(pos=(xx1,yy1,zz1),radius=r*p,color=color.red)
            
            ll=paths.line(start=(xx,yy,zz),end=(xx1,yy1,zz1),np=2)
            curve(pos=ll.pos)
            for j in range(1,ma):
                nn=ma-j
                xxa=(j*xx+nn*xx1)/(j+nn)
                yya=(j*yy+nn*yy1)/(j+nn)
                zza=(j*zz+nn*zz1)/(j+nn)
                s=sphere(pos=(xxa,yya,zza),radius=r*p,color=color.red)
                
            
            
        ma=oma
        for i in range(1,ma):
            n=ma-i
            xx=(i*x+n*x1)/(i+n)
            yy=(i*y+n*y1)/(i+n)
            zz=(i*z+n*z1)/(i+n)
            xx1=(i*x2+n*x3)/(i+n)
            yy1=(i*y2+n*y3)/(i+n)
            zz1=(i*z2+n*z3)/(i+n)
            ll=paths.line(start=(xx,yy,zz),end=(xx1,yy1,zz1),np=2)
            curve(pos=ll.pos)
            s=sphere(pos=(xx,yy,zz),radius=r*p,color=color.red)
            s=sphere(pos=(xx1,yy1,zz1),radius=r*p,color=color.red)
            for j in range(0,mb):
                nn=mb-j
                xxa=(j*xx+nn*xx1)/(j+nn)
                yya=(j*yy+nn*yy1)/(j+nn)
                zza=(j*zz+nn*zz1)/(j+nn)
                s=sphere(pos=(xxa,yya,zza),radius=r*p,color=color.red)
                
        m=m+1
        mc=mc-1
        n=mc-1
    m=1
    n=ma-1
    while (ma>=1):
        x=(m*list1[0][0]+n*list1[1][0])/(m+n)
        y=(m*list1[0][1]+n*list1[1][1])/(m+n)
        z=(m*list1[0][2]+n*list1[1][2])/(m+n)
        x1=(m*list1[3][0]+n*list1[5][0])/(m+n)
        y1=(m*list1[3][1]+n*list1[5][1])/(m+n)
        z1=(m*list1[3][2]+n*list1[5][2])/(m+n)
        x2=(m*list1[2][0]+n*list1[4][0])/(m+n)
        y2=(m*list1[2][1]+n*list1[4][1])/(m+n)
        z2=(m*list1[2][2]+n*list1[4][2])/(m+n)
        x3=(m*list1[6][0]+n*list1[7][0])/(m+n)
        y3=(m*list1[6][1]+n*list1[7][1])/(m+n)
        z3=(m*list1[6][2]+n*list1[7][2])/(m+n)
        polygon([x,y,z],[x1,y1,z1],[x3,y3,z3],[x2,y2,z2])
        #faces([x,y,z],[x1,y1,z1],[x3,y3,z3],[x2,y2,z2],mc,mb)
        s=sphere(pos=(x,y,z),radius=r*p,color=color.red)
        s=sphere(pos=(x1,y1,z1),radius=r*p,color=color.red)
        s=sphere(pos=(x2,y2,z2),radius=r*p,color=color.red)
        s=sphere(pos=(x3,y3,z3),radius=r*p,color=color.red)
        m1=1
        mc=omc
        nx=mc-1
        while(mc>1):
            xx=(m1*x+nx*x1)/(m1+nx)
            yy=(m1*y+nx*y1)/(m1+nx)
            zz=(m1*z+nx*z1)/(m1+nx)
            xx1=(m1*x2+nx*x3)/(m1+nx)
            yy1=(m1*y2+nx*y3)/(m1+nx)
            zz1=(m1*z2+nx*z3)/(m1+nx)
            s=sphere(pos=(xx,yy,zz),radius=r*p,color=color.red)
            s=sphere(pos=(xx1,yy1,zz1),radius=r*p,color=color.red)
            m1=m1+1
            mc=mc-1
            nx=mc-1
        m1=1
        mb=omb
        ny=mb-1
        while(mb>1):
            xx=(m1*x+ny*x2)/(m1+ny)
            yy=(m1*y+ny*y2)/(m1+ny)
            zz=(m1*z+ny*z2)/(m1+ny)
            xx1=(m1*x1+ny*x3)/(m1+ny)
            yy1=(m1*y1+ny*y3)/(m1+ny)
            zz1=(m1*z1+ny*z3)/(m1+ny)
            s=sphere(pos=(xx,yy,zz),radius=r*p,color=color.red)
            s=sphere(pos=(xx1,yy1,zz1),radius=r*p,color=color.red)
            m1=m1+1
            mb=mb-1
            ny=mb-1
            
        
        m=m+1
        ma=ma-1
        n=ma-1
    mb=omb
    ma=oma
    mc=omc
    m=1
    n=mb-1
    while(mb>1):
        x=(m*list1[0][0]+n*list1[2][0])/(m+n)
        y=(m*list1[0][1]+n*list1[2][1])/(m+n)
        z=(m*list1[0][2]+n*list1[2][2])/(m+n)
        x1=(m*list1[3][0]+n*list1[6][0])/(m+n)
        
        y1=(m*list1[3][1]+n*list1[6][1])/(m+n)
        z1=(m*list1[3][2]+n*list1[6][2])/(m+n)
        x2=(m*list1[1][0]+n*list1[4][0])/(m+n)
        y2=(m*list1[1][1]+n*list1[4][1])/(m+n)
        z2=(m*list1[1][2]+n*list1[4][2])/(m+n)
        x3=(m*list1[5][0]+n*list1[7][0])/(m+n)
        y3=(m*list1[5][1]+n*list1[7][1])/(m+n)
        z3=(m*list1[5][2]+n*list1[7][2])/(m+n)
        polygon([x,y,z],[x1,y1,z1],[x3,y3,z3],[x2,y2,z2])
        s=sphere(pos=(x,y,z),radius=r*p,color=color.red)
        s=sphere(pos=(x1,y1,z1),radius=r*p,color=color.red)
        s=sphere(pos=(x2,y2,z2),radius=r*p,color=color.red)
        s=sphere(pos=(x3,y3,z3),radius=r*p,color=color.red)
        m1=1
        mc=omc
        nx=mc-1
        while(mc>1):
            xx=(m1*x+nx*x1)/(m1+nx)
            yy=(m1*y+nx*y1)/(m1+nx)
            zz=(m1*z+nx*z1)/(m1+nx)
            xx1=(m1*x2+nx*x3)/(m1+nx)
            yy1=(m1*y2+nx*y3)/(m1+nx)
            zz1=(m1*z2+nx*z3)/(m1+nx)
            s=sphere(pos=(xx,yy,zz),radius=r*p,color=color.red)
            s=sphere(pos=(xx1,yy1,zz1),radius=r*p,color=color.red)
            m1=m1+1
            mc=mc-1
            nx=mc-1
        m1=1
        ma=oma
        nz=ma-1
        while(ma>1):
            xx=(m1*x+nz*x2)/(m1+nz)
            yy=(m1*y+nz*y2)/(m1+nz)
            zz=(m1*z+nz*z2)/(m1+nz)
            xx1=(m1*x1+nz*x3)/(m1+nz)
            yy1=(m1*y1+nz*y3)/(m1+nz)
            zz1=(m1*z1+nz*z3)/(m1+nz)
            s=sphere(pos=(xx,yy,zz),radius=r*p,color=color.red)
            s=sphere(pos=(xx1,yy1,zz1),radius=r*p,color=color.red)
            m1=m1+1
            ma=ma-1
            nz=ma-1
        m=m+1
        mb=mb-1
        n=mb-1
        
        


#main(2,3,4,60,45,75,2,3,4,0.2)
#while in the display 2 is correct but 4 and 3 are interchanged
