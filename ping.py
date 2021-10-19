import os
import time
hostname = "cnn.com" #example

while 1:
	response = os.system("ping -n 1 " + hostname)
	
	#and then check the response...
	if response == 0:
		print (hostname,"is up!")
	else:
		print (hostname,"is down!")
	time.sleep(1)