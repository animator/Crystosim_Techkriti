facts=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600]
pi=3.1415926535897932384
def sin(x):
    if 0<=x<=(pi/2):
        y=0
    for k in range(6):
        m=2*k+1
        y=y+(-1)**k*x**m/facts[m]
    return y
if x>=0:
    x=((x/(2*pi))%1)*2*pi
if x<=pi:
    return sin(pi-x)
else:
    return -sin(x-pi)
else:
    return -sin(-x)

def cos(x):
return sin(pi/2-x)

def tan(x):
return sin(x)/cos(x)

def cot(x):
return cos(x)/sin(x)

def sec(x):
return 1/cos(x)
def csc(x):
return 1/sin(x)

def rad(x):
return x*pi/180


