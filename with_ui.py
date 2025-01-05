import tkinter as tk
from tkinter import messagebox

# Function to convert Decimal to Binary
def dec_to_bin(n):
    s = ""  
    original_n = n  
    
    while n > 0:
        r = n % 2
        s = str(r) + s
        n = n // 2
    
    return s

# Function to convert Binary to Decimal
def bin_to_dec(n2):
    dec_n = 0
    m = 1
    n2 = int(n2)  
    
    while n2 > 0:
        reminder = n2 % 10
        dec_n = dec_n + (reminder * m)
        m = m * 2
        n2 = n2 // 10
    
    return dec_n

# Function that handles button click
def convert():
    choice = choice_var.get()
    if choice == 1:
        try:
            num = int(entry.get())
            result = dec_to_bin(num)
            result_label.config(text=f"Binary Value: {result}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid decimal number.")
    
    elif choice == 2:
        num = entry.get()
        if all(digit in "01" for digit in num):  # Check if input is a valid binary number
            result = bin_to_dec(num)
            result_label.config(text=f"Decimal Value: {result}")
        else:
            messagebox.showerror("Input Error", "Please enter a valid binary number.")
    
    else:
        messagebox.showerror("Invalid Choice", "Please select a valid option.")

# Create the main window
root = tk.Tk()
root.title("Decimal-Binary Converter")

# Create the main frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create radio buttons for conversion choice (Decimal to Binary or Binary to Decimal)
choice_var = tk.IntVar()
choice_var.set(1)  # Default is Decimal to Binary

radio1 = tk.Radiobutton(frame, text="Decimal to Binary", variable=choice_var, value=1)
radio1.grid(row=0, column=0, sticky="w")

radio2 = tk.Radiobutton(frame, text="Binary to Decimal", variable=choice_var, value=2)
radio2.grid(row=1, column=0, sticky="w")

# Entry field to input the number
entry_label = tk.Label(frame, text="Enter Number:")
entry_label.grid(row=2, column=0, pady=5, sticky="w")

entry = tk.Entry(frame, width=20)
entry.grid(row=2, column=1, pady=5)

# Convert Button
convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to show the result
result_label = tk.Label(frame, text="Result will be shown here.", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
