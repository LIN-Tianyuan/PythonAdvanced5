import pandas as pd
from pyecharts.charts import Map, Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.options import InitOpts, VisualMapOpts, LegendOpts, LabelOpts, TitleOpts, TextStyleOpts
from pyecharts.types import Legend

dataset = pd.read_csv('owid-covid-data.csv')
# print(dataset.head())
# Changer la date du type de données objet en type de données datetime
dataset['date'] = pd.to_datetime(dataset['date'])
# Trier les données par date
df = dataset.sort_values(by=['date'], ascending=False)
map_df = df[df['date'] == "2022-08-01"]
map_df.reset_index(drop=True, inplace=True)
# print(map_df)

country = list(map_df["location"])
total_cases = list(map_df["total_cases"])
# Préparer les données
list1 = [[country[i], total_cases[i]] for i in range(len(country))]
# print(list1)
# Créer la carte et définir la taille de la carte
map1 = Map(init_opts=InitOpts(width="1000px", height="460px"))
# Ajouter la carte du monde
map1.add("Total Confirmed Cases", list1, maptype="world", is_map_symbol_show=False)
# Aucune étiquette affichée (nom du pays)
map1.set_series_opts(LabelOpts(is_show=False))
map1.set_global_opts(
    visualmap_opts=VisualMapOpts(max_=1100000, is_piecewise=True,
                                 pieces=[
                                     {"min": 500000},
                                     {"min": 200000, "max": 499999},
                                     {"min": 100000, "max": 199999},
                                     {"min": 50000, "max": 99999},
                                     {"min": 10000, "max": 49999},
                                     {"max": 9999}
                                 ]),
    title_opts=TitleOpts(
        title="Covid-19 Worldwide Total Cases",
        subtitle="Till August 1st, 2022",
        pos_left="center",
        padding=0,
        item_gap=2,
        title_textstyle_opts=TextStyleOpts(
            color="darkblue",
            font_weight="bold",
            font_family="Courrier New",
            font_size=30
        ),
        subtitle_textstyle_opts=TextStyleOpts(
            color="grey",
            font_weight="bold",
            font_family="Courrier New",
            font_size=13
        ),
    ),
    # Montrer la légende ou non
    legend_opts=LegendOpts(is_show=False),
)
# Montrer la carte
map1.render()