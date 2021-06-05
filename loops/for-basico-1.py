def basico():
    numbers = 151
    for number in range(numbers):
        print(number)

def multiplosdecinco():
    for i in range(201):
        number = i*5
        if i==0:
            continue
        else:
            print(number)

def contardojoway():
    for i in range (100):
        if i==0:
            print(i)
        elif i%10==0:
            print("Coding Dojo")
        elif i%5==0:
            print("Coding")
        else:
            print(i)

def toobig():
    sum = 0
    for i in range(500000):
        sum+=i
    print(sum)

def regresiva():
    for i in range(2018, 0, -4):
        print(i)

def flexible(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if i%mult == 0:
            print(i)

def isUDI(n):
    if n==1:
        return False
    i = 2
    while (i*i <=n):
        if (n%i == 0):
            return i
        i += 1
    return True

def printprimes():
    for i in range(1001):
        if i==0:
            continue
        if isUDI(i)==True:
            print(i)
