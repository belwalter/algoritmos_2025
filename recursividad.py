

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

def fib_iter(number):   # n
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

# print(suma(5))


# producto(n, m) = n * producto(n, m-1) --> producto(n, m) m == 1 = n



# for i in range(6):
#     print(fib(i))
#     input()
# print(fib(50))

# result = factorial_iter(5)
# print(result)


# 7 * 3 = 7 + 7 + 7


numbers = [1, 3, 4, 5 ,6]

def bus_bin_iter(array, value):
    first = 0
    last = len(array) -1
    position = -1
    while first <= last and position == -1:
        middle = (first + last) // 2
        if array[middle] == value:
            position = middle
        elif array[middle] > value:
            last = middle -1
        else:
            first = middle + 1
    
    return position


def bus_bin_rec(array, value, first, last):
    middle = (first + last) // 2
    if first >= last:
        return -1
    elif array[middle] == value:
        return middle
    else:
        if array[middle] > value:
            return bus_bin_rec(array, value,first, last -1)
        else:
            return bus_bin_rec(array, value, first+1, last)



# print(bus_bin_iter(numbers, 6))
# print(bus_bin_rec(numbers, 0, 0, len(numbers)))