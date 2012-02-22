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
    webpage = urllib2.urlopen(pageLinks[i])
    #Parse it
    soup = BeautifulSoup(webpage.read())
    try:
        #Adds all links to stuffwhitepeoplelike.com links on the page to an array (no duplicates)
        for link in soup('a'):
            tempLink = str(link.get('href'))
            if tempLink.find('stuffwhitepeoplelike.com')>=0 and tempLink not in pageLinks and tempLink.find('#')<0 and tempLink.find('/tag/')<0 and tempLink.find('/author/')<0 and tempLink.find('/category/')<0 and tempLink.find('?')<0:
                pageLinks.append(str(link['href']))

        #Checks to determine if URL is a page or a post
        if len(soup.findAll('div', {'class':"posttitle"})) == 1 and "Older Posts" not in str(soup) and 'pagetitle">Archive for' not in str(soup):
        	ispost = 1
        else:
        	ispost = 0
        isPostList.append(ispost)
        urlList.append(pageLinks[i])

        if ispost==1:


            for header in soup(['a']):                                                      #Loop through all the links
                if header.parent.parent.name == "div":                                      #Check to see if its nested in a div
                    if header.parent.name == "h2":                                          #Check to see that its nested in h2
                        if str(header.parent.parent['class']) == "posttitle":   			#Check to see parent div is of class posttitle
                            title = str(header.string)                                      #Save the title as a string
                            title = title.replace("&nbsp;", " ")                            #Replace &nbsp; with a space
                            title = title.replace("&#8217;", "'")                           #Replace &#8217 with an apostrophe
                            pageTitleList.append(title)					                    #Print the title


            for header in soup(['p']):														#Loop through all the p tags
        	    if header.get('class') == "post-info":						
        	    	headerstring = str(header)												#Store the data in a string
        	    	datetemp = headerstring[headerstring.find('post-info">'):headerstring.find("by")]	#Get substring beginning with postmetadata"> and ending with by
        	    	date = datetemp[datetemp.find('>')+1:]									#Get substring that is just the data
        	    	authortemp = headerstring[headerstring.find('author">'):headerstring.find("</a>")]		#Get substring beginning with author"> and ending with </a>
        	    	author = authortemp[authortemp.find('>')+1:]							#Get substring that is just the author name
        	    	authorList.append(author)
        	    	publishDateList.append(date)
        		

            test = str(soup)
            if test.find('<p>Sorry, the comment form is closed at this time.</p>') >= 0:
            	commentCountList.append("Comments Closed")
            else:
                if test.find('<p>No comments yet.</p>') >= 0:
                    commentCountList.append(0)
                else:
        	        for ptag in soup(['p']):
        	            if ptag.get('class') == "postmetadata":
        	                ptagString = str(ptag)
        	                commentstemp = ptagString[ptagString.find('| '):ptagString.find(" Comments")]
        	                comments = commentstemp[commentstemp.find('| ')+2:]
        	                commentCountList.append(comments)

        else:

            pageTitleList.append("NA")
            authorList.append("NA")
            publishDateList.append("NA")
            commentCountList.append("NA")
        
    except:
        print "Error"

    i = i+1
    print str(i) + " of " + str(len(pageLinks))

    time.sleep(1)
    
    if i<len(pageLinks):
        readPage(pageLinks,i)
    else:
        csvWriter = csv.writer(open('times.csv','wb'))
        for a in range(0,len(urlList)):
            csvWriter.writerow([urlList[a],pageTitleList[a],authorList[a],publishDateList[a],commentCountList[a],isPostList[a]])


readPage(["http://stuffwhitepeoplelike.com"],0)

