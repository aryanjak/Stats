import pandas as pd

import plotly.express as ps

df = pd.read_csv("E:/PYTHON__/C104/SOCR-HeightWeight.csv")

#median height

height = df['Height(Inches)'].tolist()
n = len(height)

if n%2==0:
    median = height[n//2]
    print("Median of Height:"+str(median))

else:
    median = (height[(n-1)//2] + height[(n+1)//2])/2
    print("Median of Height:"+str(median))


#median weight

wei = df['Weight(Pounds)'].tolist()
n = len(wei)

if n%2==0:
    median = wei[n//2]
    print("Median of Weight:"+str(median))

else:
    median = (wei[(n-1)//2] + wei[(n+1)//2])/2
    print("Median of Weight:"+str(median))
