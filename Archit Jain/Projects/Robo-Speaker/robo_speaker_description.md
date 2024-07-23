# Robo Speaker

## Project Overview

Robo Speaker is a simple Python script that uses text-to-speech technology to convert user input into spoken words.

This project is designed to work on Garuda Linux (an Arch-based distribution) using the `espeak-ng` text-to-speech engine.

## Prerequisites

- Python 3
- espeak-ng (text-to-speech engine)

## Installation

1. Ensure you have Python 3.x installed on your system.

2. Install espeak-ng:
   ```
   sudo pacman -S espeak-ng
   ```

3. Clone this repository or download the `robo_speaker.py` file.

## How to Run

1. Open a terminal in the directory containing `robo_speaker.py`.

2. Run the script using Python:
   ```
   python robo_speaker.py
   ```

3. Enter the text you want the computer to speak.

4. To exit the program, type 'exit' when prompted for input.

## Code Explanation

```python
import subprocess
```
This line imports the `subprocess` module, which we use to run external commands (in this case, espeak-ng).

```python
def speak(text):
    subprocess.run(["espeak-ng", text])
```
This defines a function called `speak` that takes a `text` parameter. It uses `subprocess.run()` to execute the espeak-ng command with the given text.

```python
if __name__ == '__main__':
```
This is a common Python idiom. It checks if the script is being run directly (as opposed to being imported as a module). The code below this line only executes if the script is run directly.

```python
    print("Welcome to Robo Speaker")
```
This prints a welcome message to the console.

```python
    while True:
```
This starts an infinite loop, allowing the user to enter multiple phrases until they choose to exit.

```python
        x = input("Enter the text you want to speak (or 'exit' to quit): ")
```
This prompts the user to enter text and stores the input in the variable `x`.

```python
        if x.lower() == "exit":
            print("Exiting Robo Speaker")
            break
```
This checks if the user wants to exit. If the input (converted to lowercase) is 'exit', it prints a message and breaks out of the loop.

```python
        speak(x)
```
If the user didn't choose to exit, this line calls the `speak()` function with the user's input, causing the computer to speak the text.

## The subprocess Module

The `subprocess` module in Python provides a way to spawn new processes. It's used to run external commands and interact with the operating system.

In our script, we use `subprocess.run()`, which is a convenient method for running a command and waiting for it to complete. The basic syntax is:

```python
subprocess.run(args, ...)
```

Where `args` is a list or tuple of program arguments. The first item should be the program to execute.

In our case, `subprocess.run(["espeak-ng", text])` runs the espeak-ng command with the given text as an argument.

## Conclusion

This Robo Speaker project demonstrates a simple use of text-to-speech technology in Python. It showcases basic input/output operations, loop structures, and how to interact with system commands using the `subprocess` module.

---