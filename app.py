import os
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas_datareader.data as web
import datetime
from dateutil.relativedelta import relativedelta

start = datetime.datetime.now() - relativedelta(years=5)
end = datetime.datetime.now() - relativedelta(years=1)



# data = [trace_close]

# layout = dict(title=inputStock, showlegend=True)
# fig = dict(data=data, layout=layout)

# print(df.head())


app = dash.Dash(__name__)
app.layout = html.Div([
     html.Div([
          dcc.Input(id="stock-input", value="SPY", type="text")
          ]),
     html.Div(html.H1(children="Hello World")),
     html.Label("DASH GRAPH"),
     # html.Div(
     #      dcc.Input(
     #      id="stock-output",
     #      placeholder="Enter a stock to be charted",
     #      type="text",
     #      value="",
     #      className="input"
     # )
     # ),
     html.Div([
          html.Div([
               html.H3("Column 1"),
               dcc.Graph(
                    id="stock-output"
               )
          ])
     ])
     # html.Div(
     #     dcc.Dropdown(
     #         options=[
     #              {"label":"Candlestick", "value": "Candlestick"},
     #              {"label":"Line", "value": "Line"}
     #         ]
     #     ) 
     # )
     ]
)

# external_stylesheets = [{}
#       "external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"
# ]


@app.callback(dash.dependencies.Output("stock-output", "figure"),
               [dash.dependencies.Input("stock-input","value")])

def update_fig(input_value):
     df = web.DataReader(input_value, 'yahoo', start=start, end=end)

     data = []
     trace_close = go.Scatter(x=list(df.index), y= list(df.Close), name="Close", line={"color":"#f44242"})

     data.append(trace_close)
     layout = {"title":"Callback Graph"}
     return {
          "data": data,
          "layout": layout
     }

if __name__ == '__main__':
    app.run_server(debug=True)