

# n! = n * (n-1)!

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)


def factorial_iter(number):
    acumulador = 1
    while number != 0:
        acumulador = acumulador * number
        number -= 1
    return acumulador



# fib(n) = fib(n-1) + fib(n-2)    -> fib(0) = 0 ->fib(1) =1

def fib(number):
    if number == 0 or number == 1:
        return number
    else:
        return fib(number-1) + fib(number-2)

def fib_iter(number):
    if number == 0 or number == 1:
        return number
    
    result_1 = 0
    result_2 = 1
    result = 0
    for i in range(2, number+1):
        result = result_1 + result_2
        result_1 = result_2
        result_2 = result

    return result


# suma(n) = n + suma(n-1)  -> suma(0) = 0


def suma(number):
    if number == 0:
        return number
    else:
        return number + suma(number-1)

print(suma(5))


# producto(n, m) = n * producto(n, m-1) --> producto(n, m) m == 1 = n



# for i in range(6):
#     print(fib(i))
#     input()
# print(fib(50))

# result = factorial_iter(5)
# print(result)


7 * 3 = 7 + 7 + 7
