# Smart_Home: 
###A Home Automation system for the Raspberry Pi written in Python and JavaScript
[click here for a demo](https://htmlpreview.github.io/?https://github.com/dragland/Smart_Home/blob/master/html/index.html)

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/screen.png "Smart_Home")

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/system.jpg "Electronics")

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/hologram.png "Hologram")

#Instalation:

```bash
cd /home/pi
curl "https://raw.githubusercontent.com/dragland/Smart_Home/master/install.sh" > install.sh
sudo chmod 755 install.sh
sudo ./install.sh
```

###You must manualy setup the folowing:
Set the IP adress to static & enabling I2C:

```bash
sudo raspi-config
```

>Look up tutorial for your version of Raspbian

Starting the script automatically:

```bash
sudo crontab -e
```

>@reboot /var/www/run.sh &

>0 12 * * * /sbin/shutdown -r now

Enabeling I2C:

```bash
sudo vi /boot/config.txt
```

>dtparam=i2c1=on

>dtparam=i2c_arm=on

```bash
sudo vi /etc/modules
```

>i2c-dev

Enabeling CGI scripts:

```bash
sudo a2enmod cgi
```

```bash
sudo vi /etc/apache2/conf-available/serve-cgi-bin.conf 
```

>ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/

>&lt;Directory "/var/www/html/cgi-bin"&gt;

>	AddHandler cgi-script .py

>&lt;/Directory&gt;

#Wiring:
![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/wiring.png "Smart_Home")