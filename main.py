
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request


app = Flask(__name__)


uri = "mongodb+srv://kalemmentore868:ZFVtYKgUGLOtriXq@cluster0.p622hsk.mongodb.net/dev?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

app.config['MONGO_URI'] = uri

mongo = PyMongo(app)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/add_question_template', methods=['POST'])
def add_question_template():
    _json = request.json

    # Pulling the fields from the JSON request body
    status = _json['status']
    subject = _json['subject']
    name = _json['name']
    description = _json['description']
    cesc_section = _json['cesc_section']
    objectives = _json.get('objectives', [])
    format = _json.get('format', [])
    text = _json['text']
    type = _json.get('type', [])
    difficulty = _json.get('difficulty', [])
    images = _json['images']
    options = _json.get('options', [])
    formula = _json['formula']
    hint = _json['hint']
    video = _json['video']
    written_solution = _json['written_solution']

    # validation omitted for brevity...

    mongo.db.questionTemplates.insert_many([{
        'status': status,
        'subject': subject,
        'name': name,
        'description': description,
        'cesc_section': cesc_section,
        'objectives': objectives,
        'format': format,
        'text': text,
        'type': type,
        'difficulty': difficulty,
        'images': images,
        'options': options,
        'formula': formula,
        'hint': hint,
        'video': video,
        'written_solution': written_solution
    }])

    resp = jsonify('Question Template added successfully')
    return resp, 200


@app.route('/get_question_templates', methods=['GET'])
def get_question_templates():
    templates = mongo.db.questionTemplates.find()

    # Convert the cursor object to a list
    templates_list = list(templates)

    # Transform the ObjectId from BSON to string, so it can be serialized by json.dumps
    for template in templates_list:
        template["_id"] = str(template["_id"])

    return jsonify(templates_list), 200


@app.route('/get_question_template/<id>', methods=['GET'])
def get_question_template(id):
    try:
        template = mongo.db.questionTemplates.find_one({"_id": ObjectId(id)})

        # Check if the template was found
        if template:
            template["_id"] = str(template["_id"])
            return jsonify(template), 200
        else:
            return jsonify({"error": "Template not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/edit_question_template/<id>', methods=['PUT'])
def edit_question_template(id):
    try:
        _json = request.json
        update_fields = {}

        for key, value in _json.items():
            update_fields[key] = value

        mongo.db.questionTemplates.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_fields}
        )

        return jsonify({"message": "Question Template updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/delete_question_template/<id>', methods=['DELETE'])
def delete_question_template(id):
    try:
        mongo.db.questionTemplates.delete_one({"_id": ObjectId(id)})
        return jsonify({"message": "Question Template deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=9000)
