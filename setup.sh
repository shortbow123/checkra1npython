#!/bin/bash

echo Please enter your username:
read username

echo Saving the username...
echo $username > /un.txt
cd /home/$username/checkra1npython

#The old service installation method
#echo Downloading latest checkra1npython version
#wget https://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py
#
#echo Copying service from github clone setup files to system services location
#sudo cp /home/$username/checkra1npython/checkra1npythongui.service /lib/systemd/system/checkra1npythongui.service
#
#echo running chmod on service
#sudo chmod 644 /lib/systemd/system/checkra1npythongui.service
#
#echo restarting systemctl daemon
#sudo systemctl daemon-reload
#
#echo enabling checkra1npythongui.service
#sudo systemctl enable checkra1npythongui.service

#The new service installtion method

echo Service will be installed under the name "checkra1npythongui"...

echo Copying program to desired location...
cp /home/$username/checkra1npython/program.py /program.py

echo Copying updater to desired location...
cp /home/$username/checkra1npython/update.py /update.py

echo Copying resources to desired location
mkdir /resources
cp /home/$username/checkra1npython/resources/* /resources/*

echo Making sure everything is up to date...
sudo apt-get update
sudo apt-get upgrade

echo Installing the daemontools and dependancies...
sudo apt-get install daemontools daemontools-run

echo Creating service directory...
sudo mkdir /etc/service/checkra1npythongui

echo Copying run file...
sudo cp /home/$username/checkra1npython/run /etc/service/checkra1npythongui/run

echo Setting up correct permissions...
sudo chmod u+x /etc/service/checkra1npythongui/run

echo This device needs to restart. Press enter now or CTRL + C to stop this setup and restart manually later. Install will finalize on next reboot.
read restartconfirmation
sudo reboot
