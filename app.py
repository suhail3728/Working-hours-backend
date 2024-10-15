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
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')