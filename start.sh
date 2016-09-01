#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

echo "var posters =" > js/posters.js
echo "[" >> js/posters.js
(IFS='
'
for x in `ls res/posters $1`; 
	do 
		printf '"'
		printf $x
		printf '",\n'; 
done >> js/posters.js) 
echo "];" >> js/posters.js 