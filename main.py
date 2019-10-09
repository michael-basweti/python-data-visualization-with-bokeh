from bokeh.plotting import figure, output_file, show, save, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components
import pandas

df = pandas.read_csv('cars.csv')

# car=df['Car']
# hp=df['Horsepower']

# create column data source
source = ColumnDataSource(df)

output_file('index.html')

# car list
car_list=source.data['Car'].tolist()

p= figure(
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    title="Cars With Top Horsepower",
    x_axis_label='Horsepower',
    tools="pan, box_select, zoom_in, zoom_out, save, reset"
)

p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Car',
        palette=Blues8,
        factors=car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend='Car'
)

# add legend
p.legend.orientation='vertical'
p.legend.location='top_right'
p.legend.label_text_font_size='10px'

# add tooltips
hover = HoverTool()
hover.tooltips = """
<div>
    <h3>@Car</h3>
    <div><strong>Price: </strong>@Price</div>
    <div><strong>Horsepower: </strong>@Horsepower</div>
    <div><img src="@Image" alt-"" width=200></div>
</div>
"""

p.add_tools(hover)

# show results
# show(p)

save(p)

# x=[1,2,3,4,5,6]
# y=[2,4,6,8,10,12]

# output_file('index.html')

# # add plot
# p= figure(
#     title="Simple Example",
#     x_axis_label='X AXIS',
#     y_axis_label='Y AXIS',
# )

# # render glyph
# p.line(x,y, legend="Test", line_width=2)

# # show results
# show(p)

# print out scripts and div
script, div = components(p)
print(div)
print(script)