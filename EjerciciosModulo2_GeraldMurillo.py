import sqlite3
import pandas as pd
import matplotlib.pyplot as plot
#Punto 1: Genera una base de datos con SQL Lite.
conn = sqlite3.connect('BigBangTheory_database.db')
c = conn.cursor()
#Punto 2: Crea una tabla.
c.execute('''CREATE TABLE IF NOT EXISTS BigBangTheory ([line_id] INTEGER PRIMARY KEY, [Location] TEXT, [Scene] TEXT, [Text] TEXT, [Speaker] TEXT, [Season] INTEGER)''')
conn.commit()
BigBang_df = pd.read_csv('big_bang_theory_dataset.csv',index_col=0)
BigBang_df.to_sql('BigBangTheory', conn, if_exists='replace', index = False)
conn.commit()
#Punto 3: Histogramas
c.execute('''
          SELECT
          Location,
          Text,
          Speaker
          FROM BigBangTheory
          WHERE Text = 'Penny.'
          AND Speaker = 'Sheldon'
          ''')
df = pd.DataFrame(c.fetchall(), columns=['Location','Text','Speaker'])
plot.hist(df['Location'])
plot.show()
conn.commit()

c.execute('''
          SELECT
          Location,
          Text,
          Speaker
          FROM BigBangTheory
          WHERE Text like '%Penny%'
          AND Speaker = 'Sheldon'
          ''')
df2 = pd.DataFrame(c.fetchall(), columns=['Location','Text','Speaker'])
plot.hist(df2['Location'])
plot.show()
conn.commit()

conn.close()
