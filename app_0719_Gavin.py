#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 00:39:07 2019

@author: apple
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table_experiments as dt
import plotly.graph_objs as go
go.Scattermapbox
#import os
import pandas as pd
import copy

mapbox_access_token = 'pk.eyJ1IjoidXJzdWxha2Fjem1hcmVrIiwiYSI6ImNpd2ZldGh0OTAw\
MTcyb21ucjExbHpleW8ifQ.-m-YwEngdx5IEET1r4ZFqg'
#os.getenv('MAPBOXKEY')

app = dash.Dash(__name__)
server = app.server

# load data
url = 'https://github.com/a627142126/capstone-2018/blob/master/verified_avg_fee_by_station_geocoded_jx.xlsx?raw=true'
df = pd.read_excel(url)
df['text'] = df['Station Name'] #+ df['Avg. Test Fees']
df = df[['Station Id', 'Avg. Test Fees', 'Station Name', 
         'Address', 'City', 'ZIP', 'Phone Number', 'Lat', 'Lon', 'Service Type', 'text']]
#df['Avg. Test Fees'] = df['Avg. Test Fees'].str.replace('$', '')
df['Avg. Test Fees'] = df['Avg. Test Fees'].astype('float64')
df['ZIP'] = df['ZIP'].astype('float64')
df.rename(columns={'Avg. Test Fees': 'Price'}, inplace=True)



data = [go.Scattermapbox(
        lon = df['Lon'],
        lat = df['Lat'],
        text = df['text'],
        marker=go.scattermapbox.Marker(
            colorscale = 'YlOrRd',
            reversescale = True,
            color = df['Price'],
            cmin = 10,
            cmax = df['Price'].max(),
            colorbar=dict(
                title='Price($)'
            )
        )
        )]



layout_table = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=35,
        r=10,
        b=35,
        t=5
    ),
    hovermode="closest",
    plot_bgcolor='#fffcfc',
    paper_bgcolor='#fffcfc',
    legend=dict(font=dict(size=10), orientation='h'),
    title='Interactive table where you can sort by price and zipcode',
)
layout_table['font-size'] = '16'
layout_table['margin-top'] = '10'

layout_map = dict(
    autosize=True,
    height=500,
    font=dict(color="#191A1A"),
    titlefont=dict(color="#191A1A", size='14'),
    margin=dict(
        l=20,
        r=20,
        b=70,
        t=45
    ),
    hovermode="closest",
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    legend=dict(font=dict(size=15), orientation='h'),
    title='',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="light",
        center=dict(
            lon=-111.9067,
            lat=40.6666
        ),
        pitch=0,
        zoom=10,
        
    )
)
layout_right = copy.deepcopy(layout_table)
layout_right['height'] = 300
layout_right['margin-top'] = '10'
layout_right['margin-right'] = '-120'
layout_right['font-family'] = 'verdana'

