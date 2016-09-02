#!/usr/bin/env bash
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

echo "var posters =" > ../html/js/posters.js
echo "[" >> ../html/js/posters.js
(IFS='
'
for x in `ls ../html/res/posters $1`; 
	do 
		printf '"'
		printf $x
		printf '",\n'; 
done >> ../html/js/posters.js) 
echo "];" >> ../html/js/posters.js 