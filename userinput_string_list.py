def user_input():
    list=[]
    a=int(input("Enter length:"))
    print(a)
    for i in range(a):
        b=float(input("enter number:"))
        list.append(b)

    return  list

print(user_input())


def string_input():
    list=[]
    a=int(input("Enter length:"))
    print(a)
    for i in range(4):
        b=str(input("enter number:"))
        list.append(b)

    return list

print(string_input())