# 导入包
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showinfo
from os import environ, system
from requests import post

# 创建窗口
hide = Tk()
hide.withdraw()

# 设置变量
title = "文件安全工具"  # 标题
filenames = []  # 文件列表
UserProfile = environ["USERPROFILE"]  # 用户配置文件目录
openfiles = askopenfilenames(
    title=title, initialdir=UserProfile, filetype=(["所有文件", "*.*"],)
)  # 文件上传窗口
webPaths = []  # 储存文件分析说明的网络位置列表

# 遍历选中文件的路径，输出到文件列表
for f in openfiles:
    filenames.append(f)

# 设定上传函数
def upload(path):  # 运用微步云沙箱恶意文件检测功能
    apiKey = "23bd94daee364ec88ce632f8b0f1b0b5ecd099a08a794dd88ee1858cd92b7b86"  # 开发者密钥
    sandBox = "win7_sp1_enx64_office2013"  # 设置沙箱类型
    runTime = 280  # 运行时间
    fileObject = open(path, "rb")  # 储存文件对象
    url = "https://api.threatbook.cn/v3/file/upload"  # 文件上传接口
    fileNameTemp = path.split("/")  # 获取分段文件路径
    fileConfig = fileNameTemp[len(fileNameTemp) - 1]  # 获取文件名称

    # 数据字典
    data = {
        "apikey": apiKey,
        "sandbox_type": sandBox,
        "runtime": runTime,
    }
    # 文件字典
    upFile = {
        "file": (fileConfig, fileObject),
    }

    # 发送网络请求
    response = post(url, data=data, files=upFile)  # 向上传接口发送数据和文件
    content = response.json()  # JSON 解析
    return content["data"]["permalink"]  # 返回结果信息


# 遍历文件列表，发送到文件接口
for value in filenames:
    webPaths.append(upload(value))  # 添加到网址列表

webString = "\n".join(webPaths)  # 将网址添加到字符串中

with open(UserProfile + "\\Desktop\\文件分析.txt", "w", encoding="UTF-8") as f:
    f.write(webString)  # 写入文件

showinfo(title,'处理完成！') # 弹出窗口
exit()
hide.mainloop()
