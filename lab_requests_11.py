from flask import Blueprint, jsonify
import random

lab3_blueprint = Blueprint('lab3', __name__)

# Новый формат: /lab3/number/<int:param>/
@lab3_blueprint.route('/number/<int:param>/', methods=['GET'])
def generate_number(param):  # Параметр теперь берётся из URL
    random_num = random.uniform(1, 100)
    result = random_num * param
    return jsonify({
        "input_parameter": param,
        "random_multiplier": random_num,
        "result": result
    })