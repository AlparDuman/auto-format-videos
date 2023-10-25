## Table of contents
* [Description](#description)
* [Dependencies](#dependencies)
* [How to use](#how-to-use)
* [Set up as automatic task in background](#set-up-as-automatic-task-in-background)


## Description
Detects new video files in a folder with its subfolders and processes each video with a custom settings file using avidemux. The settings file is preset as x264 and aac codecs. x264 is set to "placebo" speed for highest detail per bit, can be set to "faster", "medium" or "slow" with minimal quality loss but much better encoding speed. Also uses free CPU time to encode at higher quality than the GPU encoder can, see [reddit.com | x264 encoding is still the best, slow isn't better and NVENC is second](https://www.reddit.com/r/Twitch/comments/c8ec2h/guide_x264_encoding_is_still_the_best_slow_isnt/?rdt=38004).

## Dependencies
- [Avidemux VC++ (v2.8.0 or newer)](https://sourceforge.net/projects/avidemux/files/avidemux/2.8.1/Avidemux_2.8.1%20VC%2B%2B%2064bits.exe/download)

## How to use
- Copy "auto format videos.cmd", "auto format videos (set as idle priority).cmd" & "auto format videos (settings).py" to the folder you want to process with its subfolders
- Customize "auto format videos (settings).py" to your needs
- Launch "auto format videos.cmd" to start and close the command window to quit
- If you have set up the process as a background task, you must end it via the Windows Task Scheduler!

## Set up as automatic task in background
- Recomended | Use Windows Task Scheduler (invisible in background):
  - Create a new task which starts "auto format videos.cmd" in the folder it is in
  - Set trigger "on startup" or "on login"
- Alternative | Shortcut in startup folder (visible in taskbar):
  - Press [WIN] + [R] and enter "shell:startup"
  - Create a shortcut of "auto format videos.cmd", configure it to be launched minimized and move it to the opened startup folder
