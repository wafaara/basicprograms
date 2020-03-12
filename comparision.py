
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

if a > b:
    return a-b
else:
    return b-a

if a == b:
    return 0
elif a > b:
    return a-b
else:
    return b-a