import generateFunctionData as gfd
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
import numpy as np
import plotly.io as pio
import os


if not os.path.exists('images'):
    os.mkdir('images')

g=gfd.GenerateFunctionData()

X, Y = g.generateLinearfunction(-1, 50)
#X, Y = g.generateLinearfunction(1, 0)

# Create a trace
trace = go.Scatter(
    x = X,
    y = Y,
    mode = 'markers',
    marker= dict(
        color='black',
        size = 10
    )
)

data = [trace]

layout = go.Layout(
    width=1080,
    height=1080,
    xaxis= dict(
        title='X',
        titlefont=dict(
            size=100
        )
    ),
    yaxis=dict(
        title='Y',
        titlefont=dict(
            size=100
        )
    ),
    
)

fig = go.Figure(data=data, layout=layout)

offline.plot(fig, filename='scatter.html')
pio.write_image(fig, 'images/xy.png')