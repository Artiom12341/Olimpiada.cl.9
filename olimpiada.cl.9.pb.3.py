n=int(input("Nr. de ani="))
x=int(input("daca an bisect scrie 1 -daca nu scrie 0:"))
if x==1:
    a=n*366
    b=n*12
    c=n*8784
    print(a,"-zile",b,"-luni",c,"-ore in ",n,"ani.")
elif x==0:
    a=n*365
    b=n*12
    c=n*8760
    print(a,"-zile",b,"-luni",c,"-ore in ",n,"ani.")
else :
    print("Alege tipul anului la variabila X")