#!/usr/bin/python3

import os
import sys
import time
def close(vaultname):
	time.sleep(0.2)
	os.system("clear")
	isclose = str(input("Type 'close' to properly lock and remove the device"))
	if isclose == "close":
		print("Unmounting...\n")
		time.sleep(0.4)
		os.system("umount /{}".format(vaultname))
		os.system("cryptsetup luksClose /dev/mapper/{}".format(vaultname))
		time.sleep(0.2)
		print("Your encrypted volume is locked, unmounted, and safe to remove from the system!.\n")
		input("Press enter to exit...")
		sys.exit(1)
	else:
		input("Error, use 'close' to finish the script")
		close(vaultname)

def main():
    while True: 
        os.system("clear")
        os.system("mkdir /var/lib/myluksvolume")
        os.system("clear")
        time.sleep(0.5)

        print("Run this script as a super user!\n (execute 'sudo su' first)\n")
        input("Is the USB device containing the luks partition connected?")
        os.system("clear")
        os.system("cat /var/lib/myluksvolume/defaultinfo.txt")
        devpart = str(input("What's the filename of the device partition containing the luks volume? > "))
        vaultname = str(input("What's the name of the encrypted container? ('Vault') > "))
        time.sleep(0.1)
        print("Saving .txt with volume's arguments..\n")
        os.system("echo device partition: {}, luks container directory name: {} > /var/lib/myluksvolume/defaultinfo.txt".format(devpart, vaultname))
        time.sleep(0.3)
        input("saved to /var/lib/myluksvolume/defaultinfo.txt ")
        time.sleep(0.1)
        print("Unlocking the luks partition...\n")
        os.system("cryptsetup luksOpen /dev/{} {}".format(devpart, vaultname))
        time.sleep(0.3)
        input("Press enter to continue...\n")
        print("Mounting the luks partition to it's affiliated directory...\n")
        os.system("cd ~")
        os.system("mount /dev/mapper/{} /{}/".format(vaultname, vaultname))

        time.sleep(0.1)
        print("You may now modify and/or read contents of the encrypted volume from the directory '/{}'.\n Do not remove the USB device or turn off the system.\n When you are finished working with your files, close any processes using or interacting with '{}'\n Only press enter when you are ready to close the volume.\n".format(vaultname, vaultname))
        time.sleep(3)
        close(vaultname)
        

if __name__ == "__main__":
    main()
    
