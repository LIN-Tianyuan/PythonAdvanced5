import json
from pyecharts.charts import Line

f_us = open("America.txt", "r", encoding="UTF-8")
us_data = f_us.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_data = us_data[:-2]
us_data = json.loads(us_data)
# print(us_data)
# print(type(us_data))
trend_data = us_data["data"][0]["trend"]
x_data = trend_data["updateDate"][:314]
y_data = trend_data["list"][0]["data"]
f_us.close()

line = Line()
line.add_xaxis(x_data)
line.add_yaxis("Amercia: Confirmation of diagonsis",y_data)
line.render()
