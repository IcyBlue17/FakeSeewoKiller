from cgitb import text
import os
import tkinter as tk
import time

a = 0


# Commands
def start():
    # ml_s=cmd.get()
    # ml=str(ml_s)
    # os.system(ml)
    os.system("start Koid.exe")


# 创建一个窗口
def create_window():
    win3 = tk.Tk()
    win3.title('信息中心电脑反控')
    win3.geometry('400x200')
    tk.Label(win3, text='成功连接到信息中心的计算机并使用MeteorPvP0x2019漏洞获取cmd！').pack()
    tk.Label(win3, text='请输入您要在cmd内执行的内容').pack()
    cmd = tk.Entry(win3).pack()
    tk.Button(win3, text='执行', command=start).pack()
    # os.system("start C:\Windows\System32\mstsc.exe")


# 杀死winnt.exe
def kill():
    os.system('taskkill /im winnt.exe /f')


def delfile():
    win4 = tk.Tk()
    win4.title("冰点还原一键关闭")
    win4.geometry('400x200')
    tk.Label(win4, text='冰点还原关闭程序', font=(None, 15))

    win4.mainloop()
    # os.system('del D:/*')


def get():
    # os.system('fsutil file createnew /WindowsUpdate.vape 20000')
    print('1')


def abc():
    os.system("start SeewoRunInject.exe")
    time.sleep(13)
    win2 = tk.Tk()
    win2.title("希沃管家注入控制台")
    win2.geometry('400x200')
    tk.Label(win2, text='希沃管家注入控制台', font=(None, 15)).pack()
    tk.Label(win2, text='注入成功！')
    tk.Button(win2, text='杀死希沃管家所有进程', command=kill).pack()
    tk.Button(win2, text='反控信息中心服务器', command=cmd).pack()
    tk.Button(win2, text='强制关闭冰点还原', command=delfile).pack()
    tk.Button(win2, text='管理员密码强行获取', command=get).pack()
    tk.Label(win2, text='Ps：部分希沃会带有进程守护，强杀进程可能会导致系统崩溃')
    win2.mainloop()


# Command
# r
win = tk.Tk()
win.title("希沃冰点还原破解工具 v2022.9")
win.geometry("800x300")
tk.Label(win, text='希沃冰点还原破解工具', font=("黑体", 20)).pack()
tk.Checkbutton(win, text='InjectHool反检测').pack()
tk.Checkbutton(win, text='ZeloatModule+高级模式').pack()
tk.Label(win, text='请输入您的学校代码,留空为自动识别:').pack(), tk.Entry(win, text='001035').pack()
tk.Button(win, text='开始注入希沃管家进程：SeewoAsssiant.exe', command=abc).pack()
win.mainloop()
