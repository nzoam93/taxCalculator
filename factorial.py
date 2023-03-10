# from math import factorial


# print(factorial(4))




def factorial(num):
    if num == 1:
        return 1
    else:
        product = 1
        for x in range(1,num+1):
            product = factorial(x-1)*x
        return product

print(factorial(5))


def factorial2(num):
    product = 1
    for i in range(1,num+1):
        product *= i
    return product

print(factorial2(5))
