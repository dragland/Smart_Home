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
curs.execute("SELECT * FROM data WHERE time >= time('now','-%i minutes')" % (int(RANGE))):
rows = curs.fetchall()
conn.close()

for row in rows:
    print row
    print("<br>")