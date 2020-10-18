n1=int(input("introduceti valoarea la primul  numar="))
n2=int(input(" introduceti valoarea la al doilea numar="))
if (n1%2==0) and (n2%2==0):
    if n1>n2:
        print(n1)
    else:
        print(n2)
elif (n1%2!=0) and (n2%2==0):
    print(n2)
elif (n1%2==0) and (n2%2!=0):
    print(n1)
else:
    print("Nu exista numere pare")