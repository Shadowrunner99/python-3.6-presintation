numberOfIntervals = int(input("Give number of intervals"))
intervalsList = []

def sumIntervals(numberOfIntervals):
 sumInterval = 0
 
 for i in range(numberOfIntervals):
  intervalStart = int(input("Give interval begining"))
  intervalEnd = int(input("Give interval end"))
  intervalsList.append(intervalStart)
  intervalsList.append(intervalEnd)
  
 for j in range(numberOfIntervals * 2):
  if j % 2 != 0:
   intervalDiff = intervalsList[j] - intervalsList[j-1]
   sumInterval = sumInterval + intervalDiff
 print(sumInterval)

sumIntervals(numberOfIntervals)
