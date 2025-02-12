def numberFactors(num):
    counter = 0
    for i in range(1,num+1):
        if num % i == 0:
            counter+= 1
    return counter

for i in range(500,5000):
    if numberFactors(i**2+i) > 500:
        print(i**2+i)
        break