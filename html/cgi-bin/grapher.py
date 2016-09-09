#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import smartHomeCGI
import sqlite3
import datetime

#*********************************************************************
#                            MAIN
#*********************************************************************
smartHomeCGI.header("HTML")

RANGE = smartHomeCGI.get_value("RANGE")
VALUE = smartHomeCGI.get_value("VALUE")

conn = sqlite3.connect("../archive.db")
curs = conn.cursor()
curs.execute("SELECT * FROM data WHERE timestamp >= datetime('%s','-%i %s')" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), int(VALUE), RANGE))
rows = curs.fetchall()
conn.close()

for row in rows:
    row = str(row)[3:-1].replace("'","")
    print("<br>")