# Load packages
import pandas as pd
import plotly.express as px

# Upload your data as CSV and load as data frame
df = pd.read_csv('data/sequences.csv')
df

# Visualize user journey as a sunburst chart
# Reference: https://plotly.com/python-api-reference/generated/plotly.express.sunburst.html
fig = px.sunburst(
  data_frame = df,                          # your data frame
  path = ['event_1', 'event_2', 'event_3'], # list of column names representing the user journey
  values = 'n',                             # column name indicating number of users following the path
  height = 500,                             # height of the chart
  title = "User Journey"                    # title of the chart
)
fig.update_layout(margin = dict(l=0, r=0, b=0))
fig.show(config = {"displayModeBar": False})
