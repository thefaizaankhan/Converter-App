import pyttsx3
import os

# Initialize the speech engine
engine = pyttsx3.init()

# Get the file path or name from the user
file_input = input("Enter the file path or name: ")

# Check if the input is a file path
if os.path.isfile(file_input):
    file_path = file_input
else:
    # Assume the file is in the same directory as the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_input)

# Check if the file exists
if os.path.isfile(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            text = file.read()

        # Check if the file is not empty
        if text.strip():
            # Convert the text to speech
            engine.say(text)
            engine.runAndWait()
        else:
            print("Error: File is empty.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"Error: The file '{file_input}' was not found.")
