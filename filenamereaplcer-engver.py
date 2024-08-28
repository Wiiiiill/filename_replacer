import tkinter as tk
from tkinter import filedialog, messagebox,font
from urllib.parse import unquote
import os
import webbrowser

def decode_filenames():
    path = file_path.get()
    if not path:
        messagebox.showerror("Error", "chose folder first")
        return

    try:
        os.chdir(path)
        filenamelist = [f for f in os.listdir(path) if (f.endswith('.psd') or f.endswith('.jpg') or f.endswith('.png')) and before.get() in f]
        if filenamelist:
            for name in filenamelist:
                old = name
                new = unquote(old)
                os.rename(old, new)
            messagebox.showinfo("Success", "Filename decoded")
        else:
            messagebox.showinfo("Tips", "no file to decode")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def replace_filenames():
    path = file_path.get()
    if not path:
        messagebox.showerror("Error", "chose folder first")
        return

    if not before.get() or not after.get():
        messagebox.showerror("Error", "Pls Enter Orig-filename and New-filename")
        return

    try:
        os.chdir(path)
        filenamelist = [f for f in os.listdir(path) if (f.endswith('.psd') or f.endswith('.jpg') or f.endswith('.png')) and before.get() in f]
        if filenamelist:
            for name in filenamelist:
                old = unquote(name)
                new = old.replace(before.get(), after.get())
                os.rename(old, new)
            messagebox.showinfo("Success", "filename replaced")
        else:
            messagebox.showinfo("tips", "no file to replaced")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Filename-Replacer")
root.geometry("400x300")
tk.Label(root, text="Chose a Folder and enter filename to replace").pack()
tk.Label(root, text="Supported Formats: psd png jpg").pack()

file_path = tk.StringVar()
tk.Entry(root, textvariable=file_path).pack()
browse_button = tk.Button(root, text="Chose a Folder", command=lambda: file_path.set(filedialog.askdirectory()))
browse_button.pack()
decode_button = tk.Button(root, text="Filename Decode", command=decode_filenames)
decode_button.pack()
before = tk.StringVar()
tk.Label(root, text="Orig Filename:").pack()
tk.Entry(root, textvariable=before).pack()

after = tk.StringVar()
tk.Label(root, text="New Filename:").pack()
tk.Entry(root, textvariable=after).pack()


replace_button = tk.Button(root, text="Replace", command=replace_filenames)
replace_button.pack()
# tk.Label(root, text="present by github.com/Wiiiiill").pack()
link=tk.Label(root,text="present by github.com/Wiiiiill")
link.pack()
def open_url(event):
    webbrowser.open("https://wiiiiill.github.io/",new=0)
    
link.bind("<Button-1>",open_url)

root.mainloop()
