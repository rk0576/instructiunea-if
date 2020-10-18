n1=int(input("introduceti valoarea primului numar="))
n2=int(input("introduceti valoarea al doilea numar="))
n3=int(input("introduceti valoarea al treielea numar="))
if (n1>0) and (n2>0) and (n3>0):
    if n2>n3:
        print (n2)
    if n3>n2:
        print(n3)
else:
    print(n1+n2)