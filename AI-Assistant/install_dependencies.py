import subprocess

def install(package):
    subprocess.check_call(['pip3', 'install', package])

def main():
    dependencies = [
        'openai',
        'SpeechRecognition',
        'elevenlabs',
        'google',
    ]

    for dependency in dependencies:
        try:
            install(dependency)
            print(f"Successfully installed {dependency}.")
        except Exception as e:
            print(f"Error installing {dependency}: {e}")

if __name__ == "__main__":
    main()


# export OPENAI_API_KEY=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 
# export ELEVENLABS_API_KEY=2f84b0d55502bb8064f07e67ee9f3af6