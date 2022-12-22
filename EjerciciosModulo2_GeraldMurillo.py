import sqlite3
import pandas as pd
import matplotlib.pyplot as plot

#Punto 1: Genera una base de datos con SQL Lite.
#abre una conexion con la db
conn = sqlite3.connect('BigBangTheory_database.db')
c = conn.cursor()

#Punto 2: Crea una tabla.
#query para crear la tabla
c.execute('''CREATE TABLE IF NOT EXISTS BigBangTheory ([line_id] INTEGER PRIMARY KEY, [Location] TEXT, [Scene] TEXT, [Text] TEXT, [Speaker] TEXT, [Season] INTEGER)''')
conn.commit()
#lee csv en un df de pandas
BigBang_df = pd.read_csv('big_bang_theory_dataset.csv',index_col=0)
#carga el df en la tabla creada
BigBang_df.to_sql('BigBangTheory', conn, if_exists='replace', index = False)
conn.commit()

#Punto 3: Histogramas
#query para obtener Sheldon diciendo 'Penny.'
c.execute('''
          SELECT
          Location,
          Text,
          Speaker
          FROM BigBangTheory
          WHERE Text = 'Penny.'
          AND Speaker = 'Sheldon'
          ''')
df2 = pd.DataFrame(c.fetchall(), columns=['Location','Text','Speaker'])
conn.commit()
#primer histograma
figure, axis = plot.subplots(2, 1)
axis[0].hist(df2['Location'])
axis[0].set_title("Sheldon dice exclusivamente Penny.")
# query para obtener Sheldon mencionando penny
c.execute('''
          SELECT
          Location,
          Text,
          Speaker
          FROM BigBangTheory
          WHERE Text like '%Penny%'
          AND Speaker = 'Sheldon'
          ''')
df3 = pd.DataFrame(c.fetchall(), columns=['Location','Text','Speaker'])
conn.commit()
#segundo histograma
axis[1].hist(df3['Location'])
axis[1].set_title("Sheldon menciona Penny")
#muestra el plot
plot.show()
# hay muchos locations donde Sheldon menciona a Penny por lo que el eje X del histograma se ve superpuesto

#Punto 4: location vs Speaker
#query para obtener location y Speaker
c.execute('''
          SELECT
          Location,
          count(Text) count_text,
          Speaker
          FROM BigBangTheory
          WHERE Text like '%Penny%'
          GROUP BY Speaker,Location
          ''')
df4 = pd.DataFrame(c.fetchall(), columns=['Location','Text','Speaker'])
df4['Indice'] = df4['Location'] + df4['Speaker']
print(df4)
conn.commit()
plot.scatter(df4['Speaker'],df4['Location'])
plot.title("Speakers dicen 'Penny' en cada location")
plot.show()
#cierra la conexión
conn.close()