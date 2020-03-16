#!/usr/bin/env  python3

import subprocess
import toml

debug = 0

host_file = "hosts.toml"

def file_host_read(host_file,debug):
    host_config = toml.load(host_file)
    if (debug == 1):
        print (host_config, "\n")
    for hosts in host_config.items():
        if (debug == 1):
            print ("\n",hosts,"\n")
        else:
            print ("\n", hosts[0],"\n")
        ip_address= hosts[1]["ip_address"]
        os= hosts[1]["os"]
        user= hosts[1]["user"]
        port= hosts[1]["port"]
        commands(ip_address,port,os,user)
def commands(ip_address, port, os, user):
    if (os == "arch"):
        subprocess.run("ssh -t -p" + port + " " + user + "@" + ip_address + ' "yes | sudo pacman -Syyu && yes | sudo pacman -c"', shell=True)
    if (os == "arch1"):
        subprocess.run("ssh -t -p" + port + " " + user + "@" + ip_address + ' "yes | sudo yay -Syyu && yes | sudo yay -c"', shell=True) 
    elif (os == "centos"):
        subprocess.run("ssh -t -p" + port + " " + user + "@" + ip_address + ' "sudo yum update -y"', shell=True)
    elif (os == "debian"):
        subprocess.run("ssh -t -p" + port + " " + user + "@" + ip_address + ' " sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get dist-upgrade -y && sudo apt-get autoremove -y"', shell=True)
    elif (os == "fedora"):
        subprocess.run("ssh -t -p" + port + " " + user + "@" + ip_address + ' " sudo dnf update -y"', shell=True)

file_host_read(host_file,debug)
print ("\nUpdate script complete")
