def compare_numbers():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))

    if a > b:
        print("a-b")
        return a-b
    else:
        print("b-a")
        return b-a

    # if a == b:
    #     print("values are equal")
    #     return 0
    # elif a > b:
    #     print("a is greater than b")
    #     return a-b
    # else:
    #     print("b is greater than a")
    #     return b-a

print(compare_numbers())