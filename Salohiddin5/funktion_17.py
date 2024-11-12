def my_function(*args):
    prod = 1
    for i in args:
        prod *= i
    return prod
print(my_function(5, 6, 3, 11))