@echo off
title ���̱�ը�޸����� By @PanDaoxi

:input
set /p Disk=��������Ҫ�޸��ı���PanDaoxi�ƴ��̱�ը���ߡ��Ĵ����̷���
set %Disk%=%Disk:~0,1%
if not exist "%Disk%:\" (
echo ������Ĵ����̷������ڣ��뻻һ����
echo.
goto input
)
if not exist "%Disk%:\PanDaoxiYYDS" (
echo ����ѡ���̷���δ���ƻ����뻻һ����
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
echo �޸���ɣ�
timeout 3
goto exi
)
else (
echo ����������˵����⣬�޸�ʧ�ܡ�
pause
)

:exi
cls
echo ��PanDaoxi�ƴ��̱�ը���ߡ��޸�����ɣ�
echo Copyright 2022 by @PanDaoxi. ��������
pause
start https://www.luogu.com.cn/user/593403