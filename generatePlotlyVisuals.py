import pandas as pd
import plotly.express as px

#This script creates a plotly graph for the quarantined.csv data
features = ["Date", "Quarantined"]

covid_data = pd.read_csv(
    "data/quarantined.csv",
    names=features,
    sep=r'\s*,\s*',
    engine='python',
    na_values="?",
    skiprows=1)

fig = px.bar(covid_data, x="Date", y="Quarantined", color="Quarantined", title="Percentage of Quarantined Students living On-Campus", labels={
                     "Quarantined": "Percentage Quarantined"},)
fig.write_html("quarantined.html")
