# SpaceX Falcon 9 Launch Records Dashboard
# IBM Data Science Capstone - Interactive Visual Analytics with Plotly Dash

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data
spacex_df = pd.read_csv("dataset_part_2.csv")
max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

# Create a Dash application
app = dash.Dash(__name__)

# Get unique launch sites
launch_sites = spacex_df['LaunchSite'].unique().tolist()
site_options = [{'label': 'All Sites', 'value': 'ALL'}]
site_options += [{'label': site, 'value': site} for site in launch_sites]

# Create app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Dropdown for Launch Site selection
    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder="Select a Launch Site",
        searchable=True
    ),
    html.Br(),
    
    # Pie chart for success counts
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),
    
    html.P("Payload range (Kg):"),
    
    # Payload range slider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: str(i) for i in range(0, 10001, 2500)},
        value=[min_payload, max_payload]
    ),
    
    # Scatter chart for payload vs success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

# Callback for pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df, values='Class', names='LaunchSite',
                     title='Total Success Launches by Site')
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == entered_site]
        fig = px.pie(filtered_df, names='Class',
                     title=f'Total Success Launches for site {entered_site}')
    return fig

# Callback for scatter chart
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload):
    low, high = payload
    mask = (spacex_df['PayloadMass'] >= low) & (spacex_df['PayloadMass'] <= high)
    if entered_site == 'ALL':
        fig = px.scatter(spacex_df[mask], x='PayloadMass', y='Class',
                         color='BoosterVersion',
                         title='Correlation between Payload and Success for All Sites')
    else:
        filtered_df = spacex_df[(spacex_df['LaunchSite'] == entered_site) & mask]
        fig = px.scatter(filtered_df, x='PayloadMass', y='Class',
                         color='BoosterVersion',
                         title=f'Correlation between Payload and Success for {entered_site}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
