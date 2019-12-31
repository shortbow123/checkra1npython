#!/bin/bash

echo "Updating sources and upgrading packages (this may take a while)..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Installing dependancies and daemon tools (this may take a while)..."
sudo apt-get install daemontools daemontools-run -y
pip3 install wget
pip3 install pygame

echo Creaing service directory...
mkdir /etc/service/checkra1npythongui

echo Copying daemon run file...
cp /home/$USER/checkra1npython/run /etc/service/checkra1npythongui/run

echo Fixing permissions...
sudo chmod u+x /etc/service/checkra1npythongui/run

echo This device needs to restart. Press enter to restart, or CTRL + C to stop this setup and restart manually later. Device will start checkra1npython at next boot.
read restartconfirmation
sudo reboot


