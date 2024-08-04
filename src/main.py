import tkinter as tk

# Function to update the label text
def update_label():
    label.config(text="Button Clicked!")

# Create the main application window
root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("300x200")  # Set window size (width x height)

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)  # Add padding around the label

# Create a button widget
button = tk.Button(root, text="Click Me", command=update_label)
button.pack(pady=10)  # Add padding around the button

# Run the application
root.mainloop()
