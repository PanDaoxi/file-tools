@echo off
title 磁盘爆炸修复工具 By @PanDaoxi

:input
set /p Disk=请输入需要修复的被【PanDaoxi牌磁盘爆炸工具】的磁盘盘符：
set %Disk%=%Disk:~0,1%
if not exist "%Disk%:\" (
echo 你输入的磁盘盘符不存在！请换一个。
echo.
goto input
)
if not exist "%Disk%:\PanDaoxiYYDS" (
echo 您所选的盘符并未被破坏！请换一个。
echo.
goto input
)
goto fix

:fix
echo.
attrib -s -h "%Disk%:\PanDaoxiYYDS"
del "%Disk%:\PanDaoxiYYDS\*.*" /s /q /f > nul
rd "%Disk%:\PanDaoxiYYDS"
if not exist "%Disk%:\PanDaoxiYYDS" (
echo 修复完成！
timeout 3
goto exi
)
else (
echo 可能哪里出了点问题，修复失败。
pause
)

:exi
cls
echo 【PanDaoxi牌磁盘爆炸工具】修复已完成！
echo Copyright 2022 by @PanDaoxi. 求三连！
pause
start https://www.luogu.com.cn/user/593403