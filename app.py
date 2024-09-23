from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("config/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Flask milk pizza hashireeeee!"})

@app.route('/api/items', methods=['POST'])
def create_item():
    try:
        item = request.json
        doc_ref = db.collection('items').add(item)
        return jsonify({"id": doc_ref[1].id, "message": "Item created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/items', methods=['GET'])
def read_items():
    try:
        all_items = [{"id": doc.id, **doc.to_dict()} for doc in db.collection('items').stream()]
        return jsonify(all_items), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/items/<item_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_item(item_id):
    if item_id == 'undefined':
        return jsonify({"error": "Invalid item ID"}), 400

    item_ref = db.collection('items').document(item_id)
    
    if not item_ref.get().exists:
        return jsonify({"error": "Item not found"}), 404

    if request.method == 'GET':
        try:
            item = item_ref.get()
            return jsonify({"id": item.id, **item.to_dict()}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'PUT':
        try:
            item = request.json
            item_ref.update(item)
            return jsonify({"message": "Item updated successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == 'DELETE':
        try:
            item_ref.delete()
            return jsonify({"message": "Item deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')