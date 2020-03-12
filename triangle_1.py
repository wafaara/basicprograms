
#Triangle is valid if sum of its any two sides is greater than the third side

a= int(input("Enter value of a:"))
b= int(input("Enter value of b:"))
c= int(input("Enter value of c:"))


#
# if (a+b > c) or (a+c > b) or (b+c > a):
#     print("Triangle is valid")
# else:
#     print("not valid")

def triangle(a,b,c):
    if (a + b > c) or (a + c > b) or (b + c > a):
        x = "Valid triangle"
        return  x
    else:
        x= "not valid"
        return x

# print(tirangle(2,7,3))
print(triangle(a,b,c))