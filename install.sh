#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 3.0 | 2017

#***************************SETUP*************************************
echo "Home Automation System version 3.0"
echo "Davy Ragland | dragland@stanford.edu"

echo "Downloading..."
sudo apt-get update
sudo apt-get install vim -y
sudo apt-get install apache2 -y
sudo apt-get install git-core -y
sudo apt-get install sqlite3 -y
sudo apt-get install python-serial -y
sudo apt-get install python-rpi.gpio -y
sudo apt-get install speedtest-cli -y

echo "Installing..."
cd /home/pi
sudo git clone git://git.drogon.net/wiringPi
cd wiringPi
sudo ./build
cd /home/pi
sudo pip install cleverbot
sudo pip install xbee

echo "Updating..."
sudo apt-get update -y
sudo apt-get upgrade -y

#****************************MAIN*************************************
echo "Setting up..."
sudo chown -R -v pi /var/www
sudo rm -rf /var/www/html/*
sudo git clone https://github.com/dragland/Smart_Home.git temp
sudo mv temp/* /var/www/
sudo mv temp/.git /var/www/
sudo rm -rf temp
sudo a2enmod cgi
echo "enable_uart=1" | sudo tee -a /boot/config.txt
echo "dtparam=i2c1=on" | sudo tee -a /boot/config.txt
echo "dtparam=i2c_arm=on" | sudo tee -a /boot/config.txt
echo "i2c-dev" | sudo tee -a /etc/modules

echo "done! Restarting now..."
sudo shutdown -r now
