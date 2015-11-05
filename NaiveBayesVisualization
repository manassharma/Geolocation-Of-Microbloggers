#
import barchart
from matplotlib import pyplot

chart = barchart.BarChart(ylabel="ConfidenceLevel", title="Grouped BarChart", width=0.5)

f= open("Bayes.txt",'r')
for line in f:
    nextline = f.next();

    chart.add_group_data("USER:"+line, [(nextline.split("-")[0],float(nextline.split("-")[1].split(" ")[0])  ),
                                (nextline.split("-")[1].split(" ")[1],float(nextline.split("-")[2])),
                               ])


    chart.auto_add_categories()
    chart.add_category("cat2", "2nd category")

fig, ax = pyplot.subplots(1, 1)
fig.subplots_adjust(bottom=0.15)
chart.plot(ax, stacked=False, sort=True)

# output
pyplot.savefig("barchart-grouped.png")
