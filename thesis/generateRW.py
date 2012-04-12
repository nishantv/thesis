"""
Generates an RW crawl.

"""
import flickr 
import random

def main():
    MAXHOPS = 200 #number of hops    
    startRW(MAXHOPS)
    startRDS(MAXHOPS)

def startRDS(MAXHOPS):
    rdsConst = 0.3 #30% probability of activation of node 
    pass

def generateRDS(MAXHOPS, rdsConst):
    pass

def startRW(MAXHOPS):
    fp = open("smallFlickrList.txt")
    for line in fp: 
        userID = line.rstrip("\n")
        print ("Current userID: %s"%userID)
        ##userList = flickr.contacts_getPublicList(user_id=userID)
        ##if userList: print type(userList), userList, len(userList)
        ##else: print "no userList for %s"%userID
        randomWalk(userID, MAXHOPS)    
        #userID = "25833004@N07"#zabong
    
def randomWalk(userID, MAXHOPS):
    nodeDict = {}
    nodeList = []
    nodeSet = set()
    numRounds = 0
    for i in range(MAXHOPS):
        #print nodeDict
        nodeList.append(userID)
        nodeSet.add(userID)
        if userID in nodeDict:
            userList = nodeDict[userID] 
        else:
            userList = flickr.contacts_getPublicList(user_id=userID)
        if(isinstance(userList, list)): #making sure the node has contacts
            #print type(userList), userList, len(userList)
            #newList = [str(userID.id) for userID in userList]
            #newList = userList
            #print newList
            nodeDict[userID] = userList
            randID = random.randint(0, len(userList))   #get a random number 
            user = userList[randID-1]       #get the user indexed by that number
            userID = str(user.id)
            print "  -%s"%userID
            """
            try:
                userID = str(user.id)
                print randID, userID
            except:
                pass
            """
        else: 
            pass

        #fix for checking local minima...
        if ( len(nodeList) - len(nodeSet) > int(MAXHOPS * 0.1) ):
            print ("nodeList: %s, nodeSet: %s, returning..."%(len(nodeList), len(nodeSet)))
            print nodeList
            return
    print nodeList#, nodeDict        

if __name__ == "__main__":
    main()
