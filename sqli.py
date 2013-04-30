from bs4 import BeautifulSoup

class Fuzzer(object):
	def __init__(self):
		pass

class SQLiTest(object):
	def __init__( self, page ):
		'''Page is HTML, as string'''
		self.page = BeautifulSoup( page )
		self.inputs = self._find_input( )
		print self.inputs
		
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
		
if __name__=="__main__":
	import requests
	s_page = requests.get( "http://www.google.com" )
	s = SQLiTest( s_page.text )