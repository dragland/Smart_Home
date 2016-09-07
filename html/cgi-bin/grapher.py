#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import relayCGI

#*********************************************************************
#                            MAIN
#*********************************************************************
relayCGI.header("HTML")
RANGE = relayCGI.get_value("RANGE")
print("Range = %s" % (RANGE))

conn = sqlite3.connect("../archive.db")
curs = conn.cursor()
for row in curs.execute("SELECT * FROM data"):
    print row
conn.close()