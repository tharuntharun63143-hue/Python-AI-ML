#MINProject in data loading and inspection
#data loading
import pandas as pd
passenger = pd.read_csv("airline-passengers.csv")
print( passenger)
#inspection data starting0 rows 1 
print("10 passengers:",passenger.head(10))
#inspection data last 5 rows
print("5 passengers atlast:",passenger.tail())
#checking how many rows and columns
print(passenger.shape)
#how many columns does the dataset have checking?
print(passenger.columns)
#information about the passenger
print(passenger.info())
#checking summary details of passengers
print(passenger.describe())
