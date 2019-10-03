#!/usr/bin/python3 

import os
import sys
import time
def main():
    while True:
        os.system("clear")
        os.system("cd ~")
        with open("luksdev.txt", "r") as fdev:
            devpart = fdev.read()
        with open("lukspartition.txt", "r") as fpart:
            luks_name = fpart.read()
            
        os.system("cryptsetup luksOpen /dev/{} {}".format(devpart, luks_name))
        time.sleep(0.1)
        os.system("mount /dev/mapper{} /{}/".format(luks_name, luks_name))
        os.system("rsync -av ~/field_data/ /{}/field_backups/")
        os.system("rm -r ~/field_data")
        os.system("mkdir ~/field_data")
        os.system("umount /{}".format(luks_name))
        os.system("cryptsetup luksClose /dev/mapper/{}".format(luks_name))
        time.sleep(0.1)
        print("Safe to remove external storage, field data backed up")
        time.sleep(2)
        sys.exit(1)
        
if __name__ == "__main__":
    main()
    
