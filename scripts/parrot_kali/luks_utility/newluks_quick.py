#!/usr/bin/python3 

import os
import sys
import time

def clearterm():
    os.system("clear")
    
def main():
    while True:
        clearterm()
        luksdev = str(input("Filename associated with external storage device =>"))
        luks_name = str(input("Name for encrypted container and mount point =>"))
        with open("luksdev.txt", "w+") as fdev:
            fdev.write("luksdev.txt", luksdev)
            
        input("Press enter")
        
        with open("lukspartition.txt", "w+") as fpart:
            fpart.write("lukspartition.txt", luks_name)
            
        input("Press enter")
        
        clearterm()
        os.system("parted --script /dev/{} mktable msdos".format(luksdev))
        clearterm()
        partition_num = str(input("Partition number (1-4) => "))
        start_part = str(input("Starting sector for partition =>"))
        end_part = str(input("Ending sector of partition =>"))
        os.system("parted --script /dev/{} mkpart primary ext4 {} {}".format(start_part, end_part))
        luksdevname = str(luksdev + "{}".format(partition_num))
        clearterm()
        os.system("cryptsetup luksFormat /dev/{}".format(luksdevname))
        clearterm()
        mount_vault = luks_name
        os.system("cryptsetup luksOpen /dev/{} {}".format(luksdevname, mount_vault))
        os.system("cd /dev/mapper/")
        os.system("mkfs.ext4 /dev/mapper/{}".format(mount_vault))
        os.system("mkdir /{}".format(mount_vault))
        os.system("cd ~")
        clearterm()
        os.system("mount /dev/mapper/{} /{}/".format(mount_vault, mount_vault))
        print("luks container successfully created\n")
        print("Volume is unlocked and opened, you're free to modify contents\n")
        input("Press enter when finished to close and lock the volume =>")
        clearterm()
        os.system("umount /{}".format(mount_vault))
        os.system("cryptsetup luksClose /dev/mapper/{}".format(mount_vault))
        input("Press enter to exit")
        sys.exit(0)
        
if __name__ == "__main__":
    main()
