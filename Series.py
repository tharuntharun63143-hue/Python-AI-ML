#series 
import pandas as pd
marks = pd.Series([85,98,82,75,75,95], index = ["adithya","hithesh","gowtham","lakshmisha","prajwal","Nithin"])
print("Series:\n",marks)
#accessing element
print("\nSeries with custom index\n",marks)
print("\n marks of gowtham:",marks["gowtham"])
print("\n index of 95:",marks[marks==95])
#methods or operations
print("\n Max:",marks.max())
print("\n Mean:",marks.mean())
print("\n Summary:",marks.describe())
