#!/bin/bash

echo Please enter your username:
read username
cd /home/$username/checkra1npython
echo Downloading latest checkra1npython version
wget https://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py
echo Copying service from github clone setup files to system services location
sudo cp /home/$username/checkra1npython/checkra1npythongui.service /lib/systemd/system/checkra1npythongui.service
echo running chmod on service
sudo chmod 644 /lib/systemd/system/checkra1npythongui.service
echo restarting systemctl daemon
sudo systemctl daemon-reload
echo enabling checkra1npythongui.service
sudo systemctl enable checkra1npythongui.service
echo This device needs to restart. Press enter now or CTRL + C to stop this setup and restart manually later. Install will finalize on next reboot.
read restartvarr
sudo restart
