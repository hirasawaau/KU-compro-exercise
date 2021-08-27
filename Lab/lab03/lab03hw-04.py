def even_check(num: int):
    print('The number is odd' if num % 2 == 1 else 'The number is even')


def prime_check(num: int):
    for i in range(2, num):
        if num % i == 0:
            print('The number is not prime')
            return
    print('The number is prime')


num = int(input('Number : '))
even_check(num)
prime_check(num)