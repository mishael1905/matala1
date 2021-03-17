def atzeret(i:float):
    sum=i
    while(i>1):
        sum=sum*(i-1)
        i=i-1
    return(sum)
        

def hezka(x:float,i:float):
    if i==0:
        return(1)
    elif x==0:
        return(0)
    else:
        j=0
        sum=1
        while j<i:
            sum=sum*x
            j=j+1
        return (sum)
  

    

def expo(x:float):
    i=1
    sum=0
    while(i<100):
        sum=sum+((hezka(x,i)/atzeret(i)))
        i=i+1
    result = float('%0.6f' % sum)
    return(result+1)
  
 
    
def ln(x):
    i=0
    sum=0
    while i<1000:
        sum=sum+ 2*((x-expo(sum))/(x+expo(sum)))   
        i=i+1
    result = float('%0.6f' % sum)
    return(result)
  
   
    
def XtimesY(x,y):
    if(x<=0):
        return(0)
    z1=ln(x)
    z2=y*z1
    a = expo(z2)
    result = float('%0.6f' % a)
    return(result)
  

def sqrt(y,x):
    return(XtimesY(x,1/y))
    
        
def calculate(x:float)->float:
    if(x==0):
        return(0)
    ex=((expo(x))*(expo(x*ln(7)))*(1/x)*(sqrt(x, x)))
    result = float('%0.6f' % ex)
    return(result)