import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# DATA
df = pd.DataFrame(
    np.random.randn(100, 4),
    columns=['A', 'B', 'C', 'D']
)

df2 = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Values': [32, 43, 50]
})

#----------------------------------------------

# fig = px.line(df)


#----------------------------------------------
# fig = px.scatter(df, x='A', y='B')

#----------------------------------------------
# fig = px.bar(df2, x='Category', y='Values')

#----------------------------------------------

# fig = px.bar(df.count())
# fig = px.bar(df.sum())

#----------------------------------------------

# fig = px.box(df)

#----------------------------------------------

df3 = pd.DataFrame({
    'x': [1,2,3,4,5],
    'y': [10,20,30,40,50],
    'z': [500,400,300,200,100]
})


# fig = px.scatter_3d(df3,x='x',y='y',z='z')


#----------------------------------------------

# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)

# X, Y = np.meshgrid(x, y)

# Z = np.maximum(20 - np.sqrt(X**2 + Y**2) * 2, 0)

# fig = go.Figure(
#     data=[go.Surface(x=X, y=Y, z=Z)]
# )

#----------------------------------------------

# fig = px.histogram(df['A'], nbins=20, title='Histogram of A')
# fig = px.histogram(df)

#----------------------------------------------

#Spread plot
#bubble plot

# fig = px.scatter_matrix(df)

fig.show()



























