
a=[]
for i in range(4):
    b=int(input("enter number:"))
    a.append(b)
    print(a)
for b in a:
    if b%2 == 0:
        print('even number',b)
    else:
        print('odd number',b)