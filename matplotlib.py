import matplotlib
import seaborn
import pandas

matplotlib.rcParams['figure.figsize'] = [15, 7] # указываем размер графика

top_games = pandas.Series(['Counter-Strike: Global Offensive',
             'Dota 2',
             'Team Fortress 2',
             "PLAYERUNKNOWN'S BATTLEGROUNDS",   # двойные кавычки позволяют
             "Garry's Mod",                     # поставить апостроф внутри строки
             'Grand Theft Auto V',
             'PAYDAY 2',
             'Unturned',
             'Terraria',
             'Left 4 Dead 2'])

positive_reviews = pandas.Series([2644404, 863507, 515879, 496184, 363721,
                    329061, 308657, 292574, 255600, 251789])

seaborn.barplot(x=positive_reviews, y=top_games)