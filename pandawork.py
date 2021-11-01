import plotly.graph_objects as go
from plotly import offline

lat = [32.83105, 34.50349983866648, 38.865576260782646, 37.93690]
lon = [-117.17597, -119.83034775441203, -77.05823644257613, -122.31578, ]

fig = go.Figure()

fig.add_trace(go.Scattergeo(
    locationmode='USA-states',
    mode='lines+markers',
    line=dict(width=3, color='orange'),
    marker=dict(
        size=15,
        color='orange',
        line=dict(
            width=1,
            color='black'
        )
    ),
    lon=lon,
    lat=lat,
    hoverinfo='text',
))

fig.update_layout(
    title_text='Where I have lived',
    showlegend=False,
    geo=dict(
        scope='usa',
        resolution=50,
        showland=True,
        showlakes=True,
        landcolor='lightgrey',
        countrycolor='skyblue',
        lakecolor='powderblue',
    ),
)

offline.plot(fig, filename='twopoints.html')
