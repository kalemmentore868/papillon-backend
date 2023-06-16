
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from models.fraction_template import Fraction_Template

app = Flask(__name__)


uri = "mongodb+srv://kalemmentore868:ZFVtYKgUGLOtriXq@cluster0.p622hsk.mongodb.net/dev?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

app.config['MONGO_URI'] = uri

mongo = PyMongo(app)

print(mongo)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/get_fraction_question/<id>', methods=['GET'])
def get_fraction_question(id):
    # Query the MongoDB for the template with the provided id
    question_template_data = mongo.db.questionTemplates.find_one(
        {"_id": ObjectId(id)})

    # If no document was found with the provided id, return an error message
    if question_template_data is None:
        return jsonify({"error": "No question template found with the provided id"}), 404

    # If a document was found, check if the subject is "Fractions"
    if question_template_data['subject'] == "Fractions":
        # Remove the '_id' key from the dictionary
        question_template_data_without_id = {
            key: value for key, value in question_template_data.items() if key != '_id'}

        # Create a Fraction_Template instance with the data from the document (excluding '_id')
        fraction_template = Fraction_Template(
            **question_template_data_without_id)

        # Call the set_question_and_answer method
        fraction_template.set_question_and_answer()

        # Convert the updated Fraction_Template instance back to a dictionary
        question_template_data = fraction_template.to_dict()

    # Return the updated document data as JSON
    return jsonify(question_template_data), 200


@app.route('/add_question_template', methods=['POST'])
def add_question_template():
    _json = request.json

    # Pulling the fields from the JSON request body
    media = _json['media']
    subject = _json['subject']
    question_id = _json['question_id']
    description = _json['description']
    difficulty = _json['difficulty']
    topic = _json['topic']
    subtopic = _json['subtopic']
    question_type = _json['question_type']
    answer = _json['answer']
    csec_section = _json['csec_section']
    hint = _json['hint']
    status = _json['status']
    name = _json['name']
    question_text = _json['question_text']

    # validation omitted for brevity...

    mongo.db.questionTemplates.insert_many([{
        'media': media,
        'subject': subject,
        'question_id': question_id,
        'description': description,
        'difficulty': difficulty,
        'topic': topic,
        'subtopic': subtopic,
        'question_type': question_type,
        'answer': answer,
        'csec_section': csec_section,
        'hint': hint,
        'status': status,
        'name': name,
        'question_text': question_text
    }])

    resp = jsonify('Question Template added successfully')
    return resp, 200


if __name__ == '__main__':
    app.run(debug=True, port=9000)
