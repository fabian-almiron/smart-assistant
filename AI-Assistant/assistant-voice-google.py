import os
import openai
import speech_recognition as sr
from elevenlabs import generate, play
from googlesearch import search


def get_chat_response(prompt):
    if prompt.lower().startswith("you: google"):
        # Extract the search query from the prompt
        query = prompt[32:]
        search_results = list(search(query, num_results=1))
        if search_results:
            return search_results[0]
        else:
            return "I couldn't find any relevant search results for your query."
    else:
        # Use OpenAI to get the response
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=550
        )
        return response.choices[0].text.strip()


import os
import openai
import speech_recognition as sr
from elevenlabs import generate, play

# Load API keys from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
elevenlabs_api_key = os.getenv('ELEVENLABS_API_KEY')

# Set OpenAI API key
openai.api_key = openai_api_key

def get_chat_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the engine you have access to
        prompt=prompt,
        max_tokens=550
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the Smart Assistant!")
    print("You can start by asking me anything or giving me a command.")
    
    # Initialize the recognizer
    r = sr.Recognizer()

    while True:
        # Listen for user input
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        
        try:
            # Use Google Speech Recognition to convert the audio to text
            user_input = r.recognize_google(audio)
            print(f"You: {user_input}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            continue

        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Smart Assistant: Goodbye!")
            break
        
        # Prepare the prompt for ChatGPT
        prompt = f"You: {user_input}\nSmart Assistant:"
        
        # Get the response from ChatGPT
        response = get_chat_response(prompt)
        
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
    main()


