
"""Wrapper class to store the page url and the occurence of the search string in the html of this page"""

class ResultPage():
	def __init__(self,pageurl,count):
		self.url = pageurl
		self.countString  = count
	
	def return_Frequency(self):
		return self.countString
	
	def return_url(self):
		return self.url

