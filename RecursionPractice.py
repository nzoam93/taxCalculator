def factorialRecursive(num):
    if num == 1:
        return 1
    else:
        return num * factorialRecursive(num-1)

print("Factorial Recursive:",factorialRecursive(5))

def additionRecursive(num):
    if num == 1:
        return 1
    else:
        return num + additionRecursive(num-1)

def fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        sum = 0
    for i in range(2,num):
        sum += (i-1 + i-2)
    return sum

print("Fibonacci:", fibonacci(2))

print(additionRecursive(10))
