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
headers = pd.DataFrame(df.iloc[0,3:13])
headers.columns = [ 'Voltage']





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

fig2 = px.bar(headers, y=['Voltage'])

fig2.update_layout(yaxis_range=[10,16])



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
        value=10,
        tooltip={"placement": "bottom", "always_visible": True},
        updatemode='drag'
    ),
    

    html.Table([ html.Tr([   html.Td([dcc.Graph(
        id='batts',
        figure=fig2,
        #height=200,
        #width=50,
        #value=16,
        #showCurrentValue=False,
        #units='volts',
        #min=10,
        #max=16,
        #label="m1v",
        #labelPosition='bottom',
        #style={'margin-left': '15px'},
        #className='dark-theme-control'
    ),]), 
        
        
        
        ]),]),

    
    ])
             
@app.callback(dash.dependencies.Output('batts', 'figure'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    #batts=df.iloc[value,3:13]
    df3 = pd.DataFrame(df.iloc[value,3:13])
    df3.columns = ['Voltage']
    scale = px.colors.sequential.Jet
    batbar = px.bar(df3, y='Voltage', color='Voltage', color_continuous_scale=scale) # color_discrete_sequence=["red"])
    batbar.update_layout(yaxis_range=[10,16],) # marker=dict( colorscale=scale))
    #return 'Time shown {}seconds, ({:.2f} minutes)'.format(value, To_minutes(value))
    return batbar

if __name__ == '__main__':
    app.run_server(debug=True, host = "192.168.1.130") #app.run_server(debug = True,host = ‘0.0.0.0’).
    
  


