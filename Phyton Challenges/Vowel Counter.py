# Calculating number of vowels using for loop
count = 0
word = raw_input("Please enter a phrase: ")
for letter in word:
    if letter in "aeiou":
        count +=1
print "The number of vowels are: ", count
raw_input("\n\nPress the enter key to continue\n\n")
# Calculatint number of vowels using while loop
word = raw_input("Please enter a second phrase: ")
numVowels = 0
count = 0
vowel = "aeiou"
while count < len(word):
    if (word[count] in vowel):
        numVowels = numVowels + 1
print numVowels
