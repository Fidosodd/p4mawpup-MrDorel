import time
import urllib
import re



def main ():
	
	sec = 500
	timeT = 0
    htmlfile = urllib.urlopen("http://www.nasdaq.com/symbol/aapl/real-time")
	htmltext = htmlfile.read()
	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	
	pattern = re.compile(regex)
	oldPrice = re.findall(pattern,htmltext)

	while timeT < sec:
	
		print "Checking the current price of apple stock. This may take a few a few minutes..."
		time.sleep(65)
		htmlfile = urllib.urlopen("http://www.nasdaq.com/symbol/aapl/real-time")
		htmltext = htmlfile.read()
		regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'	
		pattern = re.compile(regex)
		newPrice = re.findall(pattern,htmltext)
		time.sleep(5)
		print " The old price of apple stock is: "+str(oldPrice)
		
		if newPrice != oldPrice:
			print "---------------------Price changed!---------------------"
			print " The new Apple stock price is: "+str(newPrice)
			oldPrice = newPrice
		
		else:
			print " The Apple stock price has not changed."
			timeT +=1
			
		if timeT == sec:
			print "Ending process..."
			break
		else:
			print "Restarting...This may take a few seconds..."
		
		
	

main()

