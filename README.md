# pi_video_looper
Application to turn your Raspberry Pi into a dedicated looping video playback device, good for art installations, information displays, or just playing cat videos all day.

This program is adapted from Adafruit's Pi Video Looper. It has been adapted to allow slideshow of video and images. It also has an auto detect for when new files are moved, created, deleted, or copied into the directory that is being watched. The auto detect was implemented using pyinotify and using the threaded version. The rest of the framework is kept roughly in the same structure that it originally was written in.

Install:
cd /home/pi
git clone https://github.com/dezito/pi_video_looper
cd pi_video_looper
sudo sh ./install.sh