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
           # Initialize a Hugging Face pipeline with DialoGPT
           chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
           
           # Example usage of the pipeline
           user_input = data.get("message", "Hello!")
           chat_response = chatbot(user_input, max_length=100, num_return_sequences=1)
           
           response = {"message": chat_response[0]['generated_text']}
           return jsonify(response)
      
if __name__ == '__main__':
           app.run(debug=True)
