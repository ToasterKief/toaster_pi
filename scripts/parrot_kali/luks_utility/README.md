This script is an interactive terminal for creating an encrypted luks partition on an external device (USB) 
Be wary of the arguments you pass to this script and make sure to close all processes using the opened partition before letting the script finish.

before running, plug in external device, do not mount or do nothing to it, just run the script
make sure not to accidentally fuck up your OS filesystem.
usage:
sudo su
python3 newluks_dev.py



## Opening and modifying the encrypted partition
usage:
sudo su
python3 unlock_dev.py
#keep the terminal open while the luks container is unlocked, allow the script to lock and close it when finished

## Back up field_data directory to encrypted volume

