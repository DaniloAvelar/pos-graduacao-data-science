import pandas as pd

df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
       index=['cobra', 'viper', 'sidewinder'],
       columns=['max_speed', 'shield'])
print(df.loc['viper'])
print(df.loc[['viper', 'sidewinder']])

df = pd.DataFrame({'A': range(1, 6),
                   'B': range(10, 0, -2),
                   'C': range(10, 5, -1)})
print(df.query('A > B'))
print(df.query('B == `C C`'))
print(df[df.A > df.B])

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                               'Parrot', 'Parrot'],
                    'Max Speed': [380., 370., 24., 26.]})
grouped = df.groupby(['Animal'])
print(grouped.mean())