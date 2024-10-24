from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from transformers import pipeline
      
load_dotenv()

app = Flask(__name__)
CORS(app)
      
@app.route('/api/assistant', methods=['POST'])
def assistant():
           data = request.json
           # Use a pipeline as a high-level helper
           messages = [
               {"role": "user", "content": data.get("message", "Who are you?")},
           ]
           pipe = pipeline("text-generation", model="microsoft/DialoGPT-medium")
           chat_response = pipe(messages)
           
           response = {"message": chat_response[0]['generated_text']}
           return jsonify(response)
      
if __name__ == '__main__':
           app.run(debug=True)
