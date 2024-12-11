import tkinter as tk
from tkinter import messagebox

# Function to handle key presses
def on_key_press(event):
    if timer_running:  # Allow input only if the timer is running
        if event.char.isalpha() or event.char == " ":  # Check if key is alphabetic or a space
            input_label.config(text=input_label.cget("text") + event.char)

# Function to handle the timer countdown
def countdown():
    global timer_running
    remaining_time = int(timer_label.cget("text"))
    if remaining_time > 0:
        timer_label.config(text=str(remaining_time - 1))
        root.after(1000, countdown)  # Call countdown again after 1 second
    else:
        timer_running = False
        messagebox.showinfo("Time's Up!", "We Are Done")  # Show the popup

# Create the main window
root = tk.Tk()
root.title("Speed Typing Test")
root.geometry("600x400")

# Global variable to track if the timer is running
timer_running = True

# Sentence label
sentence_label = tk.Label(
    root,
    text="A quick brown fox jumps over a lazy dog",
    font=("Arial", 18),
    wraplength=500,
    justify="center"
)
sentence_label.pack(pady=20)

# Label to display user input
input_label = tk.Label(
    root,
    text="",
    font=("Arial", 16),
    fg="blue"  # Make it visually distinct
)
input_label.pack(pady=10)

# Timer label
timer_label = tk.Label(
    root,
    text="60",  # Starting value for the timer
    font=("Arial", 16),
    fg="red"  # Red text for visibility
)
timer_label.pack(pady=10)

# Bind key press event
root.bind("<KeyPress>", on_key_press)

# Start the timer
root.after(1000, countdown)

# Start the Tkinter event loop
root.mainloop()
