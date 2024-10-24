from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore



# Initialize Firebase
cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()
app = Flask(__name__)
CORS(app)



@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message":  "hello"})

@app.route('/api/getuser/<user_id>', methods= ['GET'])

def getUser(user_id):

    try:

        user_ref = db.collection('users').document(user_id)
        doc = user_ref.get()

        if doc.exists:
            user_data = doc.to_dict()
            return jsonify(user_data), 200
        else:
            return jsonify({"error": "User not found"}), 404
        
    
    except Exception as e:
         print(f"Error getting users: {str(e)}")
         return jsonify({"error": str(e)}), 500
   





@app.route('/api/user', methods=['POST'])
def create_user():
    try:


  
        user_data = request.json
        name = user_data.get('name', '')
        email = user_data.get('email')
        user_id = user_data.get('userId')
        business = user_data.get('business', '')
        mobile_number = user_data.get('mobileNumber', '')
        position = user_data.get('position', '')
        address = user_data.get('address', '')  
        business_type = user_data.get('businessType', '')  
        num_of_employees = user_data.get('numberOfEmployees', 0)
        business_id = user_data.get('businessId',0)
        
        # Print the extracted values
        print(f"Email: {email}")
        print(f"User ID: {user_id}")
        
        if not email or not user_id:
            return jsonify({'error': 'Missing required fields'}), 400
      
        doc_ref = db.collection('users').document(user_id)
        doc_ref.set({
            'email': email,
            'userId': user_id,
            'name': name,
            'business':business,
            'business_type': business_type,
            'mobilenumber':mobile_number,
            'positon': position,
            'address': address,
            'numofemploys': num_of_employees,
            'business_id' :business_id,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        
        
        return jsonify({'message': 'User data stored successfully'}), 200

        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/user/<user_id>/department', methods=['POST'])
def create_department(user_id):
    try:
        department_data =  request.json
        department_name = department_data.get('name')
        print(f"department:{department_name}")
        if not department_name:
            return jsonify({'error':'Missing department name'}),400
        
        department_ref = db.collection('users').document(user_id).collection('departments').document()
        department_ref.set({
            'name': department_name,
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        return jsonify({'message': 'Yahoo department created', 'id': department_ref.id})
    except Exception as e:
        return jsonify({"error": str(e)}),500
    
@app.route('/api/get_departments/<user_id>/departments', methods=['GET'])
def get_departments(user_id):
    try:
        document_ref = db.collection('users').document(user_id).collection('departments')
        departments = document_ref.stream()
        department_list = []
        for department in departments:
            department_list.append({**department.to_dict(),"id":department.id})
        return jsonify(department_list), 200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@app.route('/api/<user_id>/department/<department_id>/role',methods= ['POST'])
def create_role(user_id,department_id):
    try:
        role_date = request.json
        role_name = role_date['name']
        document_ref = db.collection('users').document(user_id).collection('departments').document(department_id).collection('roles').document()
        document_ref.set({
            'name':role_name,
            'timestamp':firestore.SERVER_TIMESTAMP
        })
        return jsonify({'message': 'Role added successfully', 'role_id':document_ref.id}),200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    
@app.route('/api/<user_id>/department/<department_id>/role', methods=['GET'])
def get_role(user_id, department_id):
    try:
        document_ref = db.collection('users').document(user_id).collection('departments').document(department_id).collection('roles')
        roles = document_ref.stream()
        roles_list= []
        for role in roles:
            roles_list.append({**role.to_dict(), "id":role.id})
        return jsonify(roles_list),200
    except Exception as e:
        return jsonify({'error': str(e)}),500
    
@app.route('/api/user/<user_id>/employee', methods=['POST'])
def create_employee(user_id):
    try:
        employee_data = request.json
        email = employee_data.get('email')
        name = employee_data.get('name')
        department_id = employee_data.get('department_id')
        role = employee_data.get('role')

        if not email or not name:
            return jsonify({'error': 'Missing required fields'}), 400

        employee_ref = db.collection('users').document(user_id).collection('employees').document()
        employee_ref.set({
            'email': email,
            'name': name,
            'department_id': department_id,
            'role': role,
            'timestamp': firestore.SERVER_TIMESTAMP
        })

        return jsonify({'message': 'Employee created successfully', 'employee_id': employee_ref.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/api/<user_id>/employee', methods=['GET'])
def get_employee(user_id):
    try:
        document_ref = db.collection('users').document(user_id).collection('employees')
        employees = document_ref.stream()
        employees_list = []
        for employee in employees:
            employees_list.append({**employee.to_dict(), "id": employee.id})
        return jsonify(employees_list),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/user/<user_id>/shifts', methods=['POST'])
def create_shift(user_id):
    try:
        shift_data = request.json
        department = shift_data.get('department')
        role = shift_data.get('role')
        date = shift_data.get('date')
        start = shift_data.get('start')
        end = shift_data.get('end')
        employee = shift_data.get('employee')
        place = shift_data.get('place')
        shift_ref = db.collection('users').document(user_id).collection('shifts').document()
        shift_ref.set({
            'department': department,
            'role': role,
            'date': date,
            'start': start,
            'end': end,
            'employee': employee,
            'place': place,
        })
        return jsonify({'message': 'shift created successfully', 'shiftid': shift_ref.id}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/api/<user_id>/shifts', methods=['GET'])
def get_shifts(user_id):
    try:
        document_ref = db.collection('users').document(user_id).collection('shifts')
        shifts = document_ref.stream()
        shifts_list = []
        for shift in shifts:
            shifts_list.append({**shift.to_dict(), "id":shift.id})
        return jsonify(shifts_list),200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@app.route('/api/<user_id>/verify', methods=['GET'])
def verify_user(user_id):
    try:
        email = request.args.get('email')
        
        if not email:
            return jsonify({'error': 'Email is required'}), 400

        owner_ref = db.collection('users').document(user_id)
        owner_doc = owner_ref.get()
        
        if not owner_doc.exists:
            return jsonify({'error': 'Invalid login key'}), 404
        
      
        employees_ref = owner_ref.collection('employees')

        query = employees_ref.where(field_path='email', op_string='==', value=email).limit(1)
        
        matching_employees = list(query.stream())
        
        if not matching_employees:
            return jsonify({'error': 'No employee found with this email'}), 404
        
        employee = matching_employees[0]
        employee_data = employee.to_dict()
        
        return jsonify({
            'success': True,
            'employeeId': employee.id,
            'employeeData': {
                'name': employee_data.get('name'),
                'role': employee_data.get('role'),
                'department_id': employee_data.get('department_id'),
                'email': employee_data.get('email')
            }
        }), 200

    except Exception as e:
        print(f"Error in verify_user: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
@app.route('/api/<user_id>/emplyShifts', methods=['GET'])
def get_employee_shifts(user_id):
    try:

        employee_name = request.args.get('name')
        
        if not employee_name:
            return jsonify({"error": "Employee name is required"}), 400


        shifts_ref = db.collection('users').document(user_id).collection('shifts')
        

        shifts = shifts_ref.stream()
        
        matching_shifts = []
        
    
        for shift in shifts:
            shift_data = shift.to_dict()
            

            if ('employee' in shift_data and 
                'name' in shift_data['employee'] and 
                shift_data['employee']['name'] == employee_name):
                
 
                shift_data['shift_id'] = shift.id
                matching_shifts.append(shift_data)
        
        return jsonify({
            "shifts": matching_shifts,
            "count": len(matching_shifts)
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to fetch shifts",
            "message": str(e)
        }),         


    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')