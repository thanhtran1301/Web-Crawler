from linkfinder import LinkFinder
from page import ResultPage
"""add the links got from a current web page to the pages to visit"""
def addlink(visited_links,pages_to_visit,links):
	for i in range(len(links)):
		if links[i] in visited_links:
			continue;
		else:
			pages_to_visit.append(links[i])
		
"""counte the occurence of a substring in a string"""
def count_substring(main_string,sub_string):
	count = 0
	for i in range(len(sub_string)):
		count += main_string.count(sub_string[i])
	return count

"""create a report of the results"""
def print_report(resulted_pages):
	for i in range(3):
		print("*********************************************************")
	print("The following list contains the resulted web pages along with the occurrence of the search string in them: ")
	#sort the list of pages based on the occurence of the search string
	resulted_pages.sort(key=lambda x: x.return_Frequency(), reverse=True)

	for i in range(len(resulted_pages)):
		print(resulted_pages[i].return_url(), resulted_pages[i].return_Frequency())


"""This method is use to craw websites in a breadth first search mechanism"""
def web_crawler(feed_url, search_list, max_depth):
	# At a current level, examine all the page in the parent_pages
	# Add all the unvisted href links to the children_pages
	# Use the visited_links to avoid infinite loop
	depth_level = 0
	resulted_pages = []
	visited_links = []
	parent_pages = [feed_url]
	children_pages = []

	while parent_pages != [] and depth_level <= max_depth:
		for i in range(len(parent_pages)):
			visited_links.append(parent_pages[i])
		
			try:
				# parse a given page to get the html string and the href links
				parser = LinkFinder(parent_pages[i])
				data,links = parser.getLinks()
				print("Checking", parent_pages[i])
				# add href links to the children_pages
				addlink(visited_links,children_pages,links)
				# count the occurence of the search string in the data

				count_string = count_substring(data, search_list)
				if(count_string != 0):
					result_page = ResultPage(parent_pages[i],count_string)
					resulted_pages.append(result_page)
			except:
				continue

		depth_level = depth_level + 1
		parent_pages = children_pages
	# print the report
	print_report(resulted_pages)


