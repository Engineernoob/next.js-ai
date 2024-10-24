from flask import Flask, request, jsonify
from flask_cors import CORS
      
app = Flask(__name__)
CORS(app)
      
@app.route('/api/assistant', methods=['POST'])
def assistant():
           data = request.json
           # Process data and interact with OpenAI API
           response = {"message": "Hello from Flask!"}
           return jsonify(response)
      
if __name__ == '__main__':
           app.run(debug=True)
