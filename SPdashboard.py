# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 10:11:23 2021

@author: FCAD
"""

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


import numpy as np
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from dash import dash_table
import plotly.graph_objects as go
import plotly.express as px
import dash_daq as daq

import pandas as pd

import plotly.graph_objects as go



external_stylesheets = ['SRPrius.css']

app = dash.Dash(__name__)



# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('log.csv')
#df = pd.read_csv('log.csv', header=None, error_bad_lines=False)
df3 = pd.DataFrame(df.iloc[1:5,3:13])





def To_minutes(value):
    return value/60

#RPM,B+,m1v,m2v,m3v,m4v,m5v,m6v,m7v,m8v,m9v,m10v
#x=range(0,811,1)
fig = px.line(df, x=df.index, y=['m1v', 'm2v', 'm3v', 'm4v', 'm5v', 'm6v', 'm7v', 'm8v', 'm9v', 'm10v'], 
              line_shape='spline', 
              render_mode="svg"
              #title="Prius C Drive Battery Module Voltages"#,
              #labels={
               #      x: "Drive time (Seconds)",
                #     y: "Module Voltage"
                    # }
              )

fig.update_layout(
                title = {
                'text': 'Prius C Drive Battery Module Voltages',
                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
                xaxis=dict(title='Time (s)'),
                yaxis=dict(title='Voltage')
                )



app.layout = html.Div(children=[
    html.H1(children='Senior Prius Dashboard'),

    html.Div(children='''
        Senior Prius, "la cucaracha" of hybrid drive battery monitors
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
        
    ),
        dcc.Slider(
        id='my-slider',
        min=0,
        max=850,
        step=1,
        value=0,
        tooltip={"placement": "bottom", "always_visible": True},
        updatemode='drag'
    ),
    

    html.Table([ html.Tr([   html.Td([daq.Tank(
        id='m1v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m1v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m2v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m2v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m3v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m3v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m4v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m4v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m5v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m5v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m6v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m6v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m7v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m7v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m8v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m8v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m9v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m9v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]), html.Td([daq.Tank(
        id='m10v',
        height=200,
        width=50,
        value=16,
        showCurrentValue=False,
        units='volts',
        min=10,
        max=16,
        label="m10v",
        labelPosition='bottom',
        style={'margin-left': '15px'},
        className='dark-theme-control'
    ),]),
        
        
        ]),]),

    
    ])
             
@app.callback([dash.dependencies.Output('m1v', 'value')],
               [dash.dependencies.Output('m2v', 'value')],
                [dash.dependencies.Output('m3v', 'value')],
                 [dash.dependencies.Output('m4v', 'value')],
                  [dash.dependencies.Output('m5v', 'value')],
                   [dash.dependencies.Output('m6v', 'value')],
                    [dash.dependencies.Output('m7v', 'value')],
                     [dash.dependencies.Output('m8v', 'value')],
                      [dash.dependencies.Output('m9v', 'value')],
                       [dash.dependencies.Output('m10v', 'value')],
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    (m1v, m2v, m3v, m4v, m5v, m6v, m7v, m8v, m9v, m10v)=df.iloc[value,3:13]
    #return 'Time shown {}seconds, ({:.2f} minutes)'.format(value, To_minutes(value))
    return m1v, m2v, m3v, m4v, m5v, m6v, m7v, m8v, m9v, m10v

if __name__ == '__main__':
    app.run_server(debug=True, host = "127.0.0.1") #app.run_server(debug = True,host = ‘0.0.0.0’).
    
  


