# Author:PanDaoxi
# Created on Aug.1st, 2023.
from pywebio.output import *
from pywebio.input import *
from os.path import exists
from requests import get
from os import mkdir

if not exists("./books"):
    mkdir("./books")
data = input_group("欢迎下载义务教育教科书", [textarea("输入您要下载的电子课本的 URL，一行一个", type=TEXT, placeholder="请在此处输入形如下面的 URL（8A 语）：\nhttps://basic.smartedu.cn/tchMaterial/detail?contentType=assets_document&contentId=4f64356a-8df7-4579-9400-e32c9a7f6718&catalogType=tchMaterial&subCatalog=tchMaterial", help_text="您可以到这里去找电子书的网址，并粘贴到程序中：https://basic.smartedu.cn/tchMaterial", name="urls")])

k, n = 1, 0
err = []

try:
    put_markdown("下载部分电子课本时速度较慢，原因是程序为您挑选较清晰的一本。\n请稍等……")
    for i in data["urls"].splitlines():
        id = i.split("&")[1].split("=")[1]
        with open("./books/第%d本电子书.pdf" % k, "wb") as f:
            r1 = get("https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets/%s.pkg/pdf.pdf" % id).content
            if not ("NoSuchKey" in str(r1)):
                f.write(r1)
            else:
                f.write(get("https://r2-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/%s.pkg/pdf.pdf" % id).content)
        put_markdown("已下载第 `%d` 本书。ID：`%s`" % (k, id))
        k += 1
except Exception:
    n += 1
    err[n] = [k, data["urls"].splitlines()[k-1]]
    k += 1

put_markdown("完成下载。您可以在 `books` 文件夹下找到您要找的电子书。")
if n > 1:
    put_markdown("-----\n但是，下载 %d 本书时出现了一些错误：" % n)
    for i in err:
        put_markdown("下载第 `%d` 本书时错误。URL：%s" % (i[0], i[1]))