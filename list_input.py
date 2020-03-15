def int_input(num):
    l = []
    for i in range(num):
        l.append(int(input(f"Enter number {i + 1} :")))
    return l

def str_input(num):
    l = []
    for i in range(num):
        l.append(input(f"Enter string {i + 1} :"))
    return l


print(int_input(4))
print("\n")
print(str_input(3))