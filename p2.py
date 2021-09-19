
# ----- First problem -----


def read_year():
    while True:
        try:
            year = int(input("Write the year:"))  # check is year is a number
            if year < 0:  # check if it is a negative value
                raise ValueError
            else:
                return year
        except ValueError:
            print("Oops! That was not a natural number.  Try again...")


def check_for_leap_year(year):
    # A year is leap year if the following conditions are satisfied:
    # 1. Year is multiple of 400.
    # 2. Year is multiple of 4 and not multiple of 100
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def read_days(year):
    while True:
        try:
            day = int(input("Write the day:"))  # check if it is a number
            if day < 0:
                raise ValueError
            elif check_for_leap_year(year) and day > 366:  # for leap year: check if is is in the interval [1,366]
                raise ValueError
            elif not check_for_leap_year(year) and day > 365:  # for normal year: check if is is in the interval [1,365]
                raise ValueError
            else:
                return day
        except ValueError:
            print("Oops! That was not a natural number.  Try again...")


def get_suffix(number):  # get the suffix at the end of the number
    if 11 <= number <= 13:
        return "th"

    if number % 10 == 1:
        return "st"
    elif number % 10 == 2:
        return "nd"
    elif number % 10 == 3:
        return "rd"
    else:
        return "th"


def display(day, month, year):  # we display the result
    switcher = {
        0: "January",
        1: "February",
        2: "March",
        3: "April",
        4: "May",
        5: "June",
        6: "July",
        7: "August",
        8: "September",
        9: "October",
        10: "November",
        11: "December"
    }
    print(switcher.get(month, "Error"), f"{day}{get_suffix(day)},", year)


def extract_days(total_days, month, month_days, year):  # we decrease the month's total days from our total days
    if total_days - month_days[month] <= 0:
        # if the condition is true => we have found the day & month, so we stop searching
        display(total_days, month, year)
        return True, total_days
    else:
        # we didn't find anything, so we continue the searching
        total_days -= month_days[month]
        return False, total_days


def find_month(total_days, year):
    stop = False  # we use it to know when the for loop should stop
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_for_leap_year(year):  # if it is a leap year
        month_days[1] = 29  # February has 29 days

    for month in range(12):
        if stop:
            break
        else:
            stop, total_days = extract_days(total_days, month, month_days, year)
        '''
        if month <= 6:  # until July
            stop, total_days = first_seven_months(month, total_days, year)
        else:
            stop, total_days = last_five_months(month, total_days)
    '''


if __name__ == '__main__':
    year = read_year()
    days = read_days(year)
    find_month(days, year)

# ----- Second problem -----
'''
from math import sqrt


def read():
    while True:
        number = int(input("Write the number:"))
        try:
            if number <= 0:
                raise ValueError
            else:
                return number
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")


def display(p1, p2):
    print("The twin prime numbers p1 and p2 immediately larger than the given non-null natural number are", p1, "and", p2)


def verify_if_prime(value):
    if value == 0 or value == 1:
        return False
    if value == 2:
        return True
    if value % 2 == 0:
        return False
    value_root = int(sqrt(value))
    for divisor in range(3, value_root+1, 2):
        if value % divisor == 0:
            return False
    return True


def are_twins(p1, p2):
    if verify_if_prime(p1):
        if verify_if_prime(p2):
            return True
    return False


def twin_prime_numbers(number):
    while True:
        number += 1
        p1 = number
        p2 = number + 2
        if are_twins(p1, p2):
            display(p1, p2)
            break


if __name__ == '__main__':
    number = read()
    twin_prime_numbers(number)
'''

# ----- Third number -----
'''

def read():
    while True:
        number = int(input("Write the number:"))
        try:
            if number <= 2:
                raise ValueError
            else:
                return number
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")


def fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


def display(m):
    print(m)


if __name__ == '__main__':
    number = read()
    m = fibonacci(number)
    display(m)

'''

# ----- Fourth problem -----
'''
from math import sqrt


def read():
    while True:
        number = int(input("Write the number:"))
        try:
            if number < 0:
                raise ValueError
            else:
                return number
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")


def proper_factors(number):
    value_root = int(sqrt(number))
    p = 1
    for i in range(2, value_root):
        if number % i == 0:
            p *= i
            p *= number / i
    if value_root ** 2 == number:
        p *= value_root
    return p


def display(p, n):
    print("The product of all the proper factors of", n, "is:", p)


if __name__ == '__main__':
    number = read()
    product = int(proper_factors(number))
    display(product, number)
        

'''

# ----- Fifth problem -----
'''

def read():
    while True:
        number = int(input("Write the number:"))
        try:
            if number <= 0:
                raise ValueError
            else:
                return number
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")


def count_of_digits(number):
    nr_digits = 0
    while number > 0:
        number = int(number / 10)
        nr_digits += 1
    return nr_digits


def palindrome(number):
    nr = count_of_digits(number)
    palindrome_number = 0
    nr -= 1
    while number > 0:
        digit = int(number) % 10
        number = int(number / 10)
        palindrome_number += digit * (10 ** nr)
        nr -= 1
    palindrome_number += number
    return palindrome_number


def display(p, n):
    print("The palindrom of", n, "is:", p)


if __name__ == '__main__':
    number = read()
    pal = palindrome(number)
    display(pal, number)

'''
# ----- Sixth problem -----

'''
def digits(number):
    digits = [False] * 10  # at first, we don't have any digits.
    while number > 0:
        digit = int(number) % 10
        digits[digit] = True
        number = int(number/10)
    return digits


def validate(l1, l2):
    if l1 == l2:
        print("Their writing in base 10 uses the same digits")
    else:
        print("Their writing in base 10 doesn't use the same digits")

if __name__ == '__main__':
    n1 = int(input("Write the first number:"))
    n2 = int(input("Write the second number:"))
    first_list_of_digits = digits(n1)
    second_list_of_digits = digits(n2)
    validate(first_list_of_digits, second_list_of_digits)
'''
