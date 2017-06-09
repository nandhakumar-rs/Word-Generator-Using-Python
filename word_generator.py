import random,string

vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
letter = string.ascii_lowercase
print("For Random Vowels => 'v' |||| For Random Consonants =>'c' |||| For Random Letters |||| For Other Letter type anything")

# Generate words
def generate_word(number):
    input1 = input("which letter to the first 'v' or 'c' or 'l' or any ???:")
    input2 = input("which letter to the second 'v' or 'c' or 'l' or any ???:")
    input3 = input("which letter to the third 'v' or 'c' or 'l' or any ???:")
    for i in range(number):
        word = ""
        if input1 == 'v':
            word += random.choice(vowels)
        elif input1 == 'c':
            word += random.choice(consonants)
        elif input1 == 'l':
            word += random.choice(letter)
        else:
            word += random.choice(input1)
        if input2 == 'v':
            word += random.choice(vowels)
        elif input2 == 'c':
            word += random.choice(consonants)
        elif input2 == 'l':
            word += random.choice(letter)
        else:
            word += random.choice(input2)
        if input3 == 'v':
            word += random.choice(vowels)
        elif input3 == 'c':
            word += random.choice(consonants)
        elif input3 == 'l':
            word += random.choice(letter)
        else:
            word += random.choice(input3)
        print(word)

# This loop works until user says 'no'
while True:
    number = input("How many words you need ???:")
    generate_word(int(number))
    decision = input("Do want to continue... 'yes' or 'no' ???:")
    if (decision == 'yes' ):
        continue
    else:
        print("Thank You!!!")
        break