# import speech_recognition as sr

# # Initialize recognizer
# recognizer = sr.Recognizer()

# # Function to recognize speech
# def recognize_speech():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#         audio = recognizer.listen(source)  # Listen for audio input

#     try:
#         print("Recognizing...")
#         text = recognizer.recognize_google(audio)  # Recognize speech using Google Speech Recognition
#         print("You said:", text)
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#     except sr.RequestError as e:
#         print("Error fetching results; {0}".format(e))

# # Call the function
# recognize_speech()


# import speech_recognition as sr

# # Initialize the recognizer
# recognizer = sr.Recognizer()

# # Capture audio input from the microphone
# with sr.Microphone() as source:
#     print("Kindly voice out your command!")
#     audio = recognizer.listen(source)

# try:
#     recognized_text = recognizer.recognize_google(audio)
#     print("Interpreted as:", recognized_text)
# except sr.UnknownValueError:
#     print("Apologies, the audio wasn't clear enough.")
# except sr.RequestError as e:
#     print(f"There was an issue retrieving results. Error: {e}")


import speech_recognition as sr

def main():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Kindly voice out your command:")
            audio = recognizer.listen(source)

        recognized_text = recognizer.recognize_google(audio)
        print("Interpreted as:", recognized_text)
    except sr.UnknownValueError:
        print("Apologies, the audio wasn't clear enough.")
    except sr.RequestError as e:
        print(f"There was an issue retrieving results. Error: {e}")

if __name__ == "__main__":
    main()



