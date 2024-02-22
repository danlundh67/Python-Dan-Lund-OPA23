import plotly_express as px

gp = px.data.gapminder()

fig=px.scatter(gp, x="gdpPercap", y="lifeExp", size="pop", color="country", size_max=70, log_x=True, animation_frame="year", animation_group="country", title="Life exepctancy per country",range_y=[25,90], range_x=[100,100000])

fig.show()