import os
import speech_recognition as sr

def recognize_speech():
    # Get the current directory where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Assuming the service account key file is named "service_account_key.json" in the same directory
    service_account_key_path = os.path.join(script_directory, "google_cloud_key.json")

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Optional: Adjust for ambient noise
        print("Listening...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=1)
                text = recognizer.recognize_google_cloud(audio, credentials_json=service_account_key_path)
                print("You said:", text)
            except sr.UnknownValueError:
                pass  # Ignore if the speech cannot be recognized
            except sr.RequestError as e:
                print("Sorry, there was an error with the speech recognition service:", e)
                break
            except sr.WaitTimeoutError:
                pass  # Continue listening if no speech is detected within the timeout
            except KeyboardInterrupt:
                print("Listening stopped.")
                break

if __name__ == "__main__":
    recognize_speech()
