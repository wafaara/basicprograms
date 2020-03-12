n1= float(input("Enter value of n1:"))
n2= float(input("Enter value of n2:"))
n3= float(input("Enter value of n3:"))
n4= float(input("Enter value of n4:"))

if    (n1 > n2) and (n1 > n3 ) and (n1 > n4):
    print('n1 is greater',n1)
elif  (n2 > n1) and (n2 > n3 ) and (n1 > n4):
    print('n2 is greater',n2)
elif  (n3 > n1) and (n3 > n2 ) and (n3 > n4):
    print('n3 is greater',n3)
else:
    print('n4 is greater',n4)