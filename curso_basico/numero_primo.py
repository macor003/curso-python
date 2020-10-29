def is_prime(number):
    count = 0
    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1

    if count == 0:
        return True
    else:
        return False


def run():
    number = int(input('Write a number between 1 - 100: '))
    if is_prime(number):
        print('The number ' + str(number) + ' is a prime number')
    else:
        print('The number ' + str(number) + ' is not a prime number')


if __name__ == '__main__':
    run()
