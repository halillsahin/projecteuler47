import sympy
n=646
a=[]
while True:
    n+=1
    if len(list(sympy.factorint(n).keys()))==4:
        a.append(n)
    if (n-3) in a and (n-2) in a and (n-1) in a and n in a:
        print(n-3)
        break
