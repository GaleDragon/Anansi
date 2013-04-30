#!/usr/bin/env python

# Requests is a simple fucking http module
import requests
# BeautifulSoup parses broken XML
# It's glorious
from sqli import SQLiTest
# Argparse is for command line usage
import argparse
# Might be overkill to check versions
# b/c the 2to3 tool would take care of it
try:
	import ConfigParser as cp #Python 2
except ImportError:
	import configparser as cp #Python 3

def main():
	config = cp.ConfigParser()
	config.read('SQLi/sqli.config')
	#print config.get('SQL','rooting')
	
if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-w",help="The web address")
	args = parser.parse_args()
	s_page = requests.post( args.w )
	s = SQLiTest( s_page.text )
	main()