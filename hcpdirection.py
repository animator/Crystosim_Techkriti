from visual import *
def drawline(list1,list2):
    l=paths.line(start=list1,end=list2,np=2)
    curve(pos=l.pos)
def drawhc(s,u,v,t,w):
    
   
   # u=1.0/u
   # v=1.0/v
   # w=1.0/w
    
    
    
    phi=pi*30/180
    h=sin(phi)*s
    r=cos(phi)*s
    x=-s/2
    y=-r
    b=s+2*h
    a=2*r
    list0=[x,y]
    list1=[x+s,y]
    list2=[x+s+h,y+r]
    list3=[x+s,y+r+r]
    list4=[x,y+r+r]
    list5=[x-h,y+r]
    list10=[x,y,4]
    list11=[x+s,y,4]
    list12=[x+s+h,y+r,4]
    list13=[x+s,y+r+r,4]
    list14=[x,y+r+r,4]
    list15=[x-h,y+r,4]
    drawline(list0,list1)
    drawline(list1,list2)
    drawline(list2,list3)
    drawline(list3,list4)
    drawline(list4,list5)
    drawline(list5,list0)
    drawline(list10,list11)
    drawline(list11,list12)
    drawline(list12,list13)
    drawline(list13,list14)
    drawline(list14,list15)
    drawline(list15,list10)
    drawline(list0,list10)
    drawline(list1,list11)
    drawline(list2,list12)
    drawline(list3,list13)
    drawline(list4,list14)
    drawline(list5,list15)
    line=paths.line(start=(0,0,0),end=(0,0,10),np=2)
    curve(pos=line.pos,color=color.red)
    l2=paths.line(start=(0,0,0),end=(x,y,0),np=2)
    curve(pos=l2.pos,color=color.blue)
    #a2=atan2(r,(x+2*s+h-s/2))
   # lh=[u*cos(a2),h*sin(a2),0]
    l3=paths.line(start=(0,0,0),end=(x+s+h,y+r,0),np=2)
    curve(pos=l3.pos,color=color.orange)
    l4=paths.line(start=(0,0,0),end=(x,y+2*r,0),np=2)
    curve(pos=l4.pos,color=color.cyan)
   # a4=atan2((y1-r),(x1-s/2))
   # lh1=[v*cos(a4),v*sin(a4),0]
   # lh2=[s/2,r,w]
   # faces(pos=[(u*cos(a2),h*sin(a2),0),(v*cos(a4),v*sin(a4),0),(s/2,r,w)],color=color.red)
   # faces(pos=[(s/2,r,w),(v*cos(a4),v*sin(a4),0),(u*cos(a2),h*sin(a2),0)],color=color.red)
    
   # print lh
    m=max(u,v,w)
    u=u*1.0/m
    v=v*1.0/m
    w=w*1.0/m
    if(u==0 and v==0 and t==0):
      # convex(pos=(list0,list1,list2,list3,list4,list5),color=color.red)
       z=(list0[0]+1j*list0[1])*exp(1j*(pi/2))
       xx=z.real
       yy=z.imag
       a=arrow(pos=(0,0,0),axis=(0,0,4),color=color.blue)
       return
    if(w==0 and t==0 and v==0 and u!=0):
                a=arrow(pos=(0,0,0),axis=(x,y,0),color=color.blue)
                #l=paths.line(start=(0,0,0),end=(x,y,0))
                #curve(pos=l.pos,color=color.red)
                return
    if(w==0 and t==0 and u==0 and v!=0):
                a=arrow(pos=(0,0,0),axis=(x+s+h,y+r,0),color=color.blue)
    if (w==0):
        
        if(t==0 and (u !=0 and v!=0)):
            m=abs(u)
            n=1-m
            #print s/2,r
            #print m,n
            px1=(m*x+n*0)
            py1=(m*y+n*0)
            #print px1,py1
            if(u<0):
               
               z=(px1+py1*1j)*exp(1j*(pi))
               px1=z.real
               py1=z.imag
            #print px1,py1
            m1=abs(v)
            n1=1-m1
            #print m1,n1
                          
            px2=(m1*(x+s+h)+n1*0)
            py2=(m1*(y+r)+n1*0)
            #print px2,py2
            #print x+s+h,y+r
            if (v<0):
            
            
               z=(px2+py2*1j)*exp(1j*(pi))
                          
               px2=z.real
               py2=z.imag
               #print px2,py2
            #print px2,py2
           # faces(pos=[(px1,py1,0),(px2,py2,0),(px2,py2,4)],color=color.blue)
            px=px1+px2
            py=py1+py2
            
            #convex(pos=[(px1,py1,0),(px2,py2,0),(px2,py2,4),(px1,py1,4)],color=color.red)
            
            a=arrow(pos=(0,0,0),axis=(px,py,0),color=color.blue)
            return
        if (u and v and t ):
            m=abs(u)
            n=1-m
            px1=(m*x+n*0)
            py1=(m*y+n*0)
            if(u<0):
               
               z=(px1+py1*1j)*exp(1j*(pi))
               px1=z.real
               py1=z.imag
            m1=abs(v)
            n1=1-m1
            px2=(m1*(x+s+h)+n1*0)
            py2=(m1*(y+r)+n1*0)
            if (v<0):
            
            
               z=(px2+py2*1j)*exp(1j*(pi))
                          
               px2=z.real
               py2=z.imag
               print px2,py2
            m2=abs(t)
            n2=1-m2
            px3=(m2*x+n2*(0))
            py3=(m2*(y+r+r)+n2*(0))
            if (t<0):
            
            
               z=(px3+py3*1j)*exp(1j*(pi))
                          
               px3=z.real
               py3=z.imag
             #  print px2,py2
            #convex(pos=[(px1,py1,0),(px2,py2,0),(px1,py1,4),(px2,py2,4)],color=color.red)
            #onvex(pos=[(px1,py1,0),(px3,py3,0),(px1,py1,4),(px3,py3,4)],color=color.red)
            z=(px1+1j*py1)*exp(1j*(pi/2))
            xx=z.real
            yy=z.imag
            a=arrow(pos=(0,0,0),axis=(xx,yy,0),color=color.blue)
            return
        
    px1=0
    py1=0
    px2=0
    py2=0
    if(w!=0):
            m3=abs(w)
            n3=1-m3
            pz4=m3*4+n3*0
            if(u!=0):
             m=abs(u)
             n=1-m
             px1=(m*x+n*0)
             py1=(m*y+n*0)
            if(u<0):
               
               z=(px1+py1*1j)*exp(1j*(pi))
               px1=z.real
               py1=z.imag
            if(v!=0):
                m1=abs(v)
                n1=1-m1
                px2=(m1*(x+s+h)+n1*0)
                py2=(m1*(y+r)+n1*0)
            if (v<0):
            
            
               z=(px2+py2*1j)*exp(1j*(pi))
                          
               px2=z.real
               py2=z.imag
              # print px2,py2
            if(t!=0):
             m2=abs(t)
             n2=1-m2
             px3=(m2*x+n2*(0))
             py3=(m2*(y+r+r)+n2*(0))
            if (t<0):
            
            
               z=(px3+py3*1j)*exp(1j*(pi))
                          
               px3=z.real
               py3=z.imag
               #print px2,py2
            
            if(u!=0  and t!=0):
                #convex(pos=[(px1,py1,0),(px3,py3,0),(0,0,pz4)],color=color.red)
                z=(px1+1j*py1)*exp(1j*(pi/2))
                xx=z.real
                yy=z.imag
                a=arrow(pos=(0,0,0),axis=(xx,yy,pz4),color=color.blue)
                return
            if(v!=0 and t!=0):
               # convex(pos=[(px2,py2,0),(px3,py3,0),(0,0,pz4)],color=color.red)
                z=(px2+1j*py2)*exp(1j*(pi/2))
                xx=z.real
                yy=z.imag
                a=arrow(pos=(0,0,0),axis=(xx,yy,pz4),color=color.blue)
                return
            #convex(pos=[(px1,py1,0),(px2,py2,0),(0,0,pz4)],color=color.red)
            px=px1+px2
            py=py1+py2
            a=arrow(pos=(0,0,0),axis=(px,py,pz4),color=color.blue)
            return
        
            
                   
            #convex(pos=[(px1,py1,0),(px3,py3,0),(px1,py1,4),(px3,py3,4)],color=color.red)
            #convex(pos=[(px1,py1,0),(0,0,pz4),(px2,py2,0)],color=color.blue)
      
  
           
           
            
            
            
#drawhc(2,1,0,0,1)     
    
    
    
    

    
    
    
