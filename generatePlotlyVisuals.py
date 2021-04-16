import chart_studio.tools as tls
import pandas as pd
import plotly.express as px

features = ["Date", "Students", "Employees", "Subcontractors"]

covid_data = pd.read_csv(
    "data/UNCP_ACTIVE_CASES.csv",
    names=features,
    sep=r'\s*,\s*',
    engine='python',
    na_values="?",
    skiprows=1)

fig = px.bar(covid_data, x="Date", y="Students", color="Students", title="Students with Active Cases")
fig.write_html("student_graph.html")
