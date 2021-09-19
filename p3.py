# ----- Fourth problem -----
from math import sqrt


def read():  # we read the number
    while True:
        try:
            number = int(input("Write the number: "))  # check if object is int
            if number < 0:  # the number is negative => is not natural
                raise ValueError
            else:
                return number
        except ValueError:
            print("Oops! This is not a natural number! Try a different one: ")


def display(result):  # we display the result
    if result == 0:
        print("The largest perfect number smaller than the given natural number doesn't exist:")
    else:
        print("The largest perfect number smaller than the given natural number is: ", result)


def perfect_square(root, number):  # we check if the number is a perfect square
    if root * root == number:
        return True
    return False


def find_div(number):
    list_div = [1]  # at the beggining only the digit 1 is a divisor
    value_root = int(sqrt(number))  # we find the root of the square number
    for d in range(2, value_root+1):
        if number % d == 0:
            # we introduce in the list both the divisor and n/divisor
            list_div.append(d)
            list_div.append(int(number/d))
    if perfect_square(value_root, number):
        # we eliminate the duplicate of the root
        list_div.pop()
    return list_div


def sum_div(list_div):  # we add the divisors
    sum = 0
    lenght = len(list_div)
    for element in range(0, lenght):
        sum += list_div[element]
    return sum


def is_perfect(number):  # we check if the number is perfect
    div = find_div(number)  # this is the list of divisors
    sum = sum_div(div)  # this is the sum of divisors
    if sum == number:
        return True
    else:
        return False


def find_perf(number):
    if number <= 6:  # 6 is the first perfect number (we don't take 1 in account)
        return False
    else:
        while True:
            number -= 1
            if is_perfect(number):  # if we found a perfect number we stop the searching
                return number


if __name__ == '__main__':
    number = read()
    result = find_perf(number)
    display(result)
