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
           # Initialize a Hugging Face pipeline
           sentiment_analysis = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
           
           # Example usage of the pipeline
           analysis = sentiment_analysis("I love using Hugging Face!")
           
           response = {"message": f"Sentiment analysis result: {analysis}"}
           return jsonify(response)
      
if __name__ == '__main__':
           app.run(debug=True)
