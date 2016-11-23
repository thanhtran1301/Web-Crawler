from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse

"""LinkFinder inherits from HTMLParser and add one more funtionality"""
class LinkFinder(HTMLParser):
	def __init__(self,url):
		super().__init__()
		self.baseurl = url
		self.links = []
	# Handle all the elements that start with the 'a' tags
	# if it's a href then add that link to the list of links
	def handle_starttag(self,tag,attrs):
		if (tag == 'a'):
			for(attribute,value) in attrs:
				if(attribute == 'href'):
					url = parse.urljoin(self.baseurl,value)

					self.links.append(url)
					
	# Parse the html and feed it so that the handle_starttag can be invoked				
	def getLinks(self):
		response = urlopen(self.baseurl)

		if 'text/html' in response.getheader('Content-type'):
			htmlBytes = response.read()
			htmlString = htmlBytes.decode("utf-8")
			self.feed(htmlString)
			return htmlString, self.links
		else:
			return "",[]



