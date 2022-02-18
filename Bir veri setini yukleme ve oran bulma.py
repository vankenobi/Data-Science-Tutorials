import pandas as pd
import numpy as np

train_data = pd.read_csv("Source/train.csv")
print(train_data.head())

value = train_data.loc[train_data.Sex == "female"]["Survived"]
rate_woman = sum(value)/len(value)

print(rate_woman)

