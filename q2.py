# Set the secret number
Secret_number = 5

# Ask the user to guess until they get it right
Guess = int(input("Guess the secret number: "))


while Guess != Secret_number:
    print ("Wrong, try again.")
    Guess = int(input("Guess the secret number: "))
print("Correct!")