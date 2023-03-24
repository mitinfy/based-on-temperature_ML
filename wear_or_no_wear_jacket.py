#supervised learning
#pip install sklearn
from sklearn import tree
#pip install sklearn [sci-kit package]
# if outside temperature is between 30 - 15 then no jacket otherwise wear jacket!
features = [[30, 0], [25, 0], [20, 0], [15, 1],[10, 1]]  
labels = [0, 0, 0, 1, 1]
#Training classifier
classifier = tree.DecisionTreeClassifier()  # using decision tree classifier
classifier = classifier.fit(features, labels)  # Find patterns in data

temp=int(input("Enter Temperature:"))
#Making predictions
if classifier.predict([[temp, 1]]):
    print("Wear Jacket")
else:
    print ("No Jacket!")
