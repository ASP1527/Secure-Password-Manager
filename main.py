#imports
import tkinter as tk
from tkinter import *
import os
import face__capturing
import face__training
import face__auth

ecode = 1
authenticated = False

'''
checking if there is already a face saved and if the authentication is successful
'''

if os.path.isfile('captured.txt'):
    face__auth.authenticate()
    if os.path.isfile('authenticated.txt'):
        authenticated = True
    else:
        authenticated = False
else:
    face__capturing.capture()
    face__training.train()
    face__auth.authenticate()
    authenticated = True

'''
showing passwords using tkinter
'''
#initialising the gui if the user is authenticated
if authenticated == True:
    root = tk.Tk()
    root.title("Password Manager")
    root.geometry('1000x1000') 
    root.resizable(True, True) #allowing the window to be resizable

    frame = tk.Frame(root, bg="#C0C0C0")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.19) #creating a frame to add some contrast

    #opening the file with the passwords in so they can be read
    if os.path.isfile('encrypted.txt'):
        with open('encrypted.txt', 'r') as f:
            #splitting the file into an array
            passwords = f.read() #passwords are put in an array
            passwords = passwords.split("\n") #split at every new line
            for i in range(len(passwords)): #removes passwords that are empty
                encrypted = ""
                for c in passwords[i]: #decrypts each character in each password
                    order = ord(c)
                    encrypts = chr(order-ecode)
                    encrypted = encrypted + encrypts
                passwords[i] = encrypted #changes the location of the password to be the decrypted version
                label = tk.Label(frame, text=passwords[i], bg="#C0C0C0")
                label.pack() #show each of the passwords as a label
    else:
        f = open('encrypted.txt', 'w') #creates the file for the passwords if there is no file for them already
        f.close()


    '''
    add passwords
    '''
    #variables, etc

    #functions
    def getEntryAdd():
        item = e.get() #gets the entry from the input box
        e.delete(0, 'end') #clears the input box
        if item != "": #only adds passwords if e is not empty
            passwords.append(item) #adds it to passwords
            print(passwords)
            x = len(passwords)
            for widget in frame.winfo_children(): #for each label in the frame:
                widget.destroy() #remove them
            for i in range(x):
                if passwords[i] == '': #removes empty passwords
                    passwords.pop(i)
                    x -= 1 #to avoid any index out of range errors
            for i in range(len(passwords)): 
                label = tk.Label(frame, text=passwords[i], bg="#C0C0C0")
                label.pack() #show every password in the frame

    def getEntryUpdate(): #almost identical to the one above
        item = eu.get()
        eu.delete(0, 'end')
        if item != "":
            item = item.split(",")
            passwords[int(item[0])-1] = item[1] #sets the password at the location number to the new password from the entry
            print(passwords)
            x = len(passwords)
            for widget in frame.winfo_children():
                widget.destroy()
            for i in range(x):
                if passwords[i] == '':
                    passwords.pop(i)
                    x -= 1
            for i in range(len(passwords)):
                label = tk.Label(frame, text=passwords[i], bg="#C0C0C0")
                label.pack()

    #label/user prompt
    prompt1 = tk.Label(root, text="Writing the application that the password is for is recommended. Passwords will be encrypted when the application is closed", pady=5)
    prompt1.pack() #shows the above text

    #input field
    e = tk.Entry(root, width=50, bd=1)
    e.pack() #shows the input field

    #add button
    add = tk.Button(root, text="Add Password", command=getEntryAdd, border=0, bg="#87ceeb", pady=5)
    add.pack() #shows the button

    #label/user prompt
    prompt = tk.Label(root, text="Update passwords with the number (indicating which line) separated with a ',' and application and password", pady=5)
    prompt.pack() #shows the above text

    #input field
    eu = tk.Entry(root, width=50, bd=1)
    eu.pack() #shows the input field

    #update button
    update = tk.Button(root, text="Update Password", command=getEntryUpdate, border=0, bg="#87ceeb", pady=5)
    update.pack() #shows the button

    root.mainloop() #runs the main loop of the gui
    '''
    encrypt once closed
    '''

    with open('encrypted.txt', 'w') as f: #opens the file
        y = 1
        for item in passwords: #for each password:
            if y != 1:
                f.write('\n') #if it's not the first password, add a new line
            y += 1
            for characters in item: #encrypt each character and write it
                order = ord(characters)
                encrypted = chr(order+ecode)
                f.write(encrypted)

if os.path.isfile('authenticated.txt'): #remove the authenticated file so you have to be authenticated to open the file again
    os.remove('authenticated.txt')
