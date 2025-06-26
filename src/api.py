from flask import Flask, request
from service import (db_get_work_hours, 
                     db_get_work_hours_by_id,
                     db_create_work_hours,
                     db_update_work_hours, 
                     db_delete_work_hours,
                     db_validate_work_hours)
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
    data = request.get_json()
    is_valid, result, status = db_validate_work_hours(data)
    if not is_valid:
        return result, status
    db_create_work_hours(result["consultant_name"], result["customer_name"],
                         result["start_time"], result["end_time"], result["lunch_break"])
    return {"success": "work period created for: %s" % result["consultant_name"]}

@app.route("/work_period/<int:id>", methods=['PUT'])
def update_work_hours(id):
    data = request.get_json()
    is_valid, result, status = db_validate_work_hours(data)
    if not is_valid:
        return result, status
    db_update_work_hours(id, result["consultant_name"], result["customer_name"],
                         result["start_time"], result["end_time"], result["lunch_break"])
    return {"success": "updated work hours"}


@app.route('/work_period/<int:id>', methods=['DELETE'])
def delete_work_hours(id):
    try:
        return db_delete_work_hours(id)
    except:
        return {"error": "no such entry"}

if __name__ == "__main__":
    app.run(host='0.0.0.0')