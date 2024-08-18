import tkinter as tk
import random

# Define the choices and the game logic
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
game_logic = {
    "Rock": "Scissors",
    "Scissors": "Paper",
    "Paper": "Rock"
}

user_score = 0
computer_score = 0

def generate_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    elif game_logic[user_choice] == computer_choice:
        user_score += 1
        return "You win! 🎉"
    else:
        computer_score += 1
        return "You lose! 😢"

def play_round(user_choice):
    computer_choice = generate_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"User: {emojis[user_choice]} | Computer: {emojis[computer_choice]}\n{result}")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

def play_again():
    result_label.config(text="")
    score_label.config(text=f"User Score: {user_score} | Computer Score: {computer_score}")

def create_gradient(canvas, color1, color2):
    width = 400
    height = 300
    for i in range(height):
        ratio = i / height
        red = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        green = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        blue = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        color = f"#{red:02x}{green:02x}{blue:02x}"
        canvas.create_line(0, i, width, i, fill=color)

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("400x300")

# Create a canvas for gradient background
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)
create_gradient(canvas, (240, 240, 240), (150, 150, 255))

# Create a frame to hold widgets with a transparent background
frame = tk.Frame(root, bg="#f0f0f0")
frame.place(relwidth=1, relheight=1)

# Create and place the widgets
title_label = tk.Label(frame, text="Rock-Paper-Scissors", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

instruction_label = tk.Label(frame, text="Choose your move:", font=("Helvetica", 12), bg="#f0f0f0")
instruction_label.pack(pady=5)

# Create buttons for user choices
button_frame = tk.Frame(frame, bg="#f0f0f0")
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="🪨 Rock", font=("Helvetica", 12), command=lambda: play_round("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="📄 Paper", font=("Helvetica", 12), command=lambda: play_round("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="✂️ Scissors", font=("Helvetica", 12), command=lambda: play_round("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(frame, text="", font=("Helvetica", 12), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(frame, text=f"User Score: {user_score} | Computer Score: {computer_score}", font=("Helvetica", 12), bg="#f0f0f0")
score_label.pack(pady=10)

play_again_button = tk.Button(frame, text="Play Again", font=("Helvetica", 12), command=play_again)
play_again_button.pack(pady=10)

# Run the application
root.mainloop()
