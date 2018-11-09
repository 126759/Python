import random

numberlist = [random.randint(0, 1000) for i in range(50)]
print(numberlist)

total = sum(numberlist)

minimum = min(numberlist)
maximum = max(numberlist)
print("Maximum is", maximum)
print("Minimum is", minimum)

average = total/len(numberlist)
print("Average is", average)

