a = int(input("Give integer number: "))
primeNumbers = [2,3,5,7,11,13,17,19,23,27]
product = []
i = 0

def primesCounter(product):
    result = ""
    for i in range(len(primeNumbers)-1):
        inputs = product.count(primeNumbers[i])
        if inputs == 1:
            result = result + "(" + str(primeNumbers[i]) + ")"
        elif inputs > 1:
            result = result + "(" + str(inputs) + "**" + str(primeNumbers[i]) + ")"
    print(result)

def analysis(subject,n):
    if primeNumbers[n] < subject:
        if subject%primeNumbers[n] == 0:
            product.append(primeNumbers[n])
            analysis(subject/primeNumbers[n],0)
            n = 0
        else:
            n = n + 1
            analysis(subject,n)
    else:
        product.append(primeNumbers[n])
        primesCounter(product)

analysis(a,i)

            
                     
            
            
    
    
        
    
