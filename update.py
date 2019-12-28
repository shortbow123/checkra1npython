import wget
import os

linkToUpdate = "https://raw.githubusercontent.com/shortbow123/checkra1npython/master/program.py"
wget.download(linkToUpdate, 'program.py')
print("Update complete, restarting now.")
#if button not being held down dont reboot

os.popen('sudo reboot')
