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
    
    
    