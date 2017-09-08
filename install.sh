#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

echo "Home Automation System version 3.0"
echo "Coded by Davy Ragland [dragland@stanford.edu]"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Downloading..."
echo "Vim"
echo "Apache2"
echo "Git-core"
echo "SQLite3"
echo "Python-rpi.gpio"
sudo apt-get update
sudo apt-get install vim -y
sudo apt-get install apache2 -y
sudo apt-get install git-core -y
sudo apt-get install sqlite3 -y
sudo apt-get install python-serial -y
sudo apt-get install python-rpi.gpio -y
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Installing..."
echo "WiringPi CGI library"
echo "Cleverbot API"
echo "Xbee API"
cd /home/pi
sudo git clone git://git.drogon.net/wiringPi
cd wiringPi
sudo ./build
cd /home/pi
sudo pip install cleverbot
sudo pip install xbee
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Updating..."
sudo apt-get update -y
sudo apt-get upgrade -y
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Setting up..."
sudo chown -R -v pi /var/www
sudo rm -rf /var/www/html/*
sudo git clone https://github.com/dragland/Smart_Home.git temp
sudo mv temp/* /var/www/
sudo mv temp/.git /var/www/
sudo rm -rf temp
echo "enable_uart=1" | sudo tee -a /boot/config.txt
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "done! Restarting now..."
sudo shutdown -r now
