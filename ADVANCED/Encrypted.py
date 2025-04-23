# Function to read the content of a file from the "ADVANCED" folder
def read_file(file_name):
    try:
        # Tries to open the file in read mode
        with open("ADVANCED/" + file_name, 'r') as files:
            return files.read()  # Returns the content of the file
    except FileNotFoundError:
        print('File not found')  # Prints message if file is not found
        return None  # Returns None if file is not found

# Takes input from the user for the file name, removes extra spaces and converts it to lowercase
file = input('Enter the file name : ').strip().lower()
# Prints the content of the file
print(read_file(file))

# Function to encode the text from the file using Caesar cipher
def encoding(files, shift):
    text = read_file(files)  # Reads the content of the file
    if text is not None:
        result = ''  # Empty string to store the encoded result
        for letter in text:
            if letter.isalpha():  # Checks if the character is a letter
                base = ord('A') if letter.isupper() else ord('a')  # Sets base ASCII for upper or lower case
                result += chr((ord(letter)-base + shift) % 26 + base)  # Shifts the letter and adds to result
            else:
                result += letter  # Keeps non-alphabet characters unchanged
        # Asks user for a new file name to save the encoded text
        newfile = input("In which name you want to save the file : ")
        with open(newfile,'w') as f:
            f.write(result)  # Writes the encoded text to the new file
        return 'File save successfull'  # Returns success message
    else:
        return text  # Returns None if the file was not found

# Function to decode the text from the file using Caesar cipher
def decoding(files, shift):
    text = read_file(files)  # Reads the content of the file
    if text is not None:
        result = ''  # Empty string to store the decoded result
        for letter in text:
            if letter.isalpha():  # Checks if the character is a letter
                base = ord('A') if letter.isupper() else ord('a')  # Sets base ASCII for upper or lower case
                result += chr((ord(letter) - base - shift) % 26 + base)  # Reverses the shift to decode
            else:
                result += letter  # Keeps non-alphabet characters unchanged
        return result  # Returns the decoded text
    else:
        return text  # Returns None if the file was not found
