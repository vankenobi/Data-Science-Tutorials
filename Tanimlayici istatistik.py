import pandas as pd

data = pd.read_csv("Source/test.csv")
print(data.describe()) # Tanımlayıcı istatistik
#################################################
print(data.columns) # Tüm sütunların adlarını getirir.
#################################################
data2 = data.dropna(axis=1) # sütun silmek için kullanılır.
print(data2)    
#################################################
print(data.Age) # Spesifik bir sütunu seçmek
##########################################
features = ['Name','Sex','Age'] #istenelilen sütunları belli bir listeye alıp onları dataframe içerisinde istemek 
new_dataframe = data[features]
print(new_dataframe)
print(new_dataframe.head())
print(new_dataframe.describe())
##########################################

