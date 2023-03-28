import pandas as pd
data=pd.read_csv('addresses.csv')
#print(data)
#print(type(data))
#print(data.head(4)) # first four lines
#print(data.tail(4))# last four lines
#print(list(data.columns)) # coulmn names
#print(data.head(3))
#print(data[['id','address_1']])
#print(data[['location_id','postal_code','country']])
#print(data[['postal_code']])
#print(data['country'])
#print(type(data[['country']]))# accesing single column as list
#print(type(data['country']))#accessing single without list
##data1=pd.read_excel('airline.xls')
##print(data1)
##data2=pd.read_excel('airline1.xls')
##print(data2)
data3=pd.read_excel("airline1.xls",sheet_name="Sheet3")
#print(data3)
#print(list(data3.columns))
#data4=pd.read_excel("airline1.xls",sheet_name="Sheet3",header=None)
#print(data4)
data5=pd.read_excel("airline1.xls",sheet_name="Sheet3",header=None,names=['a','b','c','d','ss','kiran'])
print(data5)






