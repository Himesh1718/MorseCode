from tkinter import *
import json


GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

with open("morseCode.json") as f:
    data = json.load(f)


def convert():
    text = list(inputText.get("1.0", "end-1c"))
    lis = []
    for char in text:
        mc = data[char.lower()]
        lis.append(mc)
    string = ""
    for word in lis:
        string = string+"  "+word

    outputLabel.config(text=string)


def reset():
    inputText.delete("1.0", "end")
    outputLabel.config(text="")


root = Tk()
root.title("Morse Code Converter")
root.geometry("700x500")
root.minsize(700, 500)
# root.maxsize(700, 500)
root.config(padx=100, pady=50, bg=YELLOW,)


titleLabel = Label(text="Morse Code Converter", font=(
    "Courier", 30, 'bold'), fg=GREEN, bg=YELLOW)
titleLabel.grid(row=0, column=0, columnspan=5)

inputLabel = Label(text="Enter text", font=(
    "Courier", 15, 'bold'), fg="#07060a", bg=YELLOW)
inputLabel.grid(row=1, column=0, columnspan=5)

inputText = Text(root, height=5, width=50, font=(
    "Courier", 13, 'bold'), fg="#d307f2")
inputText.grid(row=2, column=0, padx=5, pady=15, columnspan=5)

resetButton = Button(text="Reset", font=(
    "Courier", 13, "bold"), fg="#e8666f", command=reset)
resetButton.grid(row=3, column=0)

convertButton = Button(text="Convert", font=(
    "Courier", 13, "bold"), fg="#e8666f", command=convert)
convertButton.grid(row=3, column=1)
convertButton.bind("<enter>")

outputLabel = Label(font=(
    "Courier", 15, 'bold'), fg="black", bg=YELLOW, height=5, width=40)
outputLabel.grid(row=4, column=0, pady=10, columnspan=5)


root.mainloop()
