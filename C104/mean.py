import pandas as pd

import plotly.express as ps

df = pd.read_csv("E:/PYTHON__/C104/SOCR-HeightWeight.csv")

#mean height

height = df['Height(Inches)'].tolist()
sum = 0

for h in height:
    sum = sum+h

mean = sum/len(height)
print("height Mean:"+str(mean))

#mean weight

weight = df['Weight(Pounds)'].tolist()
sum1 = 0

for w in weight:
    sum1 = sum1+w

mean1 = sum1/len(weight)
print("Weight(Pounds) Mean:"+str(mean))
