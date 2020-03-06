from flask import Flask, jsonify, make_response, flash, json, request, url_for, Response
from flask_cors import CORS
from werkzeug.debug.repr import helper
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/items')
def read_string_file():
    ITEMS = []
    with open("text_file.txt", "r") as file:
        for line in file.readlines():
            ITEMS.append(line.rstrip())
    if len(ITEMS) == 0:
        return "Nema podataka u datoteci!"
    elif len(ITEMS) != 0:
        d = {}
        d.update({"ITEMS": ITEMS})
        d.update({"message":"Uspjesno dohvaceni podaci!"})
        return jsonify(d)
    else:
        return "Problem u aplikaciji!"


@app.route('/items/delete', methods=['DELETE'])
def delete_string():
    req_data = request.get_json()
    item = req_data['item']
    items = []
    with open('text_file.txt', 'r') as file:
        for line in file.readlines():
            items.append(line.strip("\n"))

    dict_data = None
    if item in items:
        items.remove(item)
        dict_data = {
            "status": "Uspjesno"
        }
    else:
        dict_data = {
            "status": "Ne postoji"
        }
        return jsonify(dict_data)

    with open("text_file.txt", "w") as f:
        for d in items:
            f.writelines(d + "\n")

    return jsonify({'items':items, 'dict_data':dict_data})

@app.route('/items/post', methods=['POST'])
def append_file():
    req_data = request.get_json()
    item = req_data['item']
    with open("text_file.txt", "a") as f:
        f.write(item)
        f.write("\n")

    items = []
    with open('text_file.txt', 'r') as file:
        for line in file.readlines():
            items.append(line.strip("\n"))

    dict_data = None
    if item in items:
        dict_data = {
            "status": "Uspjesno"
        }
    else:
        dict_data = {
            "status": "Nije dodano"
        }
        return jsonify(dict_data)
    return jsonify({'items': items, 'dict_data': dict_data})


app.run(host='0.0.0.0', port='5010', debug=True)
cors = CORS(app)





