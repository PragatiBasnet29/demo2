import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)  # ❌ label is used before it's created
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Customize window size and background
root.geometry("250x100")
root.configure(bg="black")

# Start updating time (this will call update_time before label exists)
update_time()

# Create and configure the label
label = tk.Label(root, font=('Arial', 40, 'bold'), bg='black', fg='cyan')
label.pack(anchor='center')

# Start the GUI loop
root.mainloop()
