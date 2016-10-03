import random, numpy, pandas as pd
from sklearn.cross_validation import KFold
import bayes
import utility

Data = utility.Data
#print(Data['mv'].head())
#print(Data['ft'].head())

def err_cnt(train, test):
    length = len(train)
    res = 0
    mae = 0
    acc = 0
    for i in range(0, length):
        d = int(train[i])-int(test[i])
        mae += abs(d)
        if abs(d) <= 1:
            res += 1
            if d == 0:
                acc += 1
    #print(length-res)
    percantile = (length-res)/length*100
    #print(percantile)
    total = 0
    for a in train:
        total += a
    data = {}
    data['mae'] = mae/total
    data['percantile'] = percantile
    data['accurate'] = acc
    return data

f = open('bayes_log.txt', 'w')
k = input('Enter the number of sets: ')
k = int(k)
def k_cross_validation(Data, dataset, k, algo):
    data_len = len(Data[dataset])
    #print(data_len) #
    #data = data.sample(frac=1).reset_index(drop=True) # randomizes dataset and reset_index renumbers them from 0
    #print(tmp.head())
    kf = KFold(data_len, k, shuffle=True, random_state=None)
    tot = 0
    test_size = 0
    not_close = 0
    tot_acc = 0
    for train_idx, test_idx in kf:
        #print(train_idx, test_idx)
        train_data = Data['mv'].ix[train_idx]
        #print(train_data)
        test_data = Data['mv'].ix[test_idx]
        test_size = len(test_data)
        #pass
        predictions = algo.predict(train_data=train_data, test_data=test_data)
        #print(predictions)
        error = err_cnt(test_data['rating'].values, predictions)
        tot += error['mae']
        #print(error, tot)
        not_close += error['percantile']
        tot_acc += error['accurate']
    tot /= k
    tot *= 100
    not_close /= k
    tot_acc /= data_len
    tot_acc *= 100
    f.write('Mean Absolute Error in '+str(dataset)+' is '+str(tot)+'%'+'\n')
    f.write('Number of predictions with difference more than 1 is '+str(not_close)+'%' + ' in '+str(dataset)+'\n')
    f.write('Number of accurate predictions is '+str(tot_acc)+'%'+'\n\n')
    f.write('Number of sets: '+str(k))
    #res = tot/test_size*100
    return tot*100
#kf = KFold(data_len, 5, True, None)
#kf = k_cross_validation(Data, 'mv', 5)
#train_data = []
#print(Data['mv'])
#print(kf)
mve = k_cross_validation(Data, 'mv', k, bayes)
#print('Mean Absolute error in Movielens Site:' tot)
fte = k_cross_validation(Data, 'ft', k, bayes)
cde = k_cross_validation(Data, 'cd', k, bayes)
f.close()
