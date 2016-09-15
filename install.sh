#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

echo "Home Automation System version 2.0"
echo "Coded by Davy Ragland [dragland@stanford.edu]"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Downloading..."
echo "Apache2"
echo "Git-core"
echo "SQLite3"
echo "Python-rpi.gpio"
echo "Python-dev"
sudo apt-get update
sudo apt-get install apache2 -y
sudo apt-get install git-core -y
sudo apt-get install sqlite3 -y
sudo apt-get install python-rpi.gpio -y
sudo apt-get install build-essential python-dev -y

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Installing..."
echo "DHT22 temp & humidity sensor"
echo "WiringPi CGI library"
cd /home/pi
sudo git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install
cd /home/pi
sudo git clone git://git.drogon.net/wiringPi
cd wiringPi
sudo ./build
cd /home/pi
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Updating..."
sudo apt-get update
sudo apt-get upgrade
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "Setting up..."
sudo chown -R -v pi /var/www
sudo git clone https://github.com/dragland/Smart_Home.git temp
sudo mv temp/* /var/www/
sudo rm -rf temp
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
echo "done! Restarting now..."
sudo shutdown -r now