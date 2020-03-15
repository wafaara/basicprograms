
def positive_negative(number_list):
    positive = []
    negative = []

    for a in number_list:
        if  a >= 0:
             positive.append(a)
        else:
           negative.append(a)
    return  positive,negative

number_list = [-1,3,5,8,-6,-10,2]
positive,negative = positive_negative(number_list)
print('positive',positive)
print('negative',negative)