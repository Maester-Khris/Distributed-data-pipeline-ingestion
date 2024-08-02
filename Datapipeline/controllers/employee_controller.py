from flask import Blueprint, render_template, jsonify, request, make_response

# In-Memory DB
employees = [{'id': 1, 'name': 'Ashley'}, {'id': 2, 'name': 'Kate'}, {'id': 3, 'name': 'Joe'}]

employee_bp = Blueprint('employee', __name__)

@employee_bp.route('/', methods=['GET'])
def demo():
    return "Welcome to the newly created api by NK-py, Let's do something great !"

@employee_bp.route('/', methods=['GET'])
def get_employees():
    return jsonify(employees)

@employee_bp.route('/latest', methods=['GET'])
def get_latest_employees():
    employee = employees[-1]
    return jsonify(employee)

@employee_bp.route('/<int:id>', methods=['GET'])
def get_one_employee(id: int):
    employee = next((e for e in employees if e['id'] == id), None)
    if employee is None:
        return jsonify({'error':'Employee with id {0} not found'.format(id)}), 404
    return jsonify(employee)

@employee_bp.route('/new', methods=['POST'])
def add_employee():
    data = request.get_json()
    emp = dict.fromkeys(['id','name'])
    emp['id'] = len(employees)+1
    emp['name'] = data.get('name')
    employees.append(emp);
    print(data)
    return make_response("Data well received")