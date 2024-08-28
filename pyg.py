from dearpygui.core import *
from dearpygui.simple import *
from urllib.parse import unquote
import os

# 定义文件过滤函数
def filter_files(files, before, after):
    return [f for f in files if (before in f and (f.endswith('.psd') or f.endswith('.jpg') or f.endswith('.png')))]

# 替换文件名的函数
def replace_filenames(sender, data):
    path = get_value("##path")
    before = get_value("##before")
    after = get_value("##after")
    files = os.listdir(path)
    filenamelist = filter_files(files, before, after)
    
    if filenamelist:
        for name in filenamelist:
            old = name
            new = unquote(old).replace(before, after)
            os.rename(os.path.join(path, old), os.path.join(path, new))
        print("替换成功")
        show_popup("替换成功", "文件名替换完成")
    else:
        show_popup("无可替换文件", "没有找到匹配的文件")

# 创建窗口
with window("文件名替换程序"):
    with child("##main"):  # 创建一个内部子窗口
        with group("##group1", horizontal=True):  # 创建一个水平分组
            add_text("选择目录然后输入文件名进行替换")
            add_text("支持格式 psd png jpg")
        
        with group("##group2", horizontal=True):
            add_input_text("##path", default_value="")
            add_button("选择文件夹", callback=lambda: select_directory("##path"))
        
        with group("##group3", horizontal=True):
            add_text("原文件名:")
            add_input_text("##before", default_value="")
        
        with group("##group4", horizontal=True):
            add_text("替换文件名:")
            add_input_text("##after", default_value="")
        
        add_button("替换", callback=replace_filenames)

start_dearpygui()