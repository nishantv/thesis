"""
Generates an RW crawl.

"""
import flickr 
import random

def main():
    MAXHOPS = 20 #number of hops
    rdsConst = 0.3 #30% probability of activation of node 
    userID = "25833004@N07"#zabong
    randomWalk(userID, MAXHOPS)

def generateRDS(MAXHOPS, rdsConst):
    pass

def randomWalk(userID, MAXHOPS):
    nodeList = []
    nodeSet = set()
    numRounds = 0
    for i in range(MAXHOPS):
        nodeList.append(userID)
        nodeSet.add(userID)
        userList = flickr.contacts_getPublicList(user_id=userID)
        if(userList):
            randID = random.randint(1, len(userList))   #get a random number 
            user = userList[randID-1]       #get the user indexed by that number
            try:
                userID = str(user.id)
                print randID, userID
            except:
                pass
        else: 
            pass
            #fix for checking local minima...
          
        if ( len(nodeList) - len(nodeSet) > int(MAXHOPS * 0.1) ):
            print ("nodeList: %s, nodeSet: %s, returning..."%(len(nodeList), len(nodeSet)))
            print nodeList
            return
    print nodeList        

if __name__ == "__main__":
    main()
