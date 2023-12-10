# Morse Code Translator
# Icon found from http://icons8.com
import sys
import tkinter
from tkinter import IntVar, END
from playsound import playsound
from os import path

# Define window
root = tkinter.Tk()
root.title('Morse Code Translator')
root.iconbitmap('C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\Create10PythonGUI\\MorseCodeTranslator\\morse.ico')
root.geometry('500x350')
root.resizable(0, 0)

# Define fonts colors
font_button = ('SimSun', 10)
root_color = "#778899"
frame_color = "#dcdcdc"
button_color = "#c0c0c0"
text_color = "#f8f8ff"
root.config(bg=root_color)


# Define functions
def clear():
    """ Clear both text fields """
    input_text.delete("1.0", END)
    output_text.delete("1.0", END)


def convert():
    """Call the appropriate conversion function based off radio button values"""
    # English to morse code:
    if language.get() == 1:
        get_morse()
    elif language.get() == 2:
        get_english()


def load_assets(self):
    try:
        bundle_dir = getattr(sys, "_MEIPASS", path.abspath(path.dirname(__file__)))
        path_to_MorseCode = path.join(bundle_dir, "*.mp3")
        print(path_to_MorseCode)
        self.MorseCode_dash = 'C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\Create10PythonGUI\\MorseCodeTranslator\\dash.mp3'

        path_to_MorseCode = path.join(bundle_dir, "dot.mp3")
        self.MorseCode_dot = 'C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\Create10PythonGUI\\MorseCodeTranslator\\dot.mp3'

    except IOError as error:
        print(error)
        root.destroy()


def get_morse():
    """Convert an english message to morse code"""

    # String to hold morse code message
    morse_code = ""

    # Get the input text and standerdize it to lower case
    text = input_text.get("1.0", END)
    text = text.lower()

    # Remove any letters or symbols not in our dict keys
    for letter in text:
        if letter not in english_to_morse.keys():
            text = text.replace(letter, '')

    print(text)
    # Break up into individual words based on space " " and put into a list
    word_list = text.split(" ")

    # Turn each invididual word in word_list into a list of letters
    for word in word_list:
        letters = list(word)
        # For each letter, get the morse code representation and append it to the string morse_code
        for letter in letters:
            morse_char = english_to_morse[letter]
            morse_code += morse_char
            # Separate individual letters with a space
            morse_code += " "
        # Separate individual words with a |
        morse_code += "|"

    output_text.insert("1.0", morse_code)


def get_english():
    """Convert a morse code message to english"""
    # String to hold english message
    english = ""

    # Get the input text
    text = input_text.get("1.0", END)

    # Remove any letters or symbols not in our dict keys
    for letter in text:
        if letter not in morse_to_english.keys():
            text = text.replace(letter, '')

    # Break up each word based on | and put into a list
    word_list = text.split("|")

    # Turn each word into a list of letters
    for word in word_list:
        letters = word.split(" ")
        # For each letter, get the english representation and add it to the string english
        for letter in letters:
            english_char = morse_to_english[letter]
            english += english_char
        # Separate individual words with a space
        english += " "

    output_text.insert("1.0", english)


def play():
    """Play tones for corresoponding dots and dashes"""
    # Determine where the morse code is
    text = ""
    if language.get() == 1:
        text = output_text.get("1.0", END)
    elif language.get() == 2:
        text = input_text.get("1.0", END)

    # Play the tones(., -, " ", |)
    for value in text:
        if value == ".":
            playsound(
                'C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\Create10PythonGUI\\MorseCodeTranslator\\dot.mp3')
            root.after(100)  # pause between each dot.
        elif value == "-":
            playsound(
                'C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Tkinter\\Create10PythonGUI\\MorseCodeTranslator\\dash.mp3')
            root.after(200)
        elif value == " ":
            root.after(300)
        elif value == "|":
            root.after(700)


# Create our morse code dictionaries
english_to_morse = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
                    'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
                    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
                    'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
                    'u': '..--', 'v': '...-', 'w': '.--', 'x': '-..-',
                    'y': '-.--', 'z': '--..', '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': ' ', '|': '|', "": ""}

morse_to_english = dict([(value, key) for key, value in english_to_morse.items()])

# Define layout
# Create frames
input_frame = tkinter.LabelFrame(root, bg=frame_color)
output_frame = tkinter.LabelFrame(root, bg=frame_color)
input_frame.pack(padx=16, pady=(16, 8))
output_frame.pack(padx=16, pady=(8, 16))

# Layout for the input frame
input_text = tkinter.Text(input_frame, height=8, width=30, bg=text_color)
input_text.grid(row=0, column=1, rowspan=3, padx=5, pady=5)

language = IntVar()
language.set(1)
morse_button = tkinter.Radiobutton(input_frame, text="English --> Morse Code", variable=language, value=1,
                                   font=font_button, bg=frame_color)
english_button = tkinter.Radiobutton(input_frame, text="Morse Code --> English", variable=language, value=2,
                                     font=font_button, bg=frame_color)
guide_button = tkinter.Button(input_frame, text="Guide", font=font_button, bg=button_color)

morse_button.grid(row=0, column=0, pady=(15, 0))
english_button.grid(row=1, column=0)
guide_button.grid(row=2, column=0, sticky="WE", padx=10)

# Layout for the output frame
output_text = tkinter.Text(output_frame, height=8, width=30, bg=text_color)
output_text.grid(row=0, column=1, rowspan=4, padx=5, pady=5)

convert_button = tkinter.Button(output_frame, text="Convert", font=font_button, bg=button_color, command=convert)
play_button = tkinter.Button(output_frame, text="Play Morse", font=font_button, bg=button_color, command=play)
clear_button = tkinter.Button(output_frame, text="Clear", font=font_button, bg=button_color, command=clear)
quit_button = tkinter.Button(output_frame, text="Quit", font=font_button, bg=button_color, command=root.destroy)
convert_button.grid(row=0, column=0, padx=10, ipadx=50)  # convert ipadx defines column width
play_button.grid(row=1, column=0, padx=10, sticky="WE")
clear_button.grid(row=2, column=0, padx=10, sticky="WE")
quit_button.grid(row=3, column=0, padx=10, sticky="WE")

# Run the root window's main loop
root.mainloop()
