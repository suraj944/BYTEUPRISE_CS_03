import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    """
    Function to perform Caesar Cipher encryption or decryption.

    Args:
    - text (str): The text to be encrypted or decrypted.
    - shift (int): The shift value for the cipher.
    - mode (str): 'encrypt' for encryption (default), 'decrypt' for decryption.

    Returns:
    - str: The processed text after encryption or decryption.
    """
    result = []
    shift = shift % 26  # Ensure shift is within the range of 0-25

    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            offset = ord(char) - base
            if mode == 'encrypt':
                new_offset = (offset + shift) % 26
            elif mode == 'decrypt':
                new_offset = (offset - shift) % 26
            new_char = chr(base + new_offset)
            result.append(new_char)
        else:
            result.append(char)  # Append non-alphabetic characters unchanged

    return ''.join(result)

def handle_process():
    text = text_entry.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    mode = mode_var.get()

    if mode == 'Encrypt':
        processed_text = caesar_cipher(text, shift, 'encrypt')
    elif mode == 'Decrypt':
        processed_text = caesar_cipher(text, shift, 'decrypt')

    result_text.delete("1.0", "end")
    result_text.insert("1.0", processed_text)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")

# Create widgets
text_label = tk.Label(root, text="Enter text:")
text_label.pack()
text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

shift_label = tk.Label(root, text="Enter shift value:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

mode_var = tk.StringVar()
mode_var.set("Encrypt")  # Default mode

encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="Encrypt")
encrypt_radio.pack()
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="Decrypt")
decrypt_radio.pack()

process_button = tk.Button(root, text="Encrypt/Decrypt", command=handle_process)
process_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()
result_text = tk.Text(root, height=5, width=50)
result_text.pack()

# Start the main loop
root.mainloop()
