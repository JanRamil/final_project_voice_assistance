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
    
    
    