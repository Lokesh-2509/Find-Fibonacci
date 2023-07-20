def fibonacci(F):
    if F == 0:
        return 0
    elif F == 1:
        return 1
    else:
        return fibonacci(F - 1) + fibonacci(F - 2)
F = int(input("Enter the value of F: "))
result = fibonacci(F)
print(f"The {F}th Fibonacci number is: {result}")
