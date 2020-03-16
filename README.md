##Release: 0.1.0
##py-update-script

###Overview

This is a simple python script to update linux machines over ssh. It is configurable using a TOML file. 

###Instructions

1. Make sure python3 is installed
2. Look at hosts.example.toml and copy it to hosts.toml
3. Configure hosts.toml
4. Make sure host that is running script has publickey permissions to remote host with defined user
5. Make sure remote user has sudo permissions for running updates according to distro package manager
```
sudo visudo
```
```
root ALL=(ALL) ALL
#insert after root line and make sure to uncomment correct distro
#(user) ALL=(ALL) NOPASSWD: /usr/bin/pacman			#Arch
#(user) ALL=(ALL) NOPASSWD: /usr/bin/pacman,/usr/bin/yay	#Arch with yay package manager
#(user) ALL=(ALL) NOPASSWD: /usr/bin/yum,/bin/rpm		#CentOS
#(user) ALL=(ALL) NOPASSWD: /usr/bin/apt,/usr/bin/apt-get	#Debian
#(user) ALL=(ALL) NOPASSWD: /usr/bin/dnf,/bin/rpm		#Fedora
```
6. chmod +x 
7. (Optional)Automate using cron

