import random

print("vad heter du?")
name = input()
print("Hej " + name + " och välkommen till spelet")

#guess = int(input("Gissa ett nummer mellan 1 och 10: "))
#tal = random.randint(1, 10)
#if guess == tal: 
    #print("Rätt gissat!")
#else:
    #print("Tyvärr, rätt nummer var " + str(tal))

number_of_guesses = 3
tal = random.randint(1, 10)

while number_of_guesses > 0:
    guess = int(input("Gissa ett nummer mellan 1 och 10: "))
    if guess == tal:
        print("Rätt gissat!")
        break
    else:
        number_of_guesses -= 1
        print("Tyvärr, fel gissat. Du har " + str(number_of_guesses) + " gissningar kvar.")
        if number_of_guesses == 0:
            print("Spelet är slut. Rätt nummer var " + str(tal))