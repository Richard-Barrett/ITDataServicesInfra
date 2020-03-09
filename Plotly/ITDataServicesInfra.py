import os
import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import salesforce_reporting
import requests
import pandas as pd
import dash_bootstrap_components as dbc
import plotly
from dash.dependencies import Input, Output, State
from simple_salesforce import Salesforce
#from login import *
import json

# Authentication
decrypt = "gpg --output secrets.json --decrypt secrets.gpg"

if os.path.exists("secrets.gpg"):
        returned_value = subprocess.call(decrypt, shell=True)
else:
        print("The file does not exist encryption on secrets.json not in use")
#continue

with open('secrets.json','r') as f:
        config = json.load(f)
        
# Salesforce User Session and Fields
# ==================================
from simple_salesforce import SalesforceAPI
sf = SalesforceAPI((config['username']),
                   (config['password']),
                   (config['token')])

Fields = ['isMosAlert__c',
              'Milestone_violated__c',
              'First_Reply__c',
              'CaseNumber',
              'Environment2__r.Name',
	            'Owner.Name',
              'Severity_Level__c',
              'Status',
              'Subject',
              'URL_for_support__c'
]

Items = str(Fields[1:10]).strip('[]')
print(Items).replace("'", "")
sf.query("SELECT %s from Case"% ','.join(Fields)  )

Query = sf.query("SELECT Milestone_violated__c, First_Reply__c, CaseNumber, Environment2__r.Name, Owner.Name, Severity_Level__c, Status, Subject, URL_for_support__c from Case")

# End Salesforce User Functions, Sessions and Fields
# ==================================================

#PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
PLOTLY_LOGO = "https://triking-creative.s3.amazonaws.com/Logos/Miradashboard/Screen+Shot+2019-08-20+at+1.39.07+PM.png"
#MIRADASHBOARD_LOGO = "https://triking-creative.s3.amazonaws.com/Logos/ITDataServicesInfra/ITDataServicesInfra.PNG"
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
# try running the app with one of the Bootswatch themes e.g.
# app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL])
# app = dash.Dash(external_stylesheets=[dbc.themes.SKETCHY])

# Stylesheets Reference
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


# Graph Coloring Themes
# =======================
colors = {
    'background': '#C0C0C0',
    'text': '#FF8C00'
}
# =======================

# Dataframes
# ===================
df_salesforce = Query

server = app.server

# make a reuseable navitem for the different examples
nav_item = dbc.NavItem(dbc.NavLink("Helpdesk", href="#"))
nav_item2 = dbc.NavItem(dbc.NavLink("Useful Links", href="#"))
nav_item3 = dbc.NavItem(dbc.NavLink("Rundeck", href="#"))
nav_item4 =dbc.NavItem(dbc.NavLink("Labs", href="#"))

# =========================================================
# 		    UI Navbar Variables
# =========================================================
# make a reuseable dropdown for the different examples

# =========================================================
# 		      Drop Down Menus
# =========================================================

# Drop Down Menu Items for Specific Views
# =======================================
dropdown = dbc.DropdownMenu(
    label="Menu",
    children=[
        dbc.DropdownMenuItem("A"),
        dbc.DropdownMenuItem("B"),
        dbc.DropdownMenuItem("C"),
        dbc.DropdownMenuItem("D"),
        dbc.DropdownMenuItem("E"),
        dbc.DropdownMenuItem("F"),
        dbc.DropdownMenuItem("H"),
        dbc.DropdownMenuItem("I"),
    ],
)

# Drop Down Admin Menu
# ====================
dropdown2 = dbc.DropdownMenu(
    label="Settings",
    children=[
        dbc.DropdownMenuItem("User"),
        dbc.DropdownMenuItem("layout"),
        #dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Info"),
        dbc.DropdownMenuItem("Themes"),
        dbc.DropdownMenuItem("Views")
    ],
)

# Drop Down Menu for Useful Links
# ===============================

# Drop Down Menu for Labs
# =======================

# =========================================================
#                  End  Drop Down Menus
# =========================================================

# ==========
# Search Bar
# ==========
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button("Search", color="primary", className="ml-2"),
            width="auto",
        ),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)


# =================================================
# This example that adds a logo to the navbar brand
# =================================================
navbar_logo = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
			#dbc.Col(html.Img(src=MIRADASHBOARD_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("ITDataServicesInfra Internal", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://plot.ly",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [search_bar, nav_item, nav_item2, nav_item3, nav_item4, dropdown, dropdown2], className="ml-auto", navbar=True
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-5",
)

# ========================================================
# 		  Configure navbar menu
# ========================================================
nav_menu = html.Div([
    html.Ul([
            html.Li([
                    dcc.Link('First', href='/first')
                    ], className='active'),
            html.Li([
                    dcc.Link('Second', href='/second')
                    ]),
            html.Li([
            dcc.Link('Third', href='/third')
                    ]),
            ], className='nav navbar-nav')
], className='navbar navbar-default navbar-static-top')
# =========================================================
#  		   End Navbar Variables
# =========================================================



# ===================================================================================
# 		This is the general application layout for UI Design
# ===================================================================================
app.layout = html.Div(
# ===================================================================================
    style={'backgroundColor': colors['background']},
    children=[
    # Navigation Menu
    # ---------------
    navbar_logo,

    # Top Oriented Sparkchart
    # -----------------------
    html.H1(style={'color': 'black'},children='Miradashboard'),
    dcc.Graph(),

    # Top Interactive Oriented Dataframe
    # ----------------------------------
    html.H1(children='Dataframe'),
    dash_table.DataTable(
		id='table',
    		columns=[{"name": i, "id": i} for i in df.columns],
		data=df.to_dict("rows"),
		),

    html.H1(children='Salesforce Dataframe'),
    dash_table.DataTable(
                id='df_salesforce',
                ),
    # Example Graph (Bar Chart)
    # -------------------------

# ================================================================================
# 				END APP LAYOUT
])
# ================================================================================

# APPLICATION APP CALLBACKS
# =========================
# add callback for toggling the collapse on small screens
# =======================================================
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)
