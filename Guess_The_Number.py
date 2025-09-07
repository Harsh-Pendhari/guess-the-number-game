import tkinter as tk

from tkinter import font 

root = tk.Tk()
root.title("Guess The Number")
root.iconbitmap(r'icon.ico')
root.geometry("400x550")
root.resizable(False, False)

def start_the_game():
    print("working") # To Be Constructed

GuessTheNum = tk.Button(root, text="Guess The Number", font = ("Arial", 20, "bold"), bg = "green", fg="white", cursor="hand2", command=start_the_game)
GuessTheNum.pack()

tk.mainloop()
