a=int(input("Introduceti lungimea primei laturi="))
b=int(input("introduceti lungimea a doua laturi="))
c=int(input("introduceti lungimea a treiei laturi="))
if (a<32000) and (b<32000) and (c<32000) and (a+b>c) and (a+c>b) and (c+b>a) :
  print("da") 
else:
  print("nu")