import re

#iterativo

def fatorial(n:int):
    i: int = 2
    f: int = 1
    while(i<=n):
        f = i *f 
        i = i + 1      

    return f
print("Digite um valor:")

#fatorial

def fat (n: int):
    if n == 0:
        return 1
    else:
        return n* fat(n-1)

n = int(input())
print(fat(n))