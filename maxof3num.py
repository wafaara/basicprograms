a= float(input("Enter value of a:"))
b= float(input("Enter value of b:"))
c= float(input("Enter value of c:"))

if (a > b) and (a > c ):
    print('a is greater',a)
elif (b > a) and (b > c):
    print('b is greater',b)
else:
    print('c is greater',c)