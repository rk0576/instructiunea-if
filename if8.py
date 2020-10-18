a1a=int(input("Introduceti numarul bilelor albe mici:"))
b1a=int(input("Introduceti numarul bilelor albe mari:")) 
a1r=int(input("Introduceti numarul bilelor rosii mici:")) 
b1r=int(input("Introduceti numarul bilelor rosii mari:")) 
a1v=int(input("Introduceti numarul bilelor verzi mici:")) 
b1v=int(input("Introduceti numarul bilelor verzi mari:"))
print("Totalul bilelor:",a1a+b1a+a1r+b1r+a1v+b1v)
if a1a+a1r+a1v>b1a+b1r+b1v:
    print("Mari:",b1a+b1r+b1v,"bile")
else:
    print("Mici:",a1a+b1a+a1v,"bile")
if (a1a+b1a>a1r+b1r) and (a1a+b1a>a1v+b1v):
    print("Albe:",a1a+b1a,"bile")
elif (a1r+b1r>a1a+b1a) and (a1r+b1r>a1v+b1v):
    print("Rosii:",a1r+b1r,"bile")
else:
    print("Verzi:",a1v+b1v,"bile")