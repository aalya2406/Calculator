import tkinter as tk
from tkinter import messagebox
import math

def button_click(value):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(0, current_text + value)

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display.delete(0, tk.END)

def button_sqrt():
    try:
        result = math.sqrt(float(display.get()))
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display.delete(0, tk.END)

def button_square():
    try:
        result = math.pow(float(display.get()), 2)
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")
        display.delete(0, tk.END)

def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

def draw(event):
    global last_x, last_y
    x, y = event.x, event.y
    canvas.create_line((last_x, last_y, x, y), fill='black', width=2)
    last_x, last_y = x, y

def clear_canvas():
    canvas.delete('all')

root = tk.Tk()
root.title(" Calculator With A Notepad")
root.geometry("800x600")
root.configure(bg="lightgray")

display_frame = tk.Frame(root, bg="black")
display_frame.pack(pady=20)

display = tk.Entry(display_frame, font=("Arial", 24), borderwidth=0, bg="black", fg="white", justify='left')
display.pack(ipadx=8, ipady=8)

button_frame = tk.Frame(root, bg="lightgray")
button_frame.pack(side=tk.LEFT, padx=10)

button_params = {
    "font": ("Arial", 18),
    "bg": "#333",
    "fg": "black",
    "bd": 0,
    "activebackground": "#666",
    "activeforeground": "white",
    "relief": "flat",
    "highlightthickness": 0,
    "height": 2,
    "width": 4
}

special_button_params = {
    "font": ("Arial", 18),
    "bg": "#FF9500",
    "fg": "black",
    "bd": 0,
    "activebackground": "#FFB84D",
    "activeforeground": "black",
    "relief": "flat",
    "highlightthickness": 0,
    "height": 2,
    "width": 4
}

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        action = button_equal
        params = special_button_params
    else:
        action = lambda x=button: button_click(x)
        params = button_params

    tk.Button(button_frame, text=button, command=action, **params).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(button_frame, text="C", command=button_clear, **special_button_params).grid(row=0, column=0, columnspan=4, pady=5, sticky='we')
tk.Button(button_frame, text="√", command=button_sqrt, **button_params).grid(row=5, column=0, padx=5, pady=5)
tk.Button(button_frame, text="x²", command=button_square, **button_params).grid(row=5, column=1, padx=5, pady=5)

notepad_frame = tk.Frame(root, bg="lightgray")
notepad_frame.pack(side=tk.RIGHT, padx=10, pady=20)

tk.Label(notepad_frame, text="Notepad", font=("Arial", 18), bg="lightgray").pack(pady=10)

canvas = tk.Canvas(notepad_frame, width=300, height=400, bg="white")
canvas.pack()

canvas.bind("<Button-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

tk.Button(notepad_frame, text="Clear Notepad", command=clear_canvas, font=("Arial", 14), bg="#FF9500", fg="white", bd=0, activebackground="#FFB84D", activeforeground="white", relief="flat", highlightthickness=0, height=2).pack(pady=20)

root.mainloop()