def gen_map(df):
    # groupby returns a dictionary mapping the values of the first field
    # 'classification' onto a list of record dictionaries with that
    # classification value.
    if 'Lat' not in df:
        return {
            "data":[{
                "type":"scattermapbox",
                "lat":list(),
                "lon":list(),
                "mode": "markers",
                "marker": {
                    "size": 6,
                    "opacity": 0.7
                }}],
            "layout": layout_map
        }
    return {
        "data": [{
                "type": "scattermapbox",
                "lat": list(df['Lat']) if 'Lat' in df else list(),
                "lon": list(df['Lon']) if 'Lon' in df else list(),
                "hoverinfo": "text",
                "hovertext": [["Name: {} <br>Address: {} <br>Price: {} <br>Phone: {} <br>Service: {}".format(i,j,k,l,m)]
                                for i,j,k,l,m in zip(df['text'], df['Address'],df['Price'],df['Phone Number'],df['Service Type'])],
                "mode": "markers",
                "name": list(df['text']),
                "marker": {
                    "size": 6,
                    "opacity": 0.7
                }
        }],
        "layout": layout_map
    }

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.Img(
                    src="https://raw.githubusercontent.com/a627142126/capstone-2018/master/logo.png",
                    className='three columns',
                    style={
                        'height': '15%',
                        'width': '15%',
                        'float': 'center',
                        'position': 'relative',
                        'padding-top': 0,
                        'padding-right':0
                    },
                ),
               
                html.Img(
                    src="https://cusp.nyu.edu/wp-content/uploads/2017/12/PNG-logo-01.png",
                    className='three columns',
                    style={
                        'height': '16%',
                        'width': '16%',
                        'float': 'right',
                        'position': 'relative',
                        'padding-top': 12,
                        'padding-right': 0
                    },
                ),
                
        
                html.Div(children='''
                        You can use this website to locate the nearest repair shop that can do emission test.
                        ''',
                        style={'color':'#000000',
                               'font-family':'verdana'},
                        className='nine columns'
                )
            ], className="row"
        ),

        # Selectors
        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose Zipcode:'),
                        dcc.Dropdown(
                            id='zipcode',
                            options= [{'label': str(int(item)),
                                                  'value': str(item)}
                                                 for item in set(df['ZIP'])],
                            multi=True,
                            value=list(set(df['ZIP']))
                        )
                    ],
                    className='six columns',
                    style={'margin-top': '10',
                           'font-family':'verdana'}
                ),
                html.Div(
                    [
                        html.P('Choose Price Range:'),
                        dcc.RangeSlider(
                            id='price',
                            marks={0:'$0',
                                   5:'$5',
                                   10:'$10',
                                   15:'$15',
                                   20:'$20',
                                   25:'$25',
                                   30:'$30',
                                   35:'$35',
                                   40:'$40',
                                   45:'$45',
                                   50:'$50',
                                   55:'$55',
                                    },
                            min=0,
                            max=55,
                            step=1,
                            value=[0, 55]
                        )
                    ],
                    className='six columns',
                    style={'margin-top': '30px',
                           'font-family':'verdana'}
                ),
                html.Div(
                    [
                        dcc.Graph(id='map-graph',
                                  animate=True,
                                  style={'margin-top': '20'})
                    ], className = "six columns"
                ),
                html.Div(
                    [
                        html.P('Click on the column name to sort the values, or use "Filter Rows" button to filter values in each column.'),    
                        dt.DataTable(
                            rows=df.to_dict('records'),
                            columns=df.ix[:, [2, 1, 3, 4, 5, 6, 9]].columns,
                            column_widths=[50, 50],
                            row_selectable=True,
                            filterable=True,
                            sortable=True,
                            selected_row_indices=[],
                            id='datatable'),
                    ],
                    style = layout_right,
                    className="six columns"
                )
            ],
            className='row',
            style={'columnCount': 2}
        ),
          
     

        # Map + table + Histogram
        html.Div(
            [
                
                
                html.Div(
                    [
                        html.P('Developed by Capstone Team at CUSP - ', style = {'display': 'inline'}),
                        html.A('cusp@nyu.edu', href = 'cuspo@nyu.edu')
                    ], className = "twelve columns",
                       style = {'fontSize': 18, 'padding-top': 20}
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one'))
                    
                    
                    
@app.callback(
        Output('map-graph', 'figure'),
        [Input('datatable', 'rows'),
         Input('datatable', 'selected_row_indices')])     

def map_selection(rows, selected_row_indices):
    aux = pd.DataFrame(rows)
    temp_df = aux.ix[selected_row_indices, :]
    if len(selected_row_indices) == 0:
        return gen_map(aux)
    return gen_map(temp_df)         




@app.callback(
    Output('datatable', 'rows'),
    [Input('zipcode', 'value'),
     Input('price', 'value')])
def update_selected_row_indices(zipcode, price):
    map_aux = df.copy()
    if len(zipcode) == 0:
        zipcode = set(df['ZIP'])
    if len(price) == 0:
        price = [0, 55]
    # Type filter
    map_aux = map_aux[map_aux['ZIP'].isin(zipcode)]
    if map_aux.empty:
        return {}

    # Boroughs filter
    map_aux = map_aux[map_aux['Price'].between(price[0], price[1], inclusive=True)]
    if map_aux.empty:
        return {}
    rows = map_aux.to_dict('records')
    return rows

       
        
        
        
        


if __name__ == '__main__':
    app.run_server(debug=True)

