import tkinter as tk
from tkinter import filedialog, messagebox,font
from urllib.parse import unquote
import os
import webbrowser
import shutil
def copy_files_based_on_prefix():
    path = file_path.get()
    if not path:
        messagebox.showerror("错误", "请选择文件夹")
        return
    try:
        os.chdir(path)
        filenamelist = [f for f in os.listdir(path) if ( f.endswith(('.psd', '.jpg', '.png'))) and before.get() in f]
        print(filenamelist)
        
        if filenamelist:
            for filename in filenamelist:
                prefix = filename.split('_', 1)[0]
                new_dir = os.path.join(path, prefix)
                if not os.path.exists(new_dir):
                    os.makedirs(new_dir)
                old_file = os.path.join(path, filename)
                new_file = os.path.join(new_dir, filename)
                print(prefix,new_dir,old_file,new_file)
                # Move the file
                shutil.move(old_file, new_file)
            messagebox.showinfo("成功", "文件分类成功")
        else:
            messagebox.showinfo("提示", "无可操作文件")
    except Exception as e:
        messagebox.showerror("错误", str(e))


def decode_filenames():
    path = file_path.get()
    if not path:
        messagebox.showerror("错误", "请选择文件夹")
        return

    try:
        os.chdir(path)
        filenamelist = [f for f in os.listdir(path) if (f.endswith('.psd') or f.endswith('.jpg') or f.endswith('.png')) and before.get() in f]
        if filenamelist:
            for name in filenamelist:
                old = name
                new = unquote(old)
                os.rename(old, new)
            messagebox.showinfo("成功", "处理乱码成功")
        else:
            messagebox.showinfo("提示", "无可操作文件")
    except Exception as e:
        messagebox.showerror("错误", str(e))

def replace_filenames():
    path = file_path.get()
    if not path:
        messagebox.showerror("错误", "请选择文件夹")
        return

    if not before.get() or not after.get():
        messagebox.showerror("错误", "请输入原文件名和替换文件名")
        return

    try:
        os.chdir(path)
        filenamelist = [f for f in os.listdir(path) if (f.endswith('.psd') or f.endswith('.jpg') or f.endswith('.png')) and before.get() in f]
        if filenamelist:
            for name in filenamelist:
                old = unquote(name)
                new = old.replace(before.get(), after.get())
                os.rename(old, new)
            messagebox.showinfo("成功", "替换成功")
        else:
            messagebox.showinfo("提示", "无可替换文件")
    except Exception as e:
        messagebox.showerror("错误", str(e))

root = tk.Tk()
root.title("Tool From [WilL]")
root.geometry("400x300")
tk.Label(root, text="先选择目录再进行操作").pack()
tk.Label(root, text="支持格式 psd png jpg").pack()

file_path = tk.StringVar()
tk.Entry(root, textvariable=file_path).pack()
browse_button = tk.Button(root, text="选择文件夹", command=lambda: file_path.set(filedialog.askdirectory()))
browse_button.pack()
decode_button = tk.Button(root, text="处理乱码", command=decode_filenames)
decode_button.pack()
classifi_button = tk.Button(root, text="文件分类", command=copy_files_based_on_prefix)
classifi_button.pack()
before = tk.StringVar()
tk.Label(root, text="原文件名:").pack()
tk.Entry(root, textvariable=before).pack()

after = tk.StringVar()
tk.Label(root, text="替换文件名:").pack()
tk.Entry(root, textvariable=after).pack()


replace_button = tk.Button(root, text="替换", command=replace_filenames)
replace_button.pack()
# tk.Label(root, text="present by github.com/Wiiiiill").pack()
link=tk.Label(root,text="present by github.com/Wiiiiill")
link.pack()
def open_url(event):
    webbrowser.open("https://wiiiiill.github.io/",new=0)
    
link.bind("<Button-1>",open_url)

root.mainloop()