from flask import Flask, render_template, request, jsonify
import os
import openai
import speech_recognition as sr
from elevenlabs import generate, play
from googlesearch import search

app = Flask(__name__)

# ... (rest of the Python code)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    # Extract the user_input from the POST request
    user_input = request.json['user_input']

    # Prepare the prompt for ChatGPT
    prompt = f"You: {user_input}\nSmart Assistant:"

    # Get the response from ChatGPT
    response = get_chat_response(prompt)

    # Convert the response to speech using the ElevenLabs API
    audio = generate(
        text=response,
        voice="Antoni",
        model="eleven_monolingual_v1",
        api_key=elevenlabs_api_key
    )

    # Return the response as JSON
    return jsonify({'response': response, 'audio': audio})

if __name__ == "__main__":
    app.run(debug=True)
