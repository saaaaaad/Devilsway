#!/usr/bin/env python3



# Import Module
from tkinter import *
import subprocess 


# Create Object
root = Tk()

# Add Title
root.title('DevilsWay')

# Add Geometry
root.geometry("640x480")

# Keep track of the button state on/off
#global is_on
is_on = False

# Create Label
my_label = Label(root,
	text = "DEVILSWAY",
	fg = "green",
	font = ("Helvetica", 32))

my_label.pack(pady = 20)

# Define our switch function
def switch():
	global is_on
	
	# Determin is on or off
	if is_on:
		on_button.config(image = off)
		my_label.config(text = "DEVILSWAY", fg = "grey")
		subprocess.call(["python3"," /home/astaroth/Desktop/devilsway/cache.py"])
		subprocess.call(["sudo","python3","devilsway.py","-f"])
		is_on = False
	else:		
		on_button.config(image = on)
		my_label.config(text = "DEVILSWAY", fg = "green")
		subprocess.call(["sudo","python3","devilsway.py","-l"])
		subprocess.call(["bash", "caches.sh"])
		subprocess.call(["python3","/home/astaroth/Desktop/devilsway/cache.py"])
		is_on = True

# Define Our Images
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")

# Create A Button
on_button = Button(root, image = off, bd = 0,
				command = switch)
on_button.pack(pady = 50)

# Execute Tkinter
root.mainloop()
