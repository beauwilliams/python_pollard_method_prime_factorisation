import sys

val = int(input("Enter a value to factorise using Pollards p method : "))

if (len(sys.argv)>1):
    val=int(sys.argv[1])



def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
def f(x,n):
    return (x*x+3) %n


def pollard(a):
    print ("A B GCD")
    x=2
    y=2
    d=1
    while d==1:
        x=f(x,a)
        y=f(f(y,a,),a)
        d=gcd(abs(x-y),a)
        print (x,y,d)
        if d>1 and a>d:
                    return d
        if d==a:
                    return -1

print ("First factor is "+str(pollard(val)))
