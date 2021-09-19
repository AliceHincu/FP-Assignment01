
# ----- First problem -----

from math import sqrt


def read():
    while True:
        try:
            value = int(input("Write the number:"))  # check is the value is a int number
            if value < 0:  # check if it is a negative value
                raise ValueError
            else:
                return value
        except ValueError:
            print("Oops! That was not a natural number.  Try again...")


def verify_if_prime(value):  # we check if the value is a prime number
    if value == 0 or value == 1:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    value_root = int(sqrt(value))  # the squared root of the value
    for divisor in range(3, value_root+1, 2):
        if value % divisor == 0:
            return False
    return True


def find_prime_number(number):  # we try to find the first prime number
    '''
    - write what the function does
    :param number:
    :return:
    '''
    value = number + 1
    while True:
        if verify_if_prime(value):
            return value
        value = value + 1


def display(value_init, value_final):
    print("The first prime number larger than", value_init, "is:", value_final)


if __name__ == '__main__':
    number = int(read())
    result = find_prime_number(number)
    display(number, result)


# ----- Second problem -----
'''
from math import sqrt


def read():
    value = input("Write the even number: ")
    return value


def create_list(value):  # we create a list in which we save the boolean value for each number
    # (we include 0 and 1 for better scripting)
    the_list = [True] * (int(value)+1)  # at first, every number will be considered as a prime number
    return the_list


def sieve_of_eratosthenes(maximum_value):  # the algorithm for the Sieve of Eratosthenes
    prime_list = create_list(maximum_value)
    value_root = int(sqrt(maximum_value))
    for i in range(2, value_root+1):  # we ignore 0 and 1
        if prime_list[i]:  # if the number is prime
            for j in range(i*i, int(maximum_value)+1, i):
                # its multiplies won't be considered prime (we are allowed to start from i*i)
                prime_list[j] = False  # we mark the number as a number which is not prime
    return prime_list  # we return the list that checks what numbers are prime


def goldbach_hypothesis(number):
    prime_list = sieve_of_eratosthenes(number)
    for p1 in range(2, int(int(number)/2)):
        if prime_list[p1]:  # if first number is prime
            p2 = number - p1
            if prime_list[p2]:  # if second number is prime
                print(number, " = ", p1, " + ", p2)  # we can have multiple sums


def display(number):
    if int(number) % 2 == 1:
        print(number, "it is not an even number")
    else:
        print("The sums:")
        goldbach_hypothesis(number)


if __name__ == '__main__':
    number = int(read())
    display(number)


'''

# ----- Third problem -----
'''


def read():
    number = input("Write the number:")
    return number


def create_list(digits):
    list_of_digits = []
    for i in range(0, 10):
        while digits[i]:
            list_of_digits.append(i)
            digits[i] -= 1
    return list_of_digits


def separate_digits(number):
    digits = [0] * 10  # at first, we don't have any digits.
    count_of_digits = 0
    while number > 0:
        digit = int(number) % 10
        digits[digit] += 1
        number = int(number/10)
        count_of_digits += 1
    list_of_digits = create_list(digits)
    return int(count_of_digits), list_of_digits


def create_number(c_o_d, l_o_d):
    new_number = 0
    index = 0
    c_o_d -= 1
    while c_o_d:
        new_number = int(l_o_d[index] * (10 ** c_o_d)) + new_number
        c_o_d -= 1
        index += 1
    new_number += l_o_d[index]
    return new_number


def display(m):
    print("The minimal natural number m formed with the same digits is", m)


if __name__ == '__main__':
    number = int(read())
    count_of_digits, list_of_digits = separate_digits(number)
    m = create_number(count_of_digits, list_of_digits)
    display(m)

'''

# ----- Fourth problem -----

'''
def read():
    number = input("Write the number:")
    return number


def create_list(digits):
    list_of_digits = []
    for i in range(0, 10):
        while digits[i]:
            list_of_digits.insert(0, i)
            digits[i] -= 1
    return list_of_digits


def separate_digits(number):
    digits = [0] * 10  # at first, we don't have any digits.
    count_of_digits = 0
    while number > 0:
        digit = int(number) % 10
        digits[digit] += 1
        number = int(number/10)
        count_of_digits += 1
    list_of_digits = create_list(digits)
    return int(count_of_digits), list_of_digits


def create_number(c_o_d, l_o_d):
    new_number = 0
    index = 0
    c_o_d -= 1
    while c_o_d:
        new_number = int(l_o_d[index] * (10 ** c_o_d)) + new_number
        c_o_d -= 1
        index += 1
    new_number += l_o_d[index]
    return new_number


def display(m):
    print("The largest natural number written with the same digits", m)


if __name__ == '__main__':
    number = int(read())
    count_of_digits, list_of_digits = separate_digits(number)
    m = create_number(count_of_digits, list_of_digits)
    display(m)

'''

# ----- Fifth problem -----
'''
from math import sqrt


def read():
    value = input("Write the number: ")
    return value


def verify_if_prime(value):
    # is_prime = True
    if value == 0 or value == 1:
        return False
    if value == 2:
        return True
    if int(value) % 2 == 0:
        return False
    value_root = int(sqrt(int(value)))
    for divisor in range(3, value_root+1):
        if int(value) % int(divisor) == 0:
            return False
    return True


def find_prime_number(number):
    value: int = int(number) - 1
    if number <= 2:
        return 0
    while True:
        if verify_if_prime(value):
            return value
        value: int = int(value) - 1


def display(value_init, value_final):
    if value_final == 0:
        print("Two is the smallest prime number!")
    else:
        print("The largest prime number smallest than ", value_init, " is: ", value_final)


if __name__ == '__main__':
    number = int(read())
    result = find_prime_number(number)
    display(number, result)

'''
# Finish
