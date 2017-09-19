# Smart Home:
### A Home Automation system for the Raspberry Pi written in Python and JavaScript
[click here for a demo](https://htmlpreview.github.io/?https://github.com/dragland/Smart_Home/blob/master/html/index.html)

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/screen.png "Smart_Home")

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/system.jpg "Electronics")

![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/PCB.png "Circuit Board")

# Features:
1. Frontend web interface that shows live sensor readings.
2. Frontend graphing utility to plot readings from SQL database.
3. Frontend voice controls for interacting with system. 
4. Backend Python SQL logging script.
5. Backend robust multithreaded architecture.
2. Temperature and Humidity readings from HIH6130 sensor.
2. CO2 readings from SenseAir S8 sensor.
3. Power consumption readings from XBEE Tweet-A-Watt sensor.
4. Door state readings from magnetic switch.
5. Raspberry Pi system vitals readings from Linux.
6. Remote control of Relay through web interface.
7. Remote control of RGB LED strip through web interface.

# Instalation:

```bash
cd /home/pi
curl "https://raw.githubusercontent.com/dragland/Smart_Home/master/install.sh" > install.sh
sudo chmod 755 install.sh
sudo ./install.sh
```

### You must manually setup the following:
##### Starting the script automatically:

```bash
sudo crontab -e
```

>@reboot /var/www/run.sh &

>0 12 * * * /sbin/shutdown -r now

##### Enabling CGI scripts:

```bash
sudo vim /etc/apache2/conf-available/serve-cgi-bin.conf
```

>ScriptAlias /cgi-bin/ /var/www/html/cgi-bin/

>&lt;Directory "/var/www/html/cgi-bin"&gt;

>	AddHandler cgi-script .py

>&lt;/Directory&gt;

# Schematics:
![alt text](https://raw.githubusercontent.com/dragland/Smart_Home/master/html/res/github/schematics.png "Schematics")

# Bill of Materials:
| Designator           | Part ID              |quantity |
| :---                 | :---                 | ---:    |
|                      | RPI3 MODEL B         | 1       |
|                      | P3 P4400             | 1       |
|                      | Tweet-a-Watt Kit     | 1       |
|                      |                      |         |
| C1                   | 478-1400-1-ND        | 1       |
| C2                   | 478-3351-1-ND        | 1       |
| C3                   | 478-1417-1-ND        | 1       |
| DOOR,RELAY           | WM1880CT-ND          | 2       |
| LEDS                 | WM1882CT-ND          | 1       |
| PCA9685              | 568-11925-1-ND       | 1       |
| R1,R2                | 541-220CCT-ND        | 2       |
| R3,R4,R5,R6,R7,R8,R9 | 541-10.0KCCT-ND      | 7       |
| 12V+                 | CP-102A-ND           | 1       |
| RPI3 GPIO            | 1568-1462-ND         | 1       |
| HIH6130              | 480-3651-1-ND        | 1       |
| PWR                  | 475-1410-1-ND        | 1       |
| LED                  | 160-2162-1-ND        | 1       |
| Q1,Q2,Q3             | SI7232DN-T1-GE3CT-ND | 3       |
| S8 CO2               | SenseAir S8          | 1       |
|                      |                      |         |
|                      | WM1847-ND            | 1       |
|                      | WM1845-ND            | 2       |
|                      | WM1839-ND            | 8       |
