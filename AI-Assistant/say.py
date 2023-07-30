import os

def say(text):
    os.system(f"say {text}")

# Example usage:
response = "Hello, this is your Smart Assistant speaking!"
say(response)