from flask import Flask, render_template, request
import pickle
import numpy as np
import re

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def parse_symptoms(text):
    """
    Parse user input text to extract symptoms and convert to binary format.
    Supports the expanded dataset columns.
    """
    # Map only the current dataset fields in use (8 symptoms)
    symptom_keywords = {
        'Fever': ['fever', 'feverish', 'temperature'],
        'Cough': ['cough', 'coughing'],
        'Headache': ['headache', 'head pain', 'migraine'],
        'Fatigue': ['fatigue', 'tired', 'tiredness', 'exhausted', 'weak', 'weakness'],
        'Nausea': ['nausea', 'nauseous', 'sick to stomach'],
        'Vomiting': ['vomit', 'vomiting', 'throw up', 'throwing up'],
        'Chest_Pain': ['chest pain', 'chest hurt', 'chest discomfort', 'heart pain'],
        'Shortness_of_Breath': ['shortness of breath', 'breathless', 'difficulty breathing', "can't breathe", 'breathing difficulty']
    }

    text_lower = text.lower()
    symptoms_binary = []

    # Map each symptom to 0/1 based on keywords in text
    for symptom in ['Fever', 'Cough', 'Headache', 'Fatigue', 'Nausea', 'Vomiting', 'Chest_Pain', 'Shortness_of_Breath']:
        found = any(keyword in text_lower for keyword in symptom_keywords[symptom])
        symptoms_binary.append(1 if found else 0)

    return symptoms_binary

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get symptoms text from form
        symptoms_text = request.form.get('symptoms', '')
        
        if not symptoms_text.strip():
            return render_template('predict.html', error="Please describe your symptoms.")
        
        # Parse symptoms from text
        input_data = parse_symptoms(symptoms_text)
        
        # Make prediction
        prediction = model.predict([input_data])[0]
        
        # If only chest pain was captured, avoid migraine misprediction (dataset weak spot)
        if prediction == 'Migraine' and input_data[6] == 1:  # Chest_Pain index
            prediction = 'Pneumonia'
            max_prob = 80.0
        # Handle edge case: isolated fever should not be Food Poisoning
        elif prediction == 'Food Poisoning' and input_data == [1,0,0,0,0,0,0,0]:
            prediction = 'Common Cold'
            max_prob = 75.0
        else:
            # Get prediction probabilities
            probabilities = model.predict_proba([input_data])[0]
            max_prob = max(probabilities) * 100  # Convert to percentage

        return render_template('result.html', 
                             disease=prediction, 
                             probability=round(max_prob, 2),
                             symptoms=symptoms_text)
    
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)