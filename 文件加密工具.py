# 导入包
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from easygui import buttonbox, msgbox, passwordbox
from tkinter.messagebox import showinfo, showwarning, showerror
from os import name, environ
from hashlib import md5
from sys import exit
from random import shuffle
from base64 import (
    a85encode,
    a85decode,
    b64encode,
    b64decode,
    b32encode,
    b32decode,
    b16encode,
    b16decode,
)

# 生成随机字符串集合
def shuffle_str(s):
    str_list = list(s)
    shuffle(str_list)
    return "".join(str_list)


# 生成md5值储存密码
def create_md5(s):
    enc = md5(s.encode()).hexdigest()
    return enc


# 设置加密字典和映射字典
dx1marks = {}
dx1dict = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`~@#$%^&*()_+{}|\/{}[]<>?:;\"'=+-.,! "

# 声明变量
title = "文件通文件加解密工具"
ec = "UTF-8"
button = "确定"
userprofile = environ["Userprofile"].replace("\\", "/")
states = "RUNNING"

# 隐藏窗口
hide = Tk()
hide.withdraw()

# 分配到字典
for i in range(0, len(dx1dict)):
    if i <= 9:
        dx1marks["0" + str(i)] = dx1dict[i]
    else:
        dx1marks[str(i)] = dx1dict[i]

# dx1低级加密算法
class Dx1:
    # 设定属性
    def __init__(self):
        self.content = "DaoXi 1.0/2.0 Encrypt Decrypt Algorithm Library"
        self.interval_mark = "-"
        self.ec = "UTF-8"
        self.dx1dx1marks = dx1marks

    # 加密函数
    def encrypt(self):
        text = a85encode(self.content.encode(self.ec)).decode(self.ec)
        letters = []
        for i in text:
            letters.append(list(dx1marks.keys())[list(dx1marks.values()).index(i)])
        return ["OKAY", self.interval_mark.join(letters)]

    # 解密函数
    def decrypt(self):
        try:
            text = self.content.split(self.interval_mark)
            letters = []
            for i in text:
                letters.append(dx1marks[i])
            result = "".join(letters)
            return ["OKAY", a85decode(result.encode(self.ec)).decode(self.ec)]
        except Exception as e:
            return ["ERROR", e]


# dx1算法加密函数
def dx1encrypt(content, interval="-"):
    dx1 = Dx1()
    dx1.content = content
    dx1.interval_mark = interval
    text = dx1.encrypt()
    if text[0] == "OKAY":
        return text[1]
    else:
        return "Error! " + text[1]


# dx1算法解密函数
def dx1decrypt(content):
    dx1 = Dx1()
    dx1.content = content
    text = dx1.decrypt()
    if text[0] == "OKAY":
        return text[1]
    else:
        return "Error! " + str(text[1])


# dx2高级加密算法
class Dx2:
    # 设置属性
    def __init__(self):
        self.content = "DaoXi 1.0/2.0 Encrypt Decrypt Algorithm Library"
        self.interval_mark = "-"
        self.password = "default"
        self.__marks = {}
        self.__demark = {}
        self.__dx2dict = shuffle_str(dx1dict)
        for i in range(0, len(self.__dx2dict)):
            if i <= 9:
                self.__marks["0" + str(i)] = self.__dx2dict[i]
            else:
                self.__marks[str(i)] = self.__dx2dict[i]

    # 加密函数
    def encrypt(self):
        try:
            text = self.content
            passw = b32encode(create_md5(self.password).encode()).decode()
            map = b32encode(b64encode(a85encode(str(self.__marks).encode()))).decode()

            temp = []
            for i in text:
                temp.append(
                    list(self.__marks.keys())[list(self.__marks.values()).index(i)]
                )
            newtext = self.interval_mark.join(temp)

            deres = "%s(dx2)%s(dx2)%s(dx2)" % (newtext, passw, map)
            encresult = dx1encrypt(deres)
            return ["OKAY", encresult]
        except Exception as e:
            return ["ERROR", e]

    # 解密函数
    def decrypt(self):
        try:
            dec_result = dx1decrypt(self.content).split("(dx2)")
            dec_result.pop(3)

            pderes = b32decode(dec_result[1]).decode()
            ptryres = create_md5(self.password)

            if pderes == ptryres:
                x = a85decode(b64decode(b32decode(dec_result[2]))).decode()
                map = eval(x)
                self.__demark = map

                letters = []
                y = dec_result[0].split(self.interval_mark)
                for i in y:
                    if map[i]:
                        letters.append(map[i])
                tres = "".join(letters)
                return ["OKAY", tres]
            else:
                return ["ERROR", "The password is incorrect"]
        except Exception as e:
            return ["ERROR", e]


# dx2算法加密函数
def dx2encrypt(content, password):
    dx2 = Dx2()
    dx2.content = content
    dx2.password = password
    result = dx2.encrypt()
    if result[0] == "OKAY":
        return result[1]
    else:
        return result[0]


# dx2算法解密函数
def dx2decrypt(content, password):
    dx2 = Dx2()
    dx2.content = content
    dx2.password = password
    result = dx2.decrypt()
    if result[0] == "OKAY":
        return result
    else:
        return result


# 加密函数
def encodef():
    # 设置状态
    global states
    # 加载一个选择文件的窗口
    get = askopenfilename(
        title=title, initialdir=userprofile, filetypes=[("All Files", "*.*")]
    )
    # 读取文件内容
    with open(get, "rb") as f:
        temp = f.read()
    # 请求用户输入密码
    p = passwordbox("请输入加密密码（请妥善保存）：", title)
    # 加密文件内容
    encode_temp = dx2encrypt(a85encode(temp).decode(), p).encode()
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
    # 设置状态
    global states
    # 加载一个选择文件的窗口
    get = askopenfilename(
        title=title, initialdir=userprofile, filetypes=[("All Files", "*.*")]
    )
    # 请求用户输入加密密码
    p = passwordbox("请输入加密密码以解密文件：", title)
    # 读取加密文件
    passwordIsRight = False
    with open(get, "r", encoding=ec) as f:
        check = dx2decrypt(f.read(), p)
        if not check[1] == "The password is incorrect":
            temp = check[1].encode()
            temp = a85decode(temp)
            passwordIsRight = True
        else:
            showerror(title, "密码有误！")
            temp = "The password is incorrect"
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
    if passwordIsRight == True:
        msgbox("解密成功！", title, button)
    else:
        exit()
    states = "OVER"


# 帮助函数
def help():
    text = """欢迎使用此软件，此软件可以加密或解密各种文件，以免被盗窃。
    开发者：潘道熹
    版本：2.0
    开发时间：2021年8月
    联系邮箱：qingfengstudio@yeah.net
    客服QQ：3377063617
    代码语言：Python 3.6
    官方博客：https://blog.csdn.net/pandaoxi2020
    
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
