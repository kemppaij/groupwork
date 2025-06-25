import psycopg2
from config import config
from database import (get_connection, create_table, create_database)

if __name__ == '__main__':
  # common connection, you can specify to which
  # database you connect with a param
  conn = get_connection('workhours')  
  
  # create database if not exist
  create_database()
  # create table if not exist
  create_table()
  
  
  