## Contents
* [Description](#description)
* [Dependency](#dependency)
* [Setup](#setup)
* [Set up as automatic task in background](#set-up-as-an-automatic-task-in-the-background)


## Description
Detects new video files in a folder and its subfolders, processes each video with a custom settings file using avidemux, and deletes the source video file if successful. The settings file is preset to the codecs x264 (more devices can decode x264 via hardware acceleration than x265 via hardware acceleration) and aac (up to 8 stereo channels with -3db normalization), this is compatible with [Blackmagic Design DaVinci Resolve](https://www.blackmagicdesign.com/de/products/davinciresolve/). For better quality, change the "general.preset" from "faster" to a lower setting such as "fast", "medium", "slow", "slower", "veryslow", or "placebo" in "auto format videos (settings).py", the slower the speed the higher the quality. It uses free CPU time to encode at higher quality than the GPU encoder can, see [x264 encoding is still the best, slow isn't better and NVENC is second](https://www.reddit.com/r/Twitch/comments/c8ec2h/guide_x264_encoding_is_still_the_best_slow_isnt/?rdt=38004).

## Dependency
- [Avidemux VC++ (v2.8.0 or newer)](https://sourceforge.net/projects/avidemux/files/avidemux/2.8.1/Avidemux_2.8.1%20VC%2B%2B%2064bits.exe/download)

## Setup
- Install avidemux, on which this project depends. If "avidemux_cli.exe" is not found, correct the path in "auto format videos.cmd" by editing it as a text file
- Copy "auto format videos.cmd", "auto format videos (set as idle priority).cmd" & "auto format videos (settings).py" to the folder you want to process with its subfolders
- Customize "auto format videos (settings).py" to your needs
- Launch "auto format videos.cmd" to start and close the command window to quit
- If you have set up the process as a background task, you must end it via the Windows Task Scheduler!

## Set up as an automatic task in the background
- Windows Task Scheduler (Recommended & invisible in background):
  - Create a new task that launches "auto format videos.cmd" in the folder where it is located
  - Set trigger "at startup" or "at login"
- Shortcut in startup folder (Alternative & visible in taskbar):
  - Press [WIN] + [R] and type "shell:startup".
  - Create a shortcut of "auto format videos.cmd", configure it to be launched minimized and move it to the opened startup folder
