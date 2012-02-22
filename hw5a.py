#diff

#First install BeautifulSoup: pip install BeautifulSoup
import urllib2
import time
import csv
from BeautifulSoup import BeautifulSoup

#Initialize arrays to print to CSV
urlList = []
pageTitleList = []
isPostList = []
publishDateList = []
authorList = []
commentCountList = []


def readPage(pageLinks,i):
    #Open a webpage
    print pageLinks[i]
    webpage = urllib2.urlopen(pageLinks[i])


    #Parse it
    soup = BeautifulSoup(webpage.read())

    for link in soup('a'):
        tempLink = str(link.get('href'))
        if tempLink.find('http://babesofnpr.tumblr.com/') and tempLink not in pageLinks:
            pageLinks.append(str(link['href']))

    #Checks to determine if URL is a page or a post
    if len(soup.findAll('nav', {'id':"stat-navigation"}))>=1:
    	ispost = 0
    else:
    	ispost = 1
    isPostList.append(ispost)
    urlList.append(pageLinks[i])

    if ispost==1:

        pageurl = (pageLinks[i])
        titleIndex = pageurl.rfind("/") + 1
        endIndex = pageurl.find("#") -1 
        title = pageurl[titleIndex:endIndex]
        title = title.replace("-"," ")

        pageTitleList.append(title)
        

        for header in soup(['time']):														#Loop through all the time tags
    	        date = header.get('datetime')					
    	   	publishDateList.append(date)
    		

        for notes in soup(['em']):
            x = notes.string


    else:

        pageTitleList.append("NA")
        authorList.append("NA")
        publishDateList.append("NA")
        commentCountList.append("NA")
    
    #except:
        #print "Error"

    i = i+1
    print str(i) + " of " + str(len(pageLinks))

    time.sleep(1)
    
    if i<len(pageLinks):
        readPage(pageLinks,i)
    else:

        csvWriter = csv.writer(open('blog.csv','wb'))
        for a in range(0,len(urlList)):
            csvWriter.writerow([urlList[a],pageTitleList[a],authorList[a],publishDateList[a],commentCountList[a],isPostList[a]])


readPage(["http://babesofnpr.tumblr.com"],0)

