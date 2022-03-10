import pandas as pd
import statistics as st
import plotly.express as ps

df = pd.read_csv("E:/PYTHON__/C104/SOCR-HeightWeight.csv")

#median height

height = df['Height(Inches)'].tolist()
mode = st.mode(height)
print("Mode Height:"+str(mode))


#mean weight

wei = df['Weight(Pounds)'].tolist()
mode = st.mode(wei)
print("Mode Weight:"+str(mode))