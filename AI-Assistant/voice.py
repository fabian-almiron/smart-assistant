import os

from elevenlabs import generate, play
from elevenlabs import voices, generate



# Load ElevenLabs API key from environment variable
elevenlabs_api_key = os.getenv('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')

audio = generate(
  text="Hi! My name is Bella, nice to meet you!",
  voice="Bella",
  model="eleven_monolingual_v1",
  api_key=elevenlabs_api_key
)

play(audio)

# Get a list of available voices
available_voices = voices()

# Print the list of available voices
print(available_voices)

# Select a specific voice
selected_voice = available_voices[0]

# Generate audio using the selected voice
audio = generate(text="Hello there!", voice=selected_voice)


