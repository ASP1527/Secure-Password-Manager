#imports
import tkinter as tk
from tkinter import *
import os
import cv2

'''
face detection
'''



'''
decrypt passwords
'''



'''
showing passwords
'''
#initialising the gui
root = tk.Tk()
root.title("Password Manager")
root.geometry('800x600') 
root.resizable(True, True)

#opening the file with the passwords in so they can be read
if os.path.isfile('encrypted.txt'):
    with open('encrypted.txt', 'r') as f:
        #splitting the file into an array
        passwords = f.read()
        passwords = f.split("\n")
    f.close()
else:
    f = open('encrypted.txt', 'w')
    f.close()


'''
add passwords
'''


root.mainloop()
'''
encrypt once closed
'''


