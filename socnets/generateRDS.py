"""
Generates an RDS crawl.

"""

import flickr
import random

def main(MAXROUNDS, rdsConst):
	userid = "25833004@N07"#zabong
	nodeList = []
	numRounds = 0
	##while (numRound < MAXROUNDS):
	numRounds += 1
	userList = flickr.contacts_getPublicList(user_id=userid)
	##print len(userList)
	userTempList = list(userList) #creating a temp list to randomize
	lim = (int(0.3 * len(userList)))
	##print lim
	##print userTempList[:lim ]
	#for userEntry in userTempList: print userEntry.id
	nodeList.append(userTempList[:lim ] )
	##print len(nodeList)

if __name__ == "__main__":
	MAXROUNDS = 20 #number of rounds
	rdsConst = 0.3 #30% probability of activation of node 
	main(MAXROUNDS, rdsConst)
