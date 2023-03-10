
def Fibonacci(num):
    if isinstance(num,int) == False:
        return "Invalid. Must be an integer"
    elif num < 1:
        return "Invalid number choice. Must be at least 1"
    elif num == 1 or num == 2:
        return "Fibonacci number " + str(num) + " is 1"
    else:
        num1 = 1
        num2 = 1
        num3 = 0
        for x in range(3,num+1,1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
        return "Fibonacci number " + str(num) + " is " + str(num3)

print(Fibonacci(3.4))


def Fibonacci2(num):
    if isinstance(num,int) == False:
        return "Invalid. Must be an integer"
    elif num < 1:
        return "Invalid number choice. Must be at least 1"
    elif num == 1 or num == 2:
        return 1
    else:
        return Fibonacci2(num-1) + Fibonacci2(num-2)

print("Fibonacci number " + str(7) + " is " + str(Fibonacci2(7)))
