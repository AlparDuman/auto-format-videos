## Table of contents
* [Description](#description)
* [Dependencies](#dependencies)
* [How to use](#how-to-use)
* [Set up as automatic task in background](#set-up-as-automatic-task-in-background)


## Description
Detect new video files in root- and subdirectories and process each video with given custom settings file for avidemux. Settings file si preset as x264 & aac codecs, uses free cpu time to encode in higher quality than gpu encoded, see [reddit.com | x264 encoding is still the best, slow isn't better and NVENC is second](https://www.reddit.com/r/Twitch/comments/c8ec2h/guide_x264_encoding_is_still_the_best_slow_isnt/?rdt=38004).

## Dependencies
- [Avidemux VC++ (v2.8.0 or newer)](https://sourceforge.net/projects/avidemux/files/avidemux/2.8.1/Avidemux_2.8.1%20VC%2B%2B%2064bits.exe/download)

## How to use
- Copy "auto format videos.cmd", "auto format videos (set as idle priority).cmd" & "auto format videos (settings).py" in the folder you want to be processed with its subfolders
- Customize "auto format videos (settings).py" to your needs
- Start "auto format videos.cmd" to begin and close its command window to stop
- If setup as background task you need to stop the process via the Windows task scheduler!

## Set up as automatic task in background
- Recomended to use Windows Task Scheduler (invisible in background):
  - Create a new task which starts "auto format videos.cmd" in the folder it is in
  - Set trigger "on startup" or "on login"
- Alternatively a shortcut in startup folder (visible in taskbar):
  - Press [WIN] + [R] and enter "shell:startup"
  - Create a shortcut of "auto format videos.cmd", configure it to be launched minimized and move it to the opened startup folder
