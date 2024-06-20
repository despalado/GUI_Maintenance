from tkinter import *

# Create the main window
GUI = Tk()
GUI.title('Customer Service Management System')

# Set the size of the window
window_width = 800
window_height = 600

# Get the screen width and height
screen_width = GUI.winfo_screenwidth()
screen_height = GUI.winfo_screenheight()

# Calculate the position to center the window
position_x = int(screen_width/2 - window_width/2)
position_y = int(screen_height/2 - window_height/2)

# Set the geometry of the window
GUI.geometry(f'{window_width}x{window_height}+{position_x}+{position_y}')

# Run the main loop
GUI.mainloop()