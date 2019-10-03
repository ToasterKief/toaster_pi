#!/usr/bin/python3

import os
import sys
import time

def clearterm():
	os.system("clear")
	time.sleep(0.1)
def main():
	while True:
		clearterm()
		os.system("mkdir /var/lib/myluksvolume")
		clearterm()
		time.sleep(0.3)
		
		print("Run this script as a super user! \nExecute 'sudo su' from the terminal then execute this script.\n")
		input("Make sure the USB device you're going to partition is connected > ")

		clearterm()
		os.system("fdisk -l")
		input("Press enter after deciding which storage device you want to use > ")
		clearterm()
		device_name = str(input("Enter the exact name of the desired device, careful! > "))
		clearterm()
		input("This will erase all data on the device and format it, cool? >")
		os.system("parted --script /dev/{} mktable msdos".format(device_name))
		print("Created new partition table on /dev/{}\n".format(device_name))
		time.sleep(0.3)
		start_part = str(input("Starting sector for the new partition (Min= 1) > "))
		part_size = str(input("Desired size of the new partition (MB) > "))
		end_part = str(int(start_part) + int(part_size))
		os.system("parted --script /dev/sdd mkpart primary ext4 {} {}".format(start_part, end_part))
		print("Successfully partitioned device\n")
		time.sleep(0.1)
		print("Partition device name: {}1".format(device_name))
		partition_name = str(device_name + "1")
		input("Press enter to continue > ")
		clearterm()
		print("Setting up partition as a luks encrypted volume..\n")
		os.system("cryptsetup luksFormat /dev/{}".format(partition_name))
		time.sleep(0.3)
		print("Successfully created luks volume.\n")
		input("Press enter to continue > ")
		clearterm()
		print("Opening volume and creating mount point.\n")
		time.sleep(0.1)
		volume_name = str(input("Enter a filename for the volume and mount point > "))
		time.sleep(0.1)
		os.system("cryptsetup luksOpen /dev/{} {}".format(partition_name, volume_name))
		time.sleep(0.1)
		os.system("cd /dev/mapper/")
		input("Press enter to create the volume's filesystem >")
		clearterm()
		print("Creating 'ext4' file system on volume..\n")
		time.sleep(0.2)
		os.system("mkfs.ext4 /dev/mapper/{}".format(volume_name))
		time.sleep(0.2)
		print("Successfully created ext4 filesystem..\n")
		time.sleep(0.2)
		os.system("mkdir /{}".format(volume_name))
		time.sleep(0.1)
		os.system("cd ~")
		time.sleep(0.1)
		print("Mounting volume to its own mount point located at /{}".format(volume_name))
		time.sleep(0.2)
		os.system("mount /dev/mapper/{} /{}/".format(volume_name, volume_name))
		clearterm()
		print("Success!\n Your new encrypted partition is unlocked and mounted at /{}. Keep this prompt open while you add/modify contents of the /{}.\n When you're finished writing/reading to the volume, safely unmount and lock the volume with enter.\n".format(volume_name, volume_name))
		input("Press enter to continue > ")
		clearterm()
		time.sleep(0.2)
		print("Saving volume info.\n")
		os.system("echo Device Name: {}, Volume Filename/Mount Point: {} > /var/lib/myluksvolume/{}info.txt".format(partition_name, volume_name, volume_name))
		print("Saved Volume's info to /var/lib/myluksolume/{}info.txt".format(volume_name))
		time.sleep(0.1)
		print("Unmounting device..\n")
		os.system("umount /{}".format(volume_name))
		time.sleep(0.1)
		os.system("cryptsetup luksClose /dev/mapper/{}".format(volume_name))
		time.sleep(0.1)
		input("You may now exit with enter and remove your device > ")
		sys.exit(0)
		
		
		
		
if __name__ == "__main__":
	main()
	

