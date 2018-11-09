number = int(input("Enter a number with base 10\n")) 
  
print("a. Decimal to Hexadecimal ") 
print("b. Decimal to Binary") 
  
print("Enter your choice :- ") 
choice = input() 

if choice is 'a':  
    print("Hexadecimal form of " + str(number) + " is " + hex(number).lstrip("0x").rstrip("L")) 
                    
elif choice is 'b': 
    print("Binary form of " + str(number) + " is "+bin(number).lstrip("0b").rstrip("L"))
