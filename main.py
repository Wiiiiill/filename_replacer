import PySimpleGUI as sg
import os
#sg.theme('DarkAmber')    # Keep things interesting for your users
layout = [[sg.Text('选择目录然后输入文件名进行替换')],[sg.Text('支持格式 psd png jpg')],
          [sg.FolderBrowse("选择文件夹",target="input")],
          [sg.In(key="input")],
          [sg.Text("原文件名:")],
          [sg.Input(key='-before-')],
          [sg.Text("替换文件名:")],
          [sg.Input(key='-after-')],
          [sg.Button('替换')],[sg.Text("present by github.com/Wiiiiill")]]      
window = sg.Window('文件名替换程序', layout)
while True:                            
    event, values = window.read() 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break 
    elif not values['input']:
        sg.popup("请选择文件夹")
    elif not values['-before-']:
        sg.popup("请输入原文件名")
    elif not values['-after-']:
        sg.popup("请输入替换文件名")
    else :
        print("work baby")
        path = values['input']
        os.chdir(path)
        filenamelist = list(filter(lambda name:(values['-before-'] in name) and ((".psd" in name) or (".jpg" in name) or (".png" in name))   ,os.listdir(path)))
        if len(filenamelist):
            for name in filenamelist :
                old=name
                new=old.replace(values['-before-'],values['-after-'])
                print(old,new)
                os.rename(old,new)
            #print(path,filenamelist)
            sg.popup_ok("替换成功")
        else:
            sg.popup_ok("无可替换文件")
window.close()
