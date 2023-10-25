: Repository https://github.com/AlparDuman/auto-format-videos
: GNU General Public License v3.0 https://github.com/AlparDuman/auto-format-videos/blob/main/LICENSE

@echo off
title auto format videos (set as idle priority)
set loop=0

:loop

timeout /t 1
wmic process where name="avidemux_cli.exe" CALL setpriority "idle"
set /a loop=%loop%+1 
if "%loop%"=="10" exit

goto loop
