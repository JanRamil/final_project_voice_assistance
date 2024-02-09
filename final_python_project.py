# Final Project
# Create a program that will generate a strong password

import tkinter as tk
import random
import string

# Create a function
def generate_password(min_length_entry, number_var, special_var, result_label):
    min_length = int(min_length_entry.get())
    has_number = number_var.get()
    has_special = special_var.get()
    # For letters, digits, and special
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if has_number: 
        characters += digits
    if has_special: 
        characters += special
        
    pwd = "" 
    meets_criteria = False
    has_number = False
    has_special = False
    
    
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
            
        meets_criteria = True 
        if has_number: 
            meets_criteria = has_number
        if has_special:
            meets_criteria = meets_criteria and has_special

    result_label.config(text="Generated Password: " + pwd)
    
def submit_details():
    first_name = first_name_entry.get()
    middle_initials = middle_initials_entry.get()
    last_name = last_name_entry.get()
    
    user_window = tk.Toplevel()
    user_window.title("User Account")
    
    # Customize window style
    user_window.configure(bg="#f0f0f0")
    
    # Creating widgets
    min_length_label = tk.Label(user_window, text="Minimum Length:", bg="#f0f0f0")
    min_length_label.pack(pady=(10, 2))
    min_length_entry = tk.Entry(user_window)
    min_length_entry.pack(pady=2)
    number_var = tk.BooleanVar()
    number_check = tk.Checkbutton(user_window, text="Include Numbers", variable=number_var, bg="#f0f0f0")
    number_check.pack()
    
    special_var = tk.BooleanVar()
    special_check = tk.Checkbutton(user_window, text="Include Special Characters", variable=special_var, bg="#f0f0f0")
    special_check.pack()

    result_label = tk.Label(user_window, text="", bg="#f0f0f0", font=("Helvetica", 12))
    result_label.pack(pady=(10, 2))

    generate_button = tk.Button(user_window, text="Generate Password", command=lambda: generate_password(min_length_entry, number_var, special_var, result_label), bg="#4caf50", fg="white", font=("Helvetica", 12), relief=tk.FLAT)
    generate_button.pack(pady=(2, 10))

def done_button():
    window.destroy()

# Creating the tkinter window
window = tk.Tk()
window.title("User Information")

# Customize window style
window.configure(bg="#f0f0f0")

# Creating widgets
first_name_label = tk.Label(window, text="First Name:", bg="#f0f0f0", font=("Helvetica", 12))
first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
first_name_entry = tk.Entry(window, font=("Helvetica", 12))
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

middle_initials_label = tk.Label(window, text="Middle Initials:", bg="#f0f0f0", font=("Helvetica", 12))
middle_initials_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
middle_initials_entry = tk.Entry(window, font=("Helvetica", 12))
middle_initials_entry.grid(row=1, column=1, padx=10, pady=5)

last_name_label = tk.Label(window, text="Last Name:", bg="#f0f0f0", font=("Helvetica", 12))
last_name_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
last_name_entry = tk.Entry(window, font=("Helvetica", 12))
last_name_entry.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(window, text="Submit", command=submit_details, bg="#4caf50", fg="white", font=("Helvetica", 12), relief=tk.FLAT)
submit_button.grid(row=4, columnspan=2, padx=10, pady=10)

done_button = tk.Button(window, text="Done", command=done_button, bg="#e91e63", fg="white", font=("Helvetica", 12), relief=tk.FLAT)
done_button.grid(row=5, columnspan=2, padx=10, pady=10)

# Running the tkinter event loop
window.mainloop()