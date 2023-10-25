: Repository https://github.com/AlparDuman/auto-format-videos
: GNU General Public License v3.0 https://github.com/AlparDuman/auto-format-videos/blob/main/LICENSE

@echo off

set if_cut_exists_delete_source=true
set if_formated_exists_delete_source=true
set if_formated_exists_format_source=false
set avidemux_cli="C:\Program Files\Avidemux 2.8 VC++ 64bits\avidemux_cli.exe"

set title=auto format videos
title %title%

rem if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit ) : debug
if not exist %avidemux_cli% (
  echo Avidemux not found!
  pause
  exit /b
)

:cycle
setlocal EnableExtensions enableDelayedExpansion

for /d /r %%D in (.) do (
  echo.%%D | findstr /C:"_">nul || (
    pushd %%D
    for %%f in (*.avi *.flv *.mkv *.mov *.mp4 *.ts *.mpg *.webm) do (
      if exist "%%f" (
        echo.%%f | findstr /C:".formated.">nul || (
          if %if_cut_exists_delete_source% equ true (
            for %%s in ("%%~nf".*.avi "%%~nf".*.flv "%%~nf".*.mkv "%%~nf".*.mov "%%~nf".*.mp4 "%%~nf".*.ts "%%~nf".*.mpg "%%~nf".*.webm) do (
              echo.%%s | findstr /C:".cut.">nul && (
                if exist "%%f" (
                  del "%%f"
                  rem goto breakLoop0 : goto causes syntactic issue
                )
              )
            )
            rem :breakLoop0
          )
          if %if_formated_exists_delete_source% equ true (
            for %%s in ("%%~nf".*.avi "%%~nf".*.flv "%%~nf".*.mkv "%%~nf".*.mov "%%~nf".*.mp4 "%%~nf".*.ts "%%~nf".*.mpg "%%~nf".*.webm) do (
              echo.%%s | findstr /C:".formated.">nul && (
                if exist "%%f" (
                  del "%%f"
                  rem goto breakLoop1 : goto causes syntactic issue
                )
              )
            )
            rem :breakLoop1
          )
          if exist "%%f" (
            set do_formating=true
            if %if_formated_exists_format_source% equ false (
              for %%s in ("%%~nf".*.avi "%%~nf".*.flv "%%~nf".*.mkv "%%~nf".*.mov "%%~nf".*.mp4 "%%~nf".*.ts "%%~nf".*.mpg "%%~nf".*.webm) do (
                echo.%%s | findstr /C:".formated.">nul && (
                  set do_formating=false
                  rem goto breakLoop2 : goto causes syntactic issue
                )
              )
              rem :breakLoop2
            )
            if !do_formating! equ true (
              2>nul (call;>>"%%f") && (
                if !sizeBefore! equ !sizeAfter! (
                  title !title! ^| %cd%\%%f
                  start "" "auto format videos (set as idle priority).cmd"
                  %avidemux_cli% --nogui --load "%%f" --run "%~dp0auto format videos (settings).py" --save "%%~nf.formating.mp4" --quit
                  if errorlevel 0 (
                    if exist "%%~nf.formated.mp4" del "%%~nf.formated.mp4"
                    ren "%%~nf.formating.mp4" "%%~nf.formated.mp4"
                    if %if_formated_exists_delete_source% equ true (
                      if exist "%%f" del "%%f"
                    )
                  )
                )
              )
            )
          )
        )
      )
    )
    popd
  )
)

endlocal
title %title%
rem pause : debug
timeout /t 60
goto cycle
