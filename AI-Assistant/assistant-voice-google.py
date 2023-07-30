import os
import openai
import subprocess
import speech_recognition as sr

def get_chat_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=550
    )
    return response.choices[0].text.strip()

def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        user_input = r.recognize_google(audio)
        print(f"You: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Speech Recognition service; {e}")
        return None

def say(text):
    subprocess.run(["say", text])

def main():
    print("Welcome to the Smart Assistant!")

    while True:
        user_input = recognize_speech()
        if user_input is None:
            continue

        # Prepare the prompt for ChatGPT
        prompt = f"You: {user_input}\nSmart Assistant:"

        # Get the response from ChatGPT
        response = get_chat_response(prompt)

        # Append a question to the AI's response
        response += " Can you elaborate? Give it Zazz"

        print(f"Smart Assistant: {response}")

        # Use macOS text-to-speech for response
        say(response)

if __name__ == "__main__":
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = openai_api_key
    main()