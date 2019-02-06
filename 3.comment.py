def findComments():
    file = open('code.txt','r')
    counter = 0
    for line in file:
        if line.find('#') != -1:
            counter = counter + 1
    print(counter)

findComments()
