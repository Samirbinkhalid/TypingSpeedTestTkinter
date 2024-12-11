import tkinter as tk
from tkinter import messagebox

# Global variables
sentence = "A quick brown fox jumps over a lazy dog"
timer_running = True


# Function to handle key presses
def on_key_press(event):
    global timer_running
    if timer_running:  # Allow input only if the timer is running
        if event.char.isalpha() or event.char == " ":  # Check if key is alphabetic or a space
            input_label.config(text=input_label.cget("text") + event.char)
        elif event.keysym == "Return":  # Check if Enter is pressed
            end_program()

# Function to handle the timer countdown
def countdown():
    global timer_running
    remaining_time = int(timer_label.cget("text"))
    if remaining_time > 0:
        timer_label.config(text=str(remaining_time - 1))
        root.after(1000, countdown)  # Call countdown again after 1 second
    else:
        timer_running = False
        end_program()

# Function to end the program and display results
def end_program():
    global timer_running
    timer_running = False

    # Get the user input
    user_input = input_label.cget("text")

    # Compare characters
    matched = sum(1 for i, char in enumerate(user_input) if i < len(sentence) and char == sentence[i])
    unmatched = len(user_input) - matched

    # Display the results in a popup
    result_message = (
        f"Matched Characters: {matched}\n"
        f"Unmatched Characters: {unmatched}"
    )
    messagebox.showinfo("Results", result_message)

    # Stop the program
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Speed Typing Test")
root.geometry("600x400")

# Sentence label
sentence_label = tk.Label(
    root,
    text=sentence,
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
