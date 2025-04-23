import random as rd  # Import the random module to generate random numbers

# Function to play a number guessing game
def Guess_No():
    target = rd.randint(1, 100)  # Randomly choose a number between 1 and 100
    limit = 5  # Number of chances the user has to guess
    count = 1  # Start attempt count from 1

    # Loop until the user uses all the attempts
    while(count <= limit):
        guessing = int(input("Guess a Number from 1 to 100 : "))  # Take user input

        # If the guess is correct
        if guessing == target:
            win = "Congratulation 🎉🎉🎉🥳🥳 You guess the exact number "
            return win  # Return success message

        # If the guess is way too high
        elif guessing > (target + 10):
            print("You are guessing number in too high")

        # If the guess is way too low
        elif guessing < (target - 10):
            print("You are guessing number in too low")

        # If the guess is close, but not exact
        else:
            print("Please try Again")

        count += 1  # Increase the attempt count

    # If the user didn't guess in given attempts
    return f'You lose the game 😞😞😞 the correct number is {target}'

# Call the function and print the result
print(Guess_No())
