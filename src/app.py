import psycopg2
from config import config

conn = None

def connectDB():
    """Connect to the PostgreSQL database server."""    
    try:
        params = config('src/database.ini')
        conn = psycopg2.connect(**params)
        print(f"Connection is successful to database: {params['database']}")        
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
  # make the connection only once at startup
  conn = connectDB()