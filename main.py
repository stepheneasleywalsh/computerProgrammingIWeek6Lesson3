def factorial(x):
    if x <= 0:
        return("Error")
    elif x == 1:
        return 1
    else:
        return x*factorial(x-1)

x = int(input("Input an x and I will calculate x! "))

print(factorial(x))