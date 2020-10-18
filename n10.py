a=int(input("Numarul de gaini="))
b=int(input("Numarul de boabe de porumb="))
c=b//a
d=b-c*a
if c<d:
    print("Curcanul mai mult cu",d-c,"boabe")
if c>d:
    print("Gainile mai mult cu",c-d,"boabe")
else:
    print("Egalitate")
