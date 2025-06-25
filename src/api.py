from flask import Flask, request
from service import (db_get_work_hours, 
                     db_get_work_hours_by_id,
                     db_create_work_hours,
                     db_update_work_hours, 
                     db_delete_work_hours)
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return {"index": True}

############# Routes #############

@app.route('/work_period', methods=['GET'])
def get_all_work_hours():
    try:  
        return db_get_work_hours()
    except:
        return {"error": "no data"}

@app.route('/work_period/<int:id>', methods=['GET'])
def get_work_hours_by_id(id):
    try:
        return db_get_work_hours_by_id(id)
    except:
        return {"error": "no person with id %s" % id}

@app.route("/work_period", methods=['POST'])
def create_work_hours():
    try: 
        data = request.get_json()
        start_time = data['start_time']
        end_time = data['end_time']
        lunch_break = data['lunch_break']
        consultant_name = data['consultant_name']
        customer_name = data['customer_name']
        db_create_work_hours(consultant_name, customer_name, start_time,end_time, lunch_break)
        return {"success": "work period created for: %s" % consultant_name}
    except:
        return {"error": "error creating work period"}

@app.route("/work_period/<int:id>", methods=['PUT'])
def update_work_hours(id):
    try:
        data = request.get_json()
        start_time = data['start_time']
        end_time = data['end_time']
        lunch_break = data['lunch_break']
        consultant_name = data['consultant_name']
        customer_name = data['customer_name']
        db_update_work_hours(id, consultant_name, customer_name, start_time, end_time, lunch_break)
        return {"success": "updated work hours"}
    except:
        return {"error": "error updating work hours"}

@app.route('/work_period/<int:id>', methods=['DELETE'])
def delete_work_hours(id):
    try:
        return db_delete_work_hours(id)
    except:
        return {"error": "no such entry"}

if __name__ == "__main__":
    app.run()