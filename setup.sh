#!/bin/bash

echo Please enter your username:
read username

echo Saving the username...
echo $username > /un.txt
crp=/checkra1npythongui
cd /home/$username/checkra1npython

##### The old service installation method, only used because it can run scripts as root #####

echo Removing old checkra1npyhon files...
rm -rf $crp

echo Creaing new checkra1npython directory...
mkdir $crp

echo Copying program to desired location...
cp /home/$username/checkra1npython/program.py $crp/program.py

echo Copying update script to desired location...
cp /home/$username/checkra1npython/update.py $crp/update.py

echo Making resources directory...
mkdir $crp/resources

echo Copying resources to resource location...
cp /home/$username/checkra1npython/resources/checkra1n.png $crp/resources/checkra1n.png

echo Copying the service into the correct directory...
sudo cp /home/$username/checkra1npython/checkra1npythongui.service /etc/systemd/system/checkra1npythongui.service

echo running chmod on service
sudo chmod 644 /etc/systemd/system/checkra1npythongui.service

echo restarting systemctl daemon
sudo systemctl daemon-reload

echo enabling checkra1npythongui.service
sudo systemctl enable checkra1npythongui.service


##### The newer service installtion method ######
#
#echo Service will be installed under the name "checkra1npythongui"...
#
#echo Copying program to desired location...
#cp /home/$username/checkra1npython/program.py /program.py
#
#echo Copying updater to desired location...
#cp /home/$username/checkra1npython/update.py /update.py
#
#echo Copying resources to desired location
#mkdir /resources
#cp /home/$username/checkra1npython/resources/* /resources/*
#
#echo Making sure everything is up to date (this may take a while)...
#sudo apt-get update -y
#sudo apt-get upgrade -y
#
#echo Installing the daemontools and dependancies...
#sudo apt-get install daemontools daemontools-run -y
#
#echo Creating service directory...
#sudo mkdir /etc/service/checkra1npythongui
#
#echo Copying run file...
#sudo cp /home/$username/checkra1npython/run /etc/service/checkra1npythongui/run
#
#echo Setting up correct permissions...
#sudo chmod u+x /etc/service/checkra1npythongui/run

echo This device needs to restart. Press enter now or CTRL + C to stop this setup and restart manually later. Install will finalize on next reboot.
read restartconfirmation
sudo reboot
