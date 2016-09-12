# Smart_Home: 
###A Home Automation system for the Raspberry Pi writen in Python and Javascript

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/icons/screen_desktop.png "Smart_Home")

#Instalation:

```bash
cd /home/pi
curl "https://raw.githubusercontent.com/dragland/Smart_Home/master/install.sh" > install.sh
sudo chmod 755 install.sh
sudo ./install.sh
```

###You must manualy setup the folowing:
Set the IP adress to static:

>Look up tutorial for your version of Raspbian

Starting the script automatically:

```bash
sudo crontab -e
```

>@reboot /var/www/run.sh &

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