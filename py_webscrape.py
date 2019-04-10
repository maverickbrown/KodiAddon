import re
import requests # pip install requests to install. i have not used this currently on this code.
import urllib2
from bs4 import BeautifulSoup

#fetch the URL
targeturl = 'http://sport5.live/category/nba/'

#Add the UserAgent string since the link does not allow to be fetch if using python user agent string
req = urllib2.Request(targeturl, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
#req.add_header('Accept-Encoding', 'utf-8')

#try catch block - exit if the status code is other than HTTP 200
try:
	response = urllib2.urlopen(req).read()
	#print response.get_code()

	#Parse the webpage 
	html_soup = BeautifulSoup(response, 'html.parser')
	type(html_soup)
	#print html_soup

except HTTPError as e:
	print "Error retrieving the URL..."
	print 'Error Code: ', e.code


#this outputs the title and the link but needs some cleaning up
# using BeautifulSoup to parse through the webpage
game_containers = html_soup.find_all('h3', class_='g1-delta g1-delta-1st entry-title')
print (type(game_containers))

#get the number of games/links
num_of_games = (len(game_containers))

#check if there are any games 
if num_of_games == 0:
		print 'There are no games for tonight...'
else:
		print num_of_games

#print game_containers
print '*************'
print ""

#iterate throug the beautifulsoup result to get the text as well as the href link
game_title = []
game_link = []
for tag in game_containers:
	#print tag
	#print (tag.getText())
	#will get the contents
	#print tag.contents
		
	game_title.append(tag.getText())
	game_link.append(tag.find('a', href=True)['href'])

	#print tag.find('a', href=True)['href']

print game_link

print game_title


'''
With the above script it was able to extract text which is what team are playing and their link.
Next step:
parse the actual game link and get the M3U file name from the html source.

Once this is done:
Look at Kodi Video Addon how to:



'''