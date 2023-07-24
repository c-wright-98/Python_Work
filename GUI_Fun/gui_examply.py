import tkinter as tk

#This initialises tkinter and lets us pass pur visuals onto something
root = tk.Tk()

label = tk.Label(root,text = "Hello World!")
label.grid(row = 1,column = 1)

#This object has a main loop object that allows us to interact with it
# It's good practice to run this in the __main__ so it runs when the file is ran

if __name__ == '__main__':
    root.mainloop()