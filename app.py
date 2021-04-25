import os

import pymongo
from bson.decimal128 import Decimal128
from bson.objectid import ObjectId
from cerberus import Validator
from flask import Flask, request

app = Flask(__name__)

client = pymongo.MongoClient(os.environ.get("DATABASE_URL"))
db = client["or"]


@app.route("/api/v1/drivers/<lng>/<lat>")
def rides_index(lng, lat):
    drivers_cursor = db.drivers.find({
        "loc": {
            "$near": {
                "$geometry": {
                    "type": "Point",
                    "coordinates":  [Decimal128(lng), Decimal128(lat)]
                },
                "$maxDistance": 200,
                "$minDistance": 0
            }
        }
    })
    drivers = []
    for driver in drivers_cursor:
        drivers.append({
            "_id": str(driver["_id"]),
            "name": driver["name"],
            "licence": driver["license"],
            "location": {
                "lng": str(driver["loc"]["coordinates"][0]),
                "lat":  str(driver["loc"]["coordinates"][1])
            }
        }
        )
    return {"drivers": drivers}


@app.route("/api/v1/drivers/location", methods=["POST"])
def rides_update():
    req_validator = Validator({
        "id": {"type": "string", "required": True},
        "lng": {"type": "string", "required": True},
        "lat": {"type": "string", "required": True},
    })
    req_data = request.get_json()
    if req_validator.validate(req_data):
        driver_id = req_data["id"]
        lng = Decimal128(req_data["lng"])
        lat = Decimal128(req_data["lat"])
        try:
            db.drivers.update_one({"_id": ObjectId(driver_id)}, {"$set": {
                "loc.coordinates": [lng, lat]}
            })
        except:
            return {"msg": "something went wrong please try again"}, 500
        return {
            "msg": "location updated successfully"
        }
    return req_validator.errors, 400
