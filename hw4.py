import sqlalchemy
import psycopg2

engine = sqlalchemy.create_engine('postgresql://postgres:vk199786@localhost:5432/Netology 2')
#print(engine.table_names())
connection = engine.connect()

#sel = connection.execute("""SELECT * FROM Artist;""").fetchall()
#print(sel)

sel2 = connection.execute("""SELECT name, year FROM Album 
WHERE year >= 2018;""").fetchall()
print(sel2) #В базе данных таких альбомов нет

sel3 = connection.execute("""SELECT name, duration FROM Track 
ORDER BY duration DESC;""").fetchone()
print(sel3)

sel4 = connection.execute("""SELECT name FROM Track 
WHERE duration >= 3.5;""").fetchall()
print(sel4)

sel5 = connection.execute("""SELECT name FROM Collection 
WHERE year BETWEEN 2018 and 2020;""").fetchall()
print(sel5) #В базе данных таких сборников нет

sel6 = connection.execute("""SELECT name FROM Artist;""").fetchall()
for artist in sel6:
    if len(artist) == 1:
        print(artist)

sel7 = connection.execute("""SELECT name FROM Track 
WHERE name LIKE '%%my%%';""").fetchall() #В базе данных таких треков нет
print(sel7)
