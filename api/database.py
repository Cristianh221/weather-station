'''
Nombre: Cristian Hernandez
Scrpt description: weather-station Database
engine: SQLite 3
Date: 9/9/24
'''
#import database engine  package
import sqlite3


#create weather-station database connection
con = sqlite3.connect('weather-station.db')


#created cursor
cur = con.cursor()


#users model
users_model ='''
    CREATE TABLE IF NOT EXISTS users (
  id integer PRIMARY KEY,
  username TEXT NOT NULL,
  role TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  status BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT (datatime('now','localtime')),
  update_at TIMESTAMP DEFAULT (datatime('now','localtime')),
  deleted_at NULL
  )




'''


# Eexecute query
cur.execute(users_model)


#close connection
con.close()