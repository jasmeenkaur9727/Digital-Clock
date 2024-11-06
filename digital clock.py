import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')  # Get the current time
    label.config(text=current_time)  # Update the label with the current time
    label.after(1000, update_time)  # Call this function again after 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create a label to display the time
label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()  # Call the function to update the time
root.mainloop()  # Run the application
