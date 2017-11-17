import random
Choose_Number = ["1","2","3","4"]
for i in range(1,5):
    chosen = random.choice(Choose_Number)
    print(chosen)
    Choose_Number2.remove(chosen)
