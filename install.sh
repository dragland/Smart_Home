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
sqlite3 archive.db
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "TO DO"
echo "Setup static IP"

echo "Edit .bashrc"
echo "hostname -I"

echo "sudo crontab -e"
echo "@reboot /var/www/run.sh &"

echo "sudo a2enmod cgi"
echo "Edit /etc/apache2/conf-available/serve-cgi-bin.conf"
echo "ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/"
echo "<Directory "/var/www/html/cgi-bin">"
echo "	AddHandler cgi-script .py"
echo "</Directory>"

echo "sqlite3"
echo "BEGIN;"
echo "CREATE TABLE data (date DATE, time TIME, temp_f NUMERIC, rh NUMERIC, door NUMERIC, lights_red NUMERIC, lights_green NUMERIC, lights_blue NUMERIC, fan NUMERIC);"
echo "COMMIT;"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	
echo "done! Restarting now..."
sudo shutdown -r now
