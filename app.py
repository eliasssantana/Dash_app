import os
import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta

start = datetime.datetime.now() - relativedelta(years=5)
end = datetime.datetime.now() - relativedelta(years=1)


df = web.DataReader("GE", 'yahoo', start=start, end=end)

trace_close = go.Scatter(x=list(df.index), y= list(df.Close), name="Close", line=dict(color="#f44242"))

data = [trace_close]

layout = dict(title="Stock Chart", showlegend=True)

fig = dict(data=data, layout=layout)
print(df.head())


app = dash.Dash()
app.layout = html.Div([
     html.Div(html.H1(children="Hello World")),
     html.Label("DASH GRAPH"),
     html.Div(
          dcc.Graph(id="Stock Chart", figure=fig)
     )]
)

if __name__ == '__main__':
    app.run_server(debug=True)