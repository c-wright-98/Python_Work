import tkinter as tk

def strip_vowels(string):
    global label
    string = input1.get()
    label.destroy()
    label = tk.Label(root, text = ''.join(char for char in string if char not in 'aeiouAEIOU'))
    label.grid (row = 2, column =1)

#This initialises tkinter and lets us pass pur visuals onto something
root = tk.Tk()

label = tk.Label(root,text = "Hello World!")
input1 = tk.Entry(root)
label.grid(row = 1,column = 1)
input1.grid(row = 2, column = 1)

#create button to submit the input string

button = tk.Button(root, text = "Strip vowels", command = strip_vowels)
button.grid(row = 3, column = 1)

#This object has a main loop object that allows us to interact with it
# It's good practice to run this in the __main__ so it runs when the file is ran

if __name__ == '__main__':
    root.mainloop()