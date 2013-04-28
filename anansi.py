#!/usr/bin/env python

# Requests is a simple fucking http module
import requests
# BeautifulSoup parses broken XML
# It's glorious
from bs4 import BeautifulSoup
# Argparse is for command line usage
import argparse
# Might be overkill to check versions
# b/c the 2to3 tool would take care of it
try:
	import ConfigParser as cp #Python 2
except ImportError:
	import configparser as cp #Python 3
import re

class SQLiTest(object):
	def __init__(self, page):
		'''Page is HTML, as string'''
		self.page = page
		print page
		
	def _find_input(self):
		ind = 0
		while ind != -1:
			ind = self.page.find("input")
			
	def _in_band(self):
		pass
		
	def _out_band(self):
		pass
		
	def _blind(self):
		# Tries to deduce database type
		pass
		
	def execute(self):
		pass

def main():
	config = cp.ConfigParser()
	config.read('SQLi/sqli.config')
	print config.get('SQL','rooting')
	
if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-w",help="The web address")
	args = parser.parse_args()
	s_page = requests.get( args.w )
	s = SQLiTest( s_page.text )
	main()