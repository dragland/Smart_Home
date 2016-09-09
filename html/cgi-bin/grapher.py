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
curs.execute("SELECT * FROM data WHERE timestamp >= datetime('now','-%i %s')" % (int(VALUE), RANGE))
rows = curs.fetchall()
conn.close()

for row in rows:
    print row
    print("<br>")