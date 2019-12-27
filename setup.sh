#!/bin/bash

#echo Please enter your username:
#read username
cd $HOME/checkra1npython
wget https://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py
sudo cp -rf $HOME/checkra1npython/checkra1npythongui.service /lib/systemd/system/checkra1npythongui.service
sudo chmod 644 /lib/systemd/system/checkra1npythongui.service
sudo systemctl daemon-reload
sudo systemctl enable checkra1npythongui.service
echo This device needs to restart. Press enter now or CTRL + C to stop this setup and restart manually later. Install will finalize on next reboot.
read restartvarr
sudo restart
