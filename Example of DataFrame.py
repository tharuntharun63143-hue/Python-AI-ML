#dataframe
data = {
    'Name':["tharun","adithya",'hithesh','kishan'],
    'department':["CS","marketing",'mechieancial','art'],
    'salary':[1000000000,100000,3000000,8900000]

}
df = pd.DataFrame(data)
print("\nsalary of employee\n",df['salary'])
print("\n row with label index 2:\n",df.loc[2])
print("\n row at integer index 0:\n",df.iloc[0])
