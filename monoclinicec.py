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

def main(a,b,c,l,w,h,ma,mb,mc,r,p):
    x0=0
    y0=0
    z0=0
    a=a*ma
    b=b*mb
    c=c*mc
    oma=ma
    omb=mb
    omc=mc
  
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
    for w in range(0,len(list)):
      s=sphere(pos=(list[w][0],list[w][1],list[w][2]),radius=r*p,color=color.red)
    
    #s=sphere(pos=(list[w][0],list[w][1],list[w][2]),radius=r*p,color=color.blue)
    e1z=(list[2][2]+list[4][2])/2
    e1x=(list[6][0]+list[4][0])/2
    e1y=(list[4][1]+list[2][1])/2
    e2x=(list[1][0]+list[3][0])/2
    e2y=(list[1][1]+list[0][1])/2
    e2z=(list[0][2]+list[1][2])/2
    if(ma==1 and mb==1 and mc==1):
         s=sphere(pos=(e1x,e1y,e1z),radius=r*p,color=color.blue)
         s=sphere(pos=(e2x,e2y,e2z),radius=r*p,color=color.blue)
    #
    #s3=sphere(pos=(list[4][0]+e1x,list[4][0],list[4][2]+e1z),radius=r*p,color=color.red)
    #s=sphere(pos=(list[1][0]+e2x,list[1][1],list[1][2]+e2z),radius=r*p,color=color.red)
    
    

#start dividing the main cube
    m=1
    n=mc-1
    ctr=0
    while (mc>1):
        i=0
        x=(m*list[0][0]+n*list[3][0])/(m+n)
        y=(m*list[0][1]+n*list[3][1])/(m+n)
        z=(m*list[0][2]+n*list[3][2])/(m+n)
        x1=(m*list[1][0]+n*list[5][0])/(m+n)
        y1=(m*list[1][1]+n*list[5][1])/(m+n)
        z1=(m*list[1][2]+n*list[5][2])/(m+n)
        x2=(m*list[2][0]+n*list[6][0])/(m+n)
        y2=(m*list[2][1]+n*list[6][1])/(m+n)
        z2=(m*list[2][2]+n*list[6][2])/(m+n)
        x3=(m*list[4][0]+n*list[7][0])/(m+n)
        y3=(m*list[4][1]+n*list[7][1])/(m+n)
        z3=(m*list[4][2]+n*list[7][2])/(m+n)
        
        
        
        if(ctr==0):
            e1z=(list[2][2]+list[4][2])/2
            e1x=(x2+list[4][0])/2
            e1y=(list[4][1]+list[2][1])/2
            e2x=(list[1][0]+x)/2
            e2y=(list[1][1]+list[0][1])/2
            e2z=(list[0][2]+list[1][2])/2
            s=sphere(pos=(e1x,e1y,e1z),radius=r*p,color=color.blue)
            s=sphere(pos=(e2x,e2y,e2z),radius=r*p,color=color.blue)
            
        if(ctr!=0 and ctr!=mc-2):
            e1z=(list4[2]+list3[2])/2
            e1x=(list4[0]+x2)/2
            e1y=(list4[1]+list3[1])/2
            e2x=(list2[0]+x)/2
            e2y=(list2[1]+list1[1])/2
            e2z=(list1[2]+list2[2])/2
            s=sphere(pos=(e1x,e1y,e1z),radius=r*p,color=color.blue)
            s=sphere(pos=(e2x,e2y,e2z),radius=r*p,color=color.blue)
        if(ctr==mc-2):
            e1z=(z3+z2)/2
            e1x=(x3+list[6][0])/2
            e1y=(y3+y2)/2
            e2x=(list[3][0]+x1)/2
            e2y=(y1+y)/2
            e2z=(z+z1)/2
            s=sphere(pos=(e1x,e1y,e1z),radius=r*p,color=color.blue)
            s=sphere(pos=(e2x,e2y,e2z),radius=r*p,color=color.blue)
        list1=[x,y,z]
        list2=[x1,y1,z1]
        list3=[x2,y2,z2]
        list4=[x3,y3,z3]
        s=sphere(pos=(x,y,z),radius=r*p,color=color.red)
        s=sphere(pos=(x1,y1,z1),radius=r*p,color=color.red)
        s=sphere(pos=(x2,y2,z2),radius=r*p,color=color.red)
        s=sphere(pos=(x3,y3,z3),radius=r*p,color=color.red)
        polygon([x,y,z],[x1,y1,z1],[x3,y3,z3],[x2,y2,z2])
        ctr=ctr+1
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
    while (ma>1):
        x=(m*list[0][0]+n*list[1][0])/(m+n)
        y=(m*list[0][1]+n*list[1][1])/(m+n)
        z=(m*list[0][2]+n*list[1][2])/(m+n)
        x1=(m*list[3][0]+n*list[5][0])/(m+n)
        y1=(m*list[3][1]+n*list[5][1])/(m+n)
        z1=(m*list[3][2]+n*list[5][2])/(m+n)
        x2=(m*list[2][0]+n*list[4][0])/(m+n)
        y2=(m*list[2][1]+n*list[4][1])/(m+n)
        z2=(m*list[2][2]+n*list[4][2])/(m+n)
        x3=(m*list[6][0]+n*list[7][0])/(m+n)
        y3=(m*list[6][1]+n*list[7][1])/(m+n)
        z3=(m*list[6][2]+n*list[7][2])/(m+n)
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
        x=(m*list[0][0]+n*list[2][0])/(m+n)
        y=(m*list[0][1]+n*list[2][1])/(m+n)
        z=(m*list[0][2]+n*list[2][2])/(m+n)
        x1=(m*list[3][0]+n*list[6][0])/(m+n)
        
        y1=(m*list[3][1]+n*list[6][1])/(m+n)
        z1=(m*list[3][2]+n*list[6][2])/(m+n)
        x2=(m*list[1][0]+n*list[4][0])/(m+n)
        y2=(m*list[1][1]+n*list[4][1])/(m+n)
        z2=(m*list[1][2]+n*list[4][2])/(m+n)
        x3=(m*list[5][0]+n*list[7][0])/(m+n)
        y3=(m*list[5][1]+n*list[7][1])/(m+n)
        z3=(m*list[5][2]+n*list[7][2])/(m+n)
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
        
        
main(2,4,3,55,60,45,1,1,1,1,0.5)


