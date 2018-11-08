class roman:
    def int_to_Roman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // values[i]):
                roman_num += symbol[i]
                num -= values[i]
            i += 1
        return roman_num

userinput = int(input("Enter an integer value:..."))

print(roman().int_to_Roman(userinput))

