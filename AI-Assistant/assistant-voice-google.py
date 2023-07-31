import os
import openai
import subprocess
import speech_recognition as sr

def get_chat_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=550,
        temperature=0.1
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

def check_file_exists():
    if not os.path.exists("conversations.txt"):
        with open("conversations.txt", "w") as file:
            file.write("")

def read_conversations():
    messages = []
    with open("conversations.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            user_input = lines[i].strip()[len("You: "):]
            if i+1 < len(lines):  # Add this check
                ai_response = lines[i + 1].strip()[len("Smart Assistant: "):]
                messages.append({"role": "assistant", "content": ai_response})
            messages.append({"role": "user", "content": user_input})
    return messages

def store_conversation(user_input, ai_response):
    with open("conversations.txt", "a") as file:
        file.write(f"You: {user_input}\nSmart Assistant: {ai_response}\n\n")

def main():
    print("Welcome to the Smart Assistant!")
    check_file_exists()
    messages = read_conversations()
    context = "You: {}\nSmart Assistant: {}".format(
        messages[-2]["content"], messages[-1]["content"]
    ) if len(messages) >= 2 else ""

    while True:
        user_input = recognize_speech()
        if user_input is None:
            continue

        prompt = context + f"\nYou: {user_input}\nSmart Assistant:"
        response = get_chat_response(prompt)
        # response += " Can you elaborate? Give it Zazz"
        print(f"Smart Assistant: {response}")
        say(response)
        store_conversation(user_input, response)
        context = "You: {}\nSmart Assistant: {}".format(user_input, response)
        messages.append({"role": "user", "content": user_input})
        messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    openai_api_key = os.getenv('OPENAI_API_KEY')
    openai.api_key = openai_api_key
    main()
