num = int(input("Enter a number: "))

# prime numbers are greater than 1
factors = []
count = 0
isPrime = True
if num > 1:
    # check for factors
    for i in range(2, num):
        count += 1
        if (num % i) == 0:
            factors.append(i)
            isPrime = False

    else:
            factors.append(num)



if isPrime == False:
    factors = ", ".join(str(e) for e in factors)
    print(str(
        num) + " " + "Is a composite number and factors are:  " + factors + "\n With this method number of iteration  is:" + str(
        count))
else:
    factors = ", ".join(str(e) for e in factors)
    print(str(
        num) + " " + "Is a prime number and factors are: " + factors + "\n With this method number of iteration  is:" + str(
        count))