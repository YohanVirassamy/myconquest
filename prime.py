number = int(input("Choose your number\n"))

list_of_divisors = []

def is_a_prime_number(data_number):
    test_divisor = 2

    while test_divisor < (data_number // 2 ):
        i = 0
        while i < len(list_of_divisors) and test_divisor != 2:
            divisor = list_of_divisors[i]
            if test_divisor % divisor == 0:
                test_divisor += 1
                i = 0
            else:
                i += 1

        if data_number % test_divisor != 0:
            list_of_divisors.append(test_divisor)
            test_divisor += 1
        else:
            print("%d is not prime, because it is divided by %d" % (number, test_divisor))
            break
    else:
        print("Number is prime")

is_a_prime_number(number)
