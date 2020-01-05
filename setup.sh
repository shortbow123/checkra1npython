#!/bin/bash

username=$(whoami)

crp=/home/$username/Applications/checkra1npython
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

echo Copying program to desired location...
cp -rf /home/$username/checkra1npython/checkra1npythongui/ $crp

echo Creating daemon run file...
echo "#!/bin/bash" > run
echo "exec /usr/bin/python3 /home/$USER/Applications/program.py" > run

echo "Setting up daemon_setup.sh..."
echo -e "CURUSER=$USER\n$(cat daemon_setup.sh)" > daemon_setup.sh

echo Done with the program, the daemon STILL NEED TO BE SETUP, please run 'sudo ./daemon_setup.sh'
