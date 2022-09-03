# 导入需要用到的模块
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from easygui import buttonbox, msgbox
from tkinter.messagebox import showinfo, showwarning, showerror
from base64 import a85encode, a85decode
from os import name, environ
from sys import exit

# 声明变量
title = "文件通"
ec = "UTF-8"
button = "确定"
userprofile = environ["Userprofile"].replace("\\", "/")
states = "RUNNING"

# 隐藏窗口
hide = Tk()
hide.withdraw()


# 加密函数
def encodef():
    # 加载一个选择文件的窗口
    get = askopenfilename(
        title=title, initialdir=userprofile, filetypes=[("All Files", "*.*")]
    )
    # 读取文件内容
    with open(get, "rb") as f:
        temp = f.read()
    # 加密文件内容
    encode_temp = a85encode(temp)
    # 获取文件名称
    file_name_list = get.split("/")
    file_name = file_name_list[len(file_name_list) - 1]
    file_path = "/".join(file_name_list).replace(file_name, "(encode)" + file_name)
    # 加密文件
    with open(file_path, "wb") as a:
        a.write(encode_temp)
    # 提示用户加密成功
    msgbox("加密成功！", title, button)
    states = "OVER"


# 解密函数
def decodef():
    # 加载一个选择文件的窗口
    get = askopenfilename(
        title=title, initialdir=userprofile, filetypes=[("All Files", "*.*")]
    )
    # 读取加密文件
    with open(get, "r", encoding=ec) as f:
        temp = bytes(a85decode(f.read()))
    # 获取文件解密内容
    decode_temp = temp
    # 获取文件名称
    file_name_list = get.split("/")
    file_name = file_name_list[len(file_name_list) - 1]
    file_path = "/".join(file_name_list).replace(file_name, "(decode)" + file_name)

    # 在解密目录下添加文件
    with open("%s" % (file_path), "wb") as a:
        a.write(decode_temp)
    # 提示用户加密成功
    msgbox("解密成功！", title, button)
    states = "OVER"


# 帮助函数
def help():
    text = """欢迎使用此软件，此软件可以加密或解密各种文件，以免被盗窃。
    开发者：潘道熹
    开发时间：2020年1月
    联系邮箱：qingfengstudio@yeah.net
    客服QQ：3377063617
    代码语言：Python 3.6
    
    如果您在使用中出现了问题，请联系客服解决。
    """
    msgbox(text, title, button)


try:
    while states == "RUNNING":
        if __name__ == "__main__" and name == "nt":
            choose = buttonbox(
                "欢迎使用%s！\n请选择您需要的服务：" % title, title, ("加密文件", "解密文件", "关于我们")
            )
            if choose == "关于我们":
                help()
            elif choose == "加密文件":
                encodef()
            elif choose == "解密文件":
                decodef()
            else:
                exit()
        else:
            showerror(title, "请使用Windows系统运行此程序！\n请自主运行此程序，不能使用模块进行导入。")
            exit()
except Exception as e:
    showwarning(title, "错误：%s" % e)
hide.mainloop()

