"""
Generates random valid flickr IDs
- Generate a random 8 digit number
- add N00 to it
- check with API to see if it is a genuine ID
"""

import flickr, random

def main():
    idList = generateID()
    printList(idList)

def generateID():
    idList = []
    for i in range(20000):
        randNum = random.randint(10000000, 99999999)
        userID = "%s@N00"%randNum
        try:
            userList = flickr.contacts_getPublicList(user_id=userID)
            #if (userList):
            print ("%s exists... "%userID)
            idList.append(userID)
        except:
            print ("%s does not exist... "%userID)
    #print idList
    return(idList)

def printList(idList):
    fp = open("flickrIDList.txt", "a")
    for userID in idList:
        fp.write("%s\n"%(userID))
    fp.close()

if __name__ == "__main__":
    main()
