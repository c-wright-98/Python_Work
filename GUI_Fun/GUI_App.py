'''
Create a simple file reader which displays file contents in a gui window using TKinter
'''
import tkinter as tk

def read_file():
    with open(input.get(), 'r') as file:
        for i,j in enumerate(file):
            tk.Label(root, text = f'{i}:{j}').grid(row = i+4, column = 1)

root = tk.Tk()

label = tk.Label (root, text = "Enter your file Path")
label.grid(row = 1, column = 1)
input = tk.Entry(root)
input.grid(row = 2, column = 1)
submit = tk.Button(root, text = "Submit" , command = read_file)
submit.grid(row = 3, column = 1)


if __name__ == '__main__':
    root.mainloop()
