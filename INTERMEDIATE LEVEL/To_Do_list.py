import csv  # Import the csv module to work with CSV files

file_name = 'Task.csv'  # File to store tasks

# Main function for the to-do list application
def To_do_lst():
    try:
        condition = True  # Controls the main loop
        while condition:
            # Menu for user to choose an option
            choosing = int(input("Enter your desire option from the below:\n"
                                 "1.Task and status writing\n"
                                 "2.Delete your Task\n"
                                 "3.Veiw my Task\n"
                                 "4.Exit\n  : "))

            # Using match-case to handle the chosen option
            match choosing:
                case 1:
                    # Adding a task
                    Serial = input("Enter Serial Number : ")
                    Task = input("Enter your Task : ")
                    Status = input("Status : ")
                    adding(Serial, Task, Status)

                case 2:
                    # Deleting a task
                    show()  # First, show existing tasks
                    Task = input("Enter the serial number that you want to delete : ")
                    delete(Task)

                case 3:
                    # Show all tasks
                    show()

                case 4:
                    # Exit the loop
                    condition = False

                case _:
                    # If invalid option is selected
                    print("Enter correct option")
    except Exception:
        print("FILE NOT FOUND")  # Catch-all for any errors

# Function to add a task to the CSV file
def adding(Serial, Task, Status):
    with open(file_name, 'a', newline='') as file:
        writing = csv.writer(file)
        writing.writerow([Serial, Task, Status])  # Write the task as a new row
        print("Successfully added ✅✅")

# Function to show all tasks
def show():
    try:
        with open(file_name, 'r', newline='') as file:
            reading = list(csv.reader(file))  # Read all rows from the CSV
            if not reading:
                print("Task is not found")  # If file is empty
            else:
                for line in reading:
                    for each in line:
                        print(each, end=" ")  # Print each value in the row
                    print()  # New line after each task
                print("\n")
    except Exception:
        print("File is not found")

# Function to delete a task based on Serial Number
def delete(Task):
    try:
        temp_data = []  # Temporary list to store tasks we want to keep
        condition = False  # To check if the task was found
        with open(file_name, 'r', newline='') as file:
            reading = list(csv.reader(file))
            if not reading:
                print("Task not found")
            else:
                for line in reading:
                    if line[0] != Task:
                        temp_data.append(line)  # Keep tasks that don't match the Serial
                    else:
                        condition = True  # Mark as found

        if condition:
            with open(file_name, 'w', newline='') as writing_file:
                writing = csv.writer(writing_file)
                for line in temp_data:
                    writing.writerow(line)  # Rewrite file with tasks to keep
                print("successfully remove")
        else:
            print("NO task")  # If task with given Serial not found
    except Exception:
        print("File not found")

# Start the to-do list application
To_do_lst()
