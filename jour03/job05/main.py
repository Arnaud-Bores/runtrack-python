def IsPrimeNumber(number):
    isPrime = True

    for i in range(2, 11):
        if i != number and (number % i) == 0:
            isPrime = False
            break
       
    return isPrime
    
for i in range(2, 1000):
    if IsPrimeNumber(1):
        print(i)