import os
import openai
import speech_recognition as sr
from elevenlabs import generate, play

def get_chat_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=550
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the Smart Assistant!")
    print("You can start by saying 'computer'.")

    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        
        try:
            user_input = r.recognize_google(audio)
            print(f"You: {user_input}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            continue

        # if 'computer' not in user_input.lower():
        #     print("Wake word not detected. Please start your request with 'computer'.")
        #     continue

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Smart Assistant: Goodbye!")
            break
        
        # Prepare the prompt for ChatGPT
        prompt = f"You: {user_input}\nSmart Assistant:"
        
        # Get the response from ChatGPT
        response = get_chat_response(prompt)

        # Append a question to the AI's response
        response += " Can you elaborate?"

        print(f"Smart Assistant: {response}")

        # Convert the response to speech using the ElevenLabs API
        audio = generate(
            text=response,
            voice="Antoni",
            model="eleven_monolingual_v1",
            api_key=elevenlabs_api_key
        )

        play(audio)

if __name__ == "__main__":
    openai_api_key = os.getenv('OPENAI_API_KEY')
    elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')
    openai.api_key = openai_api_key
    main()
