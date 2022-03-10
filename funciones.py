# maximo comun divisor
def mcd(a,b):
    n=0
    while b!=0:
        n=b
        b=a%b
        a=n
    return a
# simplificacion de fraciones
def s1mp(a,b):
    m = mcd(a,b)
    c=str(int(a/m))
    d=str(int(b/m))
    return print("{}/{}".format(c,d))
# suma de fracciones
def sumfrac(a,b,c,d):
    e= int(a*d)+int(c*b)
    f= int(d*b)
    if f!=0:
        if e==0:
            return"0"
        if f==1:
            return e
        print("{}/{}".format(e,f))
    else :
        print("Indefinido")
#resta de fracciones
def subsfrac(a,b,c,d):
    e= int(a*d)-int(c*b)
    f= int(d*b)
    if f!=0:
        if e==0:
            return"0"
        if f==1:
            return e
        print("{}/{}".format(e,f))
    else :
        print("Indefinido")
#multiplicacion de fraciones
def multfrac(a,b,c,d):
    e= int(a*c)
    f= int(b*d)
    if f!=0:
        if e==0:
            return "0"
        if f==1:
            return e
        print("{}/{}".format(e,f))
    else:
        print("Indefinido")
# division de fracciones
def divfrac(a,b,c,d):
    e= int(a*d)
    f= int(b*c)
    if f!=0:
        if e==0:
            return "0"
        if f==1:
            return e
        print("{}/{}".format(e,f))
    else:
        print("Indefinido")