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
print("Range = %s" % (RANGE))
print("<br>")

conn = sqlite3.connect("../archive.db")
curs = conn.cursor()
for row in curs.execute("SELECT * FROM data WHERE time >= datetime('now','-%i minutes')" % (int(RANGE))):
    print row
    print("<br>")
conn.close()