def my_function_iterative(x):
    total = 0
    for i in range(1, x + 1):
        total += i
    return total

print(my_function_iterative(5)) #This will work even for large x without RecursionError 