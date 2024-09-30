### Python script for downloading videos from YouTube and VK (GUI) 
#### Version: 1.5+ (current)

![app screenshot](https://github.com/WISEPLAT/YouTube_VK_Video_Download/blob/master/app_screen.jpg?raw=true)


### UPD: April 2 2024 Version 1.5
The code has been redone using yt-dlp, downloading open videos is available again. 
The download_video function runs in a separate thread, which allows the main program execution thread to update the interface state. During the download process, the current information is displayed in the interface.

### What's it?

Python script for downloading videos from YouTube and VK via GUI.  


### How do I start using it?

1. Download the archive with the latest version and unzip it to any place convenient for you; 

2. Install the necessary components and dependencies if necessary;

3. Run the file (script) 

*youtube_vk_video_download.py* - to download videos in threads;

or *youtube_vk_video_download_no_threads.py* - to download videos NOT in threads (to be not Banned);

4. In the window that appears, paste the link to the video in the input field (or links - separated with comma) and click *Download video*;

5. In case of successful download, a notification will appear, and the video will be saved in the *downloads* folder

> For YouTube, the links should look like: *https://www.youtube.com/shorts/L-F7stkCG6A* or *https://www.youtube.com/watch?v=RoJhyg8m8Rg*
![youtube downloads](https://raw.githubusercontent.com/WISEPLAT/YouTube_VK_Video_Download/main/youtube_downloads.jpg)

> For VK, the links should look like: *https://vk.com/video-174522765_456239108* 
![vk downloads](https://github.com/WISEPLAT/YouTube_VK_Video_Download/blob/master/vk_downloads.jpg?raw=true)


### Possible problems

- The link is not inserted into the input field
> You probably have the Russian keyboard layout enabled, switch to English.

- When the program window is closed, the console continues to run
> The bug is related to ongoing processes in the background, it will be resolved in the future

- The application (script) freezes during download
> This is a feature of the work, at this time there is a download in the background, at the end of the download the script will hang itself.

- The video does not download
> The video is either closed to unauthorized access or has a format\source not supported by yt-dlp

- The files have a format after downloading .unknown_video
> Rename to .mp4? as a rule, this is enough to solve the problem

- Where is the finished video downloaded?
> To the downloads directory, located in the same place where your script is located vk_video_download.py

---

The command to install the necessary components

    pip install -r requirements.txt
    
Or a separate installation of yt-dlp

    python3 -m pip install -U yt-dlp
    
The command to build the exe file in pyinstaller:

    pyinstaller vk_video_download.py --noconsole --onefile --icon=icon.ico
 
### Copyrights and Licenses
Not for commercial use.

### Did you find this useful?! => Set a star))

## Thanks
Thanks for initial source code to github.com/blyamur
