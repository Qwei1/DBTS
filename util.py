
# get all users id in trust file 
def getTrustNetworkUsers(df_trust):
    trustUsers = list(set(df_trust['user_u']))
    return trustUsers
    
# get all user id
def getUsers(df_rating):
    userSet = list(set(df_rating['user_id']))
    return userSet
# get all items id

def getItems(df_rating):
    itemSet = list(set(df_rating['item_id']))
    return itemSet
    
# bulid trust user graph like: {user_id : [trusted users]}
def getTrustGraph(df_trust, trustUsers):
    trustGraph = { user : [user_v for user_v in set(df_trust[df_trust['user_u'] == user]['user_v'])] for user in trustUsers }
    return trustGraph
    
# the average value of one user  
def getAverageRating(user):  
    average = (sum(trainSet[user].values())*1.0) / len(trainSet[user].keys())  
    return average
    
# the average value of one item 
def getAverageItemRating(movieRating,itemid): 
    sumRating = 0.0
    countRating = 0
    for n in movieRating.keys():
        if n != itemid: continue
        for x in range(len(movieRating[n])):
            sumRating += movieRating[n][x]
            countRating +=1
    countRating = countRating if(countRating != 0) else 1
    return sumRating/countRating
    
# compute item popilarty
def itempopulary(train_data):
    IP = dict()
    itemList = [line[1] for line in train_data]
    for i in set(itemList):
        IP[i] = itemList.count(i)
    return IP
