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
#X, Y = g.generateQuadraticfunction(1, 0)


data = [
    go.Parcoords(
        line = dict(color = 'black'),
        labelfont=dict(
            size=100
        ),
        dimensions = list([
            dict(range=[-50, 100], label = 'X', values = X),
            dict(range=[-50, 100], label = 'Y', values = Y)
        ])
    )
]

layout = go.Layout(
    width=1080,
    height=1080
)

fig = go.Figure(data=data, layout=layout)

offline.plot(fig, filename='scatter.html')
pio.write_image(fig, 'images/pcp.png')