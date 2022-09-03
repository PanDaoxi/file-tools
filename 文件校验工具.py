# 导入包
from easygui import msgbox, textbox, buttonbox
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from os import environ, stat
from time import strftime, localtime
from hashlib import md5, sha256, sha1
from sys import exit

# 声明变量
title = "文件校验工具"
hide = Tk()
hide.withdraw()

# 时间戳格式化
def timeFormat(stamp):
    return strftime("%Y-%m-%d %H:%M:%S", localtime(stamp))


# 获取Md5值
def getMd5(text):
    md5text = md5(text).hexdigest()
    return md5text


# 获取Sha-256值
def getSha256(text):
    sha256text = sha256(text).hexdigest()
    return sha256text


# 获取Sha-1值
def getSha1(text):
    sha1text = sha1(text).hexdigest()
    return sha1text


# 获取Hash值
def getHash(text):
    hashtext = hash(text)
    return hashtext


# 获取文件加密值
def getFileEncode(path):
    with open(path, "rb") as f:
        temp = f.read()

    data = {
        "hash": getHash(temp),
        "md5": getMd5(temp),
        "sha-1": getSha1(temp),
        "sha-256": getSha256(temp),
    }
    return data


# 文件信息函数
def fileAttrib(fn):
    statinfo = stat(fn)

    fileSize = statinfo.st_size
    fileLastVisitTime = timeFormat(statinfo.st_atime)
    fileLastReviseTime = timeFormat(statinfo.st_mtime)
    fileCreationTime = timeFormat(statinfo.st_ctime)

    data = {
        "fs": fileSize,
        "flvt": fileLastVisitTime,
        "flrt": fileLastReviseTime,
        "fct": fileCreationTime,
    }
    return data


# 文件选择函数
def choice():
    current = environ["UserProfile"]
    fileName = askopenfilename(
        title=title, filetypes=[("所有文件", "*.*")], initialdir=current
    )

    att = fileAttrib(fileName)
    enc = getFileEncode(fileName)
    txt = """文件路径：%s
文件大小（Bytes）：%d
文件最后一次访问时间：%s
文件最后一次修改时间：%s
文件创建时间：%s
\n

文件HASH值：%s
文件md5值：%s
文件sha-1值：%s
文件sha-256值：%s
""" % (
        fileName,
        att["fs"],
        att["flvt"],
        att["flrt"],
        att["fct"],
        enc["hash"],
        enc["md5"],
        enc["sha-1"],
        enc["sha-256"],
    )
    textbox("文件详细信息如下！", title, text=txt)


# 函数调用
while True:
    try:
        choose = buttonbox(
            "欢迎使用文件校验工具！\n请按“选择文件”打开您要校验的文件，按“退出程序”退出！", title, ("选择文件", "退出程序")
        )
        if choose == "选择文件":
            choice()
        else:
            exit()
    except Exception as e:
        msgbox("错误：%s" % e, title)
        exit()
hide.mainloop()
