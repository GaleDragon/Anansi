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

class SQLiTest(object):
	def __init__( self, page ):
		'''Page is HTML, as string'''
		self.page = BeautifulSoup( page )
		self.inputs = self._find_input( )
		
	def _find_input( self ):
		matches = self.page.find_all('input')
		varNames = dict()
		for m in matches:
			if m.has_key('name'):
				try:
					dummy = m['type']
				except KeyError:
					varNames[m['name']] = m["value"]
		return varNames
		
				
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
	#print config.get('SQL','rooting')
	
if __name__=="__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-w",help="The web address")
	args = parser.parse_args()
	s_page = requests.post( args.w )
	print BeautifulSoup(s_page.text).prettify()
	s = SQLiTest( s_page.text )
	main()