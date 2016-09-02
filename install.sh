#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

echo "Home Automation System version 2.0"
echo "Coded by Davy Ragland [dragland@stanford.edu]"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "TO DO"
echo "Setup static IP"

echo "Edit .bashrc"
echo "hostname -I"

echo "sudo crontab -e"
echo "@reboot /var/www/run.sh &"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo "downloading..."
echo "Apache2"
sudo apt-get update
sudo apt-get install apache2 -y
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
