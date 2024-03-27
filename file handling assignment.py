try:
    with open("my_file.txt", "w") as file_object:
        file_object.write("This is Ngetich\nI am 18 years old\nI attend University of Pennsylvania SEAS\n")
    print("Successfully created 'my_file.txt' and wrote initial content.")
except FileNotFoundError:
    print("Error: The file could not be created.")
except Exception as e:
    print(f"An unexpected error occurred while writing: {e}")

try:
    with open("my_file.txt", "r") as file_object:
        content = file_object.read()
    print("\nContents of 'my_file.txt':")
    print(content)
except FileNotFoundError:
    print("Error: The file 'my_file.txt' could not be found for reading.")
except Exception as e:
    print(f"An unexpected error occurred while reading: {e}")

try:
    with open("my_file.txt", "a") as file_object:
        file_object.write("\nI like bacon and eggs for breakfast\nI am Kenyan\nI am 5 foot 7 inches\n")
    print("Successfully appended content to 'my_file.txt'.")
except FileNotFoundError:
    print("Error: The file 'my_file.txt' could not be opened for appending.")
except Exception as e:
    print(f"An unexpected error occurred while appending: {e}")