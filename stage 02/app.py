from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    json_data = request.get_json()

    operation_type = json_data['operation_type']
    x_value = json_data['x']
    y_value = json_data['y']

    if operation_type == 'addition':
        result = x_value + y_value
    if operation_type == 'subtraction':
        result = x_value - y_value
    if operation_type == 'multiplication':
        result = x_value * y_value

    return jsonify(
        slackUsername='daily_tee',
        result=result,
        operation_type=operation_type
    )