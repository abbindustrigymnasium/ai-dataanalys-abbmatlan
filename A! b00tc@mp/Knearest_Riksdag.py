import numpy as np 
from sklearn import preprocessing, neighbors, model_selection
import pandas as pd 

df = pd.read_csv('votering.csv')
print(list(df))

df.drop(['punkt'],1, inplace=True)

df = df[["rost","parti","fodd","kon","intressent_id"]]

print(df.head(3))
inputLabels = ['kvinna','man'] # kvinna ---> 0    man ---> 1
encoder = preprocessing.LabelEncoder()
encoder.fit(inputLabels)
df["kon"] = encoder.transform(df["kon"])

inputLabels = ['C','KD','M','L','MP','V','S','SD','-'] # - ---> 0   C ---> 1   KD ---> 2   L ---> 3   M ---> 4   MP ---> 5   S ---> 6   D ---> 7   V ---> 8
encoder.fit(inputLabels)
df["parti"] = encoder.transform(df["parti"])

inputLabels = ['Nej','Ja','Frånvarande','Avstår'] # Avstår ---> 0   Frånvarande ---> 1   Ja ---> 2   Nej ---> 3
encoder = preprocessing.LabelEncoder()
encoder.fit(inputLabels)
df["rost"] = encoder.transform(df["rost"])

for i, item in enumerate(encoder.classes_):
    print(item,"--->",i)

df.replace('?', '-9999', inplace=True)

print(df.head(4))
X = np.array(df.drop(['rost'],1))
Y = np.array(df['rost'])

XTrain, XTest, YTrain, YTest = model_selection.train_test_split(X,Y, test_size = 0.2)
XTrain = XTrain.reshape(len(XTrain),-1)
YTrain = YTrain.reshape(len(YTrain),-1)
clf = neighbors.KNeighborsClassifier()
clf.fit(XTrain,YTrain)
accuracy = clf.score(XTest,YTest)
print("accuracy is",accuracy)
print(df.iloc[0])
print(XTrain[0])
#"Lars Hjälmered","980316377627","M","Göteborgs kommun","Nej","sakfrågan","227","man","1977","2018-06-20"
exampelMessure = np.array([[2,1977,1,980316377627],])

#   _____ VIDEO 35:00 _____