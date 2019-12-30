#!/bin/bash

echo Please enter your username:
read username

echo Saving the username...
echo $username > /un.txt
crp=/checkra1npythongui
cd /home/$username/checkra1npython

##### The old service installation method, back into retirement #####
#
#echo Removing old checkra1npyhon files...
#rm -rf $crp
#
#echo Creaing new checkra1npython directory...
#mkdir $crp
#
#echo "Installing depenedancies (this may take a while)..."
#pip3 install pygame
#pip3 install wget 
#
#echo Copying program to desired location...
#cp /home/$username/checkra1npython/program.py $crp/program.py
#
#echo Copying update script to desired location...
#cp /home/$username/checkra1npython/update.py $crp/update.py
#
#echo Making resources directory...
#mkdir $crp/resources
#
#echo Copying resources to resource location...
#cp /home/$username/checkra1npython/resources/checkra1n.png $crp/resources/checkra1n.png
#
#echo Setting correct permissions for the checkra1npython directory...
#sudo chown $username $crp
#echo Copying the service into the correct directory...
#sudo cp /home/$username/checkra1npython/checkra1npythongui.service /etc/systemd/system/checkra1npythongui.service
#
#echo Running chmod on service...
#sudo chmod 644 /etc/systemd/system/checkra1npythongui.service
#
#echo Restarting systemctl daemon...
#sudo systemctl daemon-reload
#
#echo Enabling checkra1npythongui.service...
#sudo systemctl enable checkra1npythongui.service


##### The newer service installtion method ######

echo Service will be installed under the name "checkra1npythongui"...

echo Removing old checkra1npython files...
rm -rf $crp

echo Making new checkra1npythongui python directory...
mkdir $crp

echo Copying program to desired location...
cp /home/$username/checkra1npython/program.py $crp/program.py

echo Copying updater to desired location...
cp /home/$username/checkra1npython/update.py $crp/update.py
cp /home/$username/checkra1npython/version $crp/version

echo Copying resources to desired location
mkdir $crp/resources
cp /home/$username/checkra1npython/resources/checkra1n.png $crp/resources/checkra1n.png

echo "Making sure everything is up to date (this may take a while)..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo Installing the daemontools and dependancies...
sudo apt-get install daemontools daemontools-run -y
pip3 install wget
pip3 install pygame

echo Creating service directory...
sudo mkdir /etc/service/checkra1npythongui

echo Copying run file...
sudo cp /home/$username/checkra1npython/run /etc/service/checkra1npythongui/run

echo Setting up correct permissions...
sudo chmod u+x /etc/service/checkra1npythongui/run
sudo chown $username $crp

echo This device needs to restart. Press enter to restart, or CTRL + C to stop this setup and restart manually later. Device will start checkra1npython at next boot.
read restartconfirmation
sudo reboot
