from flask import Flask, jsonify, send_from_directory
import os

from Arrow import *
from Charge import *
from EquipotentialLines import *

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/get_arrow', methods=['GET'])
def arrow_data():
    print("get_arrow")
    arrow_data = []
    # For loop of data points for arrows
    for i in range(int(WIDTH / (100 / DETAIL))):
        for j in range(int(HEIGHT / (50 / DETAIL))):
            a = Arrow((i * 104 / DETAIL, j * 104 / DETAIL))
            arrow_data.append(a.draw())
    print(jsonify(arrow_data))
    return jsonify(arrow_data)

@app.route('/api/get_point_charges')
def get_point_charges():
    print(f"point_charges {(PointCharge.instances)}")
    point_charges = []
    # Point Charge Dots
    for pointCharge in PointCharge.instances:
        point_charges.append([pointCharge.xy[0], pointCharge.xy[1]])

    return jsonify(point_charges)


@app.route('/api/get_test_charges')
def get_test_charges():
    test_charges = []
    # Point Charge Dots
    for testCharge in Charge.instances:
        test_charges.append([testCharge.xy[0], testCharge.xy[1]])

    return jsonify(test_charges)


x = PointCharge((300, 250), -e)
y = PointCharge((700, 250), -e)
l = PointCharge((500, 109), -e)

z = Charge((100, 100))


if __name__ == '__main__':
    app.run(port=5000)