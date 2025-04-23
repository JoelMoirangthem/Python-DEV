# Function to count the number of words in a file named 'data.txt'
def word_counting():
    count = 0  # Variable to keep track of total word count

    # Open the file 'data.txt' in read mode
    with open('data.txt') as f:
        content = f.readlines()  # Read all lines from the file into a list

        # If the file is empty, return a message
        if not content:
            return "your file is empty"

        # Loop through each line in the file
        for line in content:
            sentence = line.split()  # Split the line into words
            for _ in sentence:
                count += 1  # Count each word

    return count  # Return the total word count

# Call the function and print the result
print(word_counting())
