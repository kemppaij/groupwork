import psycopg2
from psycopg2.extras import RealDictCursor
from config import config
import json
from datetime import datetime

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
        return json.dumps({"work_hours": data}, default=str)
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
        return json.dumps({"work_hours": data}, default=str)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return json.dumps({"error": str(error)})
    finally:
        if con is not None:
            con.close()


def db_create_work_hours(consultant_name, customer_name, start_time, end_time, lunch_break):
    con = None
    try:
        con = psycopg2.connect(**config())
        cursor = con.cursor(cursor_factory=RealDictCursor)
        SQL = 'INSERT INTO work_hours (consultant_name, customer_name, start_time, end_time, lunch_break) VALUES (%s, %s, %s, %s, %s);'
        cursor.execute(SQL, (consultant_name, customer_name, start_time, end_time, lunch_break))
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
        SQL = '''
            UPDATE work_hours
            SET consultant_name = %s,
                customer_name = %s,
                start_time = %s,
                end_time = %s,
                lunch_break = %s
            WHERE id = %s;
        '''
        cursor.execute(SQL, (consultant_name, customer_name, start_time, end_time, lunch_break, id))
        con.commit()
        cursor.close()
        result = {"success": f"work_hours updated for consultant id: {id}"}
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



def db_validate_work_hours(data):
    start_time_str = data.get('start_time')
    end_time_str = data.get('end_time')
    lunch_break_raw = data.get('lunch_break')  # kan vara string eller int
    consultant_name = data.get('consultant_name')
    customer_name = data.get('customer_name')

    if not all([start_time_str, end_time_str, lunch_break_raw is not None, consultant_name, customer_name]):
        return False, {"error": "All fields are required"}, 400

    try:
        start_time = datetime.fromisoformat(start_time_str)
        end_time = datetime.fromisoformat(end_time_str)
    except ValueError:
        return False, {"error": "Invalid datetime format"}, 400

    try:
        lunch_break = int(lunch_break_raw)
    except ValueError:
        return False, {"error": "Lunch break must be an integer"}, 400

    if start_time >= end_time:
        return False, {"error": "End time must be after start time"}, 400

    if lunch_break < 0:
        return False, {"error": "Lunch break cannot be negative"}, 400

    total_work_seconds = (end_time - start_time).total_seconds()
    if lunch_break * 60 > total_work_seconds:
        return False, {"error": "Lunch break exceeds total working time"}, 400

    return True, {
        "start_time": start_time,
        "end_time": end_time,
        "lunch_break": lunch_break,
        "consultant_name": consultant_name,
        "customer_name": customer_name
    }, 200
