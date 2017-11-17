while True:
    MyNumber = input("Please enter a number: ")
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \nI asked for a number...")

print(valid_number)