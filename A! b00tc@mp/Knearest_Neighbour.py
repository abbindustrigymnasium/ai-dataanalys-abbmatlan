import numpy as np 
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import style
import warnings 
from collections import Counter
style.use("fivethirtyeight")

                                #GRUNDER

                    # def eucdist(goldplot,plot):
                    #     euc = sqrt((plot[0] - oldplot[0])**2 + (plot[1] - goldplot[1])**2)
                    #     print(euc)
                    #     plt.scatter(plot[0],plot[1], s = 100)

                    # plot = [1,3]
                    # goldplot = [2,5]
                    # plt.scatter(goldplot[0],goldplot[1], s = 150)

                    # eucdist(goldplot,plot)
                    # plot2 = [4,7]
                    # eucdist(goldplot,plot2)

                    # eucdist(goldplot,goldplot)
                    # plt.show()

dataset = { 'k':[[2,5],[4,1],[6,5]],
            'g':[[3,2],[6,3],[4,5]],
            'r':[[5,5],[7,7],[8,6]]
            }

#       ---BONADSDATA---
dataset = {
    'Hus': [[35,35,],[37,37],[42,32],[60,34],[63,36],[61,35],[65,22],[76,16]],
    'Hyresrätt': [[3,12,],[26,33],[28,20],[19,6],[97,9]],
    'Bostadsrätt': [[57,45,],[24,28],[26,30]],
    'Radhus': [[37,21,],[45,47],[32,42],[55,24],[61,25]]
}

newFeature = [42,23]

def Knearest(data,predict,k=3):
    if len(data) >= k:
        warnings.warn("K is set to a value less then total gruops!")
    distance = []
    for group in data:
        for feature in data[group]:
            eucdist= np.linalg.norm(np.array(feature) - np.array(predict))
            distance.append([eucdist,group])
    votes = [i[1] for i in sorted(distance) [:k]]
    print(Counter(votes).most_common(1))
    votesResult = Counter(votes).most_common(1)[0][0]
    return votesResult

result = Knearest(dataset,newFeature,k=4)

print("Du bor i",result)
#       --- Colors för BONADSDATA ---
colors={'Hus':'r','Hyresrätt':'b','Bostadsrätt':'g','Radhus':'y'}

#       --- Sorter för BONADSDATA ---
[[plt.scatter(ii[0],ii[1], color= colors[i]) for ii in dataset[i]] for i in dataset]

#       --- Sorter för vanlig data ---
# [[plt.scatter(ii[0],ii[1], color= i) for ii in dataset[i]] for i in dataset]


plt.scatter(newFeature[0],newFeature[1], s = 100)

#       --- x & y för BONADSDATA ---
plt.ylabel("Inkomst")
plt.xlabel("Ålder")

plt.show()