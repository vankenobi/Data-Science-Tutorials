from logging.handlers import DatagramHandler
from pyexpat import features
from sklearn.tree import DecisionTreeRegressor
import pandas as pd

features = ["PassengerId","Pclass"]
dataframe  = pd.read_csv("Source/train.csv") 

new_dataframe = dataframe[features]

y = dataframe.SibSp

model = DecisionTreeRegressor(random_state=1)
model.fit(new_dataframe,y)
print(new_dataframe.head())
print("Tahmin")
print(model.predict(new_dataframe.head()))
