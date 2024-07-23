import subprocess

def speak(text):
    subprocess.run(["espeak-ng", text])

if __name__ == '__main__':
    print("Welcome to Robo Speaker")
    while True:
        x = input("Enter the text you want to speak (or 'exit' to quit): ")
        if x.lower() == "exit":
            print("Exiting Robo Speaker")
            break
        speak(x)