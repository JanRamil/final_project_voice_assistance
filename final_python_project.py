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