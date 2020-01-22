from similarity import getUserSim
import conf
N = conf.N
userSim = getUserSim()
# generate recommendation list
def getRecommendations(N,trainSet,userSim):
    pred = {}
    for user in trainSet.keys():
        pred.setdefault(user,{})
        interacted_items = trainSet[user].keys()
        average_u_rate = getAverageRating(user)
        userSimSum = 0
        simUser = sorted(userSim[user].items(),key = lambda x : x[1],reverse = True)[0:N]
        for n, sim in simUser:  
            average_n_rate = getAverageRating(n)
            userSimSum += sim
            for m, nrating in trainSet[n].items():  
                if m in interacted_items:  
                    continue  
                else:
                    pred[user].setdefault(m,0)
                    pred[user][m] += (sim * (nrating - average_n_rate))
        for m in pred[user].keys():  
            if userSimSum == 0:
                pred[user][m] = average_u_rate
            else:
                pred[user][m] = average_u_rate + (pred[user][m] / userSimSum)
    return pred
    
%%time
print ('generating...')
for N in range(4,40,4):
    pred = getRecommendations(20,trainSet,userSim)
    mae = getMAE(testSet,pred,N)
    rmse = getRMSE(testSet,pred,N)
    accuracy = getAccuracy(pred,N)
    diversity = getDiversity(pred,N)
    coverage = getCoverage(pred,N)
    print ('when N= %d accuray：MAE=%f, RMSE=%f, Accuracy=%f, Diversity=%f, Coverage=%f'%(N,mae,rmse,accuracy,diversity,coverage))
    recall = getRecall(testSet,pred,N)
    precision = getPrecision(testSet,pred,N)
    print ('Recall=%f, Precision=%f'%(recall,precision))
print('----end----') 
