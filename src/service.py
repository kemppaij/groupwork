import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json

from functools import cache
@cache
def get_conn():
    return psycopg2.connect(**config())

def db_get_work_hours():
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM work_hours;'
        cursor.execute(SQL)
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({"work_hours": data})
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_get_work_hours_by_id(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'SELECT * FROM work_hours where id = %s;'
        cursor.execute(SQL, (id,))
        data = cursor.fetchall()
        cursor.close()
        return json.dumps({"work_hours": data})
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    finally:
        if con is not None:
            con.close()

def db_create_work_hours(consultant_name, customer_name, start_time, end_time, lunch_break):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO work_hours (consultant_name, customer_name, start_time,end_time, lunch_break) VALUES (%s, %s, %s, %s, %s);'
        cursor.execute(SQL, (consultant_name, customer_name, start_time,end_time, lunch_break))
        con.commit()
        result = {"success": "work period created for: %s " % consultant_name}
        cursor.close()
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()


def db_update_work_hours(id, consultant_name, customer_name, start_time, end_time, lunch_break):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'UPDATE person SET consultant_name = %s, customer_name = %s, start_time = %s, end_time = %s, lunch_break = %s WHERE id = %s;'
        cursor.execute(SQL, (consultant_name, customer_name, start_time, end_time, lunch_break, id))
        con.commit()
        cursor.close()
        result = {"success": "work_hours updated for consultant id: %s " % id}
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

def db_delete_work_hours(id):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'DELETE FROM work_hours WHERE id = %s;'
        cursor.execute(SQL, (id,))
        con.commit()
        cursor.close()
        result = {"success": "deleted work hours for id: %s " % id}
        return json.dumps(result)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()
