#!/usr/bin/python
# -*- coding utf-8 -*-
import sys
import requests
import re
from bs4 import BeautifulSoup



url="https://it.kingofsat.net/pos-13.0E.php"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

channels = [tag.get_text() for tag in soup.find_all("td", class_ = "ch")]
sids=[tag.get_text() for tag in soup.find_all("td", class_ = "s")]
gen=[tag.get_text() for tag in soup.find_all("td", class_ = "genre")]
cr=[tag.get_text() for tag in soup.find_all("td", class_ = "cr")]
bq=[tag.get_text() for tag in soup.find_all("td", class_ = "bq")]
for s,c,g,caid,bouquet in zip(sids,channels,gen,cr,bq):
	#1134:0B01@000000,0100@000068,1884@000068|Trace Urban|||NC+ (Conax
	if not re.match('^SID',s) and bouquet=="Telespazio" and 'Viaccess 5' in caid:
		sid=hex(int(s.strip())).split('x')[-1].zfill(4)
		#print "%s:%s|%s|||%s" % (sid,provider[sys.argv[1]][1],c.strip().encode("ascii", "ignore"),provider[sys.argv[1]][2])
		print "%s:0500@050F00|%s|||XXX" % (sid,c.strip().encode("ascii", "ignore"))
