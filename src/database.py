import datetime
import psycopg2
from config import config

def get_connection(dbname=None):
    params = config()
    if dbname:
        params['database'] = dbname
    conn = psycopg2.connect(**params)
    return conn

def create_database():
    # Connect to the default database (usually 'postgres')
    conn = get_connection('postgres')
    conn.autocommit = True  # Needed for CREATE DATABASE
    cur = conn.cursor()
    try:
        cur.execute("CREATE DATABASE workhours")
        print("Database 'workhours' created successfully.")
    except psycopg2.errors.DuplicateDatabase:
        print("Database 'workhours' already exists.")
    finally:
        cur.close()
        conn.close()

def create_table():
    # Now connect to the 'workhours' database
    try:
        conn = get_connection('workhours')
        cur = conn.cursor()
        try:
            # Check if table exists
            cur.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public' 
                    AND table_name = 'work_hours'
                );
            """)
            exists = cur.fetchone()[0]
            if exists:
                print("Table 'work_hours' already exists.")
            else:
                cur.execute("""
                    CREATE TABLE work_hours (
                        id SERIAL PRIMARY KEY,
                        consultant_name VARCHAR(100),
                        customer_name VARCHAR(100),
                        start_time TIMESTAMP,
                        end_time TIMESTAMP,
                        lunch_break INTERVAL
                    );
                """)
                print("Table 'work_hours' created successfully.")
        except Exception as e:
            print(f"Error creating table: {e}")
        finally:
            conn.commit()
            cur.close()
            conn.close()
    except Exception as e:
        print(f"Error connecting to database: {e}")

def get_daily_data():
    today = datetime.date.today()
    try:
        conn = get_connection('workhours')
        cur = conn.cursor()
        sql = "SELECT * FROM work_hours WHERE start_time::date = %s"
        cur.execute(sql, (today,))
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching daily data: {e}")
        return []