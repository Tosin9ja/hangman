import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
word_list = ['success', 'excel', 'wonderful', 'excellent', 'awesome']


def pick_word():
    """Pick a random word from the word list"""
    return random.choice(word_list)

def update_word(word, guesses):
    """Update the word to show correctly guessed letters"""
    updated_word = ''
    for char in word:
        if char in guesses:
            updated_word += char + ' '
        else:
            updated_word += '_ '
    return updated_word.strip()

def guess_letter():
    """Process the guessed letter"""
    letter = letter_entry.get().lower()
    if len(letter) != 1 or not letter.isalpha():
        messagebox.showerror('Invalid Input', 'Please enter a single letter.')
        return
    
    if letter in guesses:
        messagebox.showinfo('Duplicate Guess', 'You have already guessed that letter.')
    elif letter in word:
        guesses.append(letter)
        guessed_word = update_word(word, guesses)
        word_label.config(text=guessed_word)
        if guessed_word.replace(' ', '') == word:
            messagebox.showinfo('Congratulations', 'You won the game!')
            reset_game()
    else:
        guesses.append(letter)
        attempts_left = max_attempts - len(guesses)
        attempts_label.config(text=f'Attempts Left: {attempts_left}')
        if attempts_left == 0:
            messagebox.showinfo('Game Over', f'You lost the game. The word was: {word}')
            reset_game()

def reset_game():
    """Reset the game state"""
    global word, guesses
    word = pick_word()
    guesses = []
    word_label.config(text='_ ' * len(word))
    attempts_label.config(text=f'Attempts Left: {max_attempts}')

# Initialize the game
max_attempts = 6
word = pick_word()
guesses = []

# Create the main window
window = tk.Tk()
window.title('Hangman_Oluwatosin')

# Create the word label
word_label = tk.Label(window, text='_ ' * len(word), font=('Arial', 18))
word_label.pack(pady=10)

# Create the letter entry
letter_entry = tk.Entry(window, font=('Arial', 14))
letter_entry.pack(pady=10)

# Create the guess button
guess_button = tk.Button(window, text='Guess', command=guess_letter, font=('Arial', 14))
guess_button.pack(pady=10)

def clear_screen():
    letter_entry.delete(0, tk.END)

# Create the "Clear" button
clear_button = tk.Button(window, text='Clear', font=('Arial', 14), command=clear_screen)
clear_button.pack(pady=20)

# Create the restart button
guess_button = tk.Button(window, text='Restart', command=reset_game, font=('Arial', 14))
guess_button.pack(pady=10)

# Create the attempts label
attempts_label = tk.Label(window, text=f'Attempts Left: {max_attempts}', font=('Arial', 14))
attempts_label.pack(pady=10)

def button_click(letter):
    letter_entry.insert(tk.END, letter)

def validate_entry():
    current_entry = letter_entry.get().strip()
    if len(current_entry) == 1 and current_entry.isalpha():
        # Process the guess with the current entry
        guess_letter(current_entry.upper())
        clear_screen()
    else:
        # Display an error message for invalid input
        messagebox.showerror('Invalid Input', 'Please enter a single letter.')


# Create the letter buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

# # Function to handle button click event
# def button_click(letter):
#     letter_entry.insert(tk.END, letter)

# Create letter buttons A-Z
for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    letter_button = tk.Button(button_frame, text=letter, font=('Arial', 14),
                              command=lambda l=letter: button_click(l))
    letter_button.pack(side=tk.LEFT, padx=5)




# Run the main window loop
window.mainloop()




# Start the game
if __name__=="__main__":
    reset_game()


# Run the main window loop
window.mainloop()


# Create the word label
word_label = tk.Label(window, text='_ ' * len(word), font=('Arial', 18))
word_label.pack(pady=10)

