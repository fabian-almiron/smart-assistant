import openai

# Your OpenAI API key, replace 'YOUR_API_KEY' with your actual API key
openai.api_key = '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'

def get_chat_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the engine you have access to
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    print("Welcome to the Smart Assistant!")
    print("You can start by asking me anything or giving me a command.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Smart Assistant: Goodbye!")
            break
        
        # Prepare the prompt for ChatGPT
        prompt = f"You: {user_input}\nSmart Assistant:"
        
        # Get the response from ChatGPT
        response = get_chat_response(prompt)
        
        print(f"Smart Assistant: {response}")

if __name__ == "__main__":
    main()
