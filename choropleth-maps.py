import json
import pandas as pd
import plotly.express as px

with open("la.json", "r", encoding="utf-8") as f:
    india = json.load(f)

df = pd.DataFrame({
    "State": [
        "Uttar Pradesh",
        "Haryana",
        "Punjab",
        "Delhi",
        "Rajasthan",
        "Maharashtra"
    ],
    "Value": [10, 20, 30, 15, 25, 35]
})

fig = px.choropleth(
    df,
    geojson=india,
    locations="State",
    featureidkey="properties.NAME_1",
    color="Value",
    color_continuous_scale="Portland"
)

fig.update_geos(
    fitbounds="locations",
    visible=False
)

fig.show()