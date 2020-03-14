#!/usr/bin/python
# -*- coding utf-8 -*-
import sys
import requests
import re
from bs4 import BeautifulSoup

provider={
		'tivusat' : ["pack-tivusat","183D@000000@00005411,183E@000000@00005411","Tivusat"],
		'skyit' : ["pack-skyitalia","09cd@000000","SkyIT"],
		'ncplus' : ["pack-ncplus","0B01@000000,0100@000068,1884@000068","Nc Plus"],
		'srg' : ["pack-ssr","0500@23800@40810@050800","SRG"],
		'polsat' : ["pack-polsat","1803@000000","Polsat"],
	}

def help():
	for prov in provider.keys():
		print prov

if len(sys.argv) != 2:
	help()
	exit()
try:
   provider[sys.argv[1]]
except KeyError:
	help()
	exit()


url="https://it.kingofsat.net/%s.php" % (provider[sys.argv[1]][0])
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

channels = [tag.get_text() for tag in soup.find_all("td", class_ = "ch")]
sids=[tag.get_text() for tag in soup.find_all("td", class_ = "s")]

for s,c in zip(sids,channels):
	#1134:0B01@000000,0100@000068,1884@000068|Trace Urban|||NC+ (Conax
	if not re.match('^SID',s):
		sid=hex(int(s.strip())).split('x')[-1].zfill(4)
		print "%s:%s|%s|||%s" % (sid,provider[sys.argv[1]][1],c.strip().encode("ascii", "ignore"),provider[sys.argv[1]][2])
