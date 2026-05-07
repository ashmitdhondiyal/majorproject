# AI Disease Prediction System

A modern, professional healthcare AI web application that predicts diseases based on user-reported symptoms using machine learning.

## Features

- **Symptom-based Disease Prediction**: Uses AI/ML to predict diseases from symptoms
- **Modern UI**: Clean, responsive design with medical-themed colors
- **Real-time Analysis**: Instant predictions with confidence scores
- **Educational Tool**: Includes medical disclaimers and health awareness information
- **Mobile-Friendly**: Fully responsive design for all devices

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, TailwindCSS
- **Backend**: Python Flask
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Processing**: Pandas
- **Model Serialization**: Pickle

## Project Structure

```
AI-Disease-Prediction/
│
├── app.py                 # Flask application
├── train_model.py         # ML model training script
├── model.pkl             # Trained ML model (generated)
├── dataset.csv           # Symptom-disease dataset
│
├── templates/
│   ├── index.html        # Homepage
│   ├── predict.html      # Symptom input form
│   └── result.html       # Prediction results
│
├── static/
│   ├── style.css         # Custom styles
│   └── script.js         # JavaScript functionality
│
└── README.md             # This file
```

## Installation & Setup

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
pip install flask scikit-learn pandas
```

### Step 2: Train the ML Model

```bash
python train_model.py
```

This will create a `model.pkl` file containing the trained Random Forest model.

### Step 3: Run the Flask Application

```bash
python app.py
```

### Step 4: Access the Application

Open your web browser and go to: `http://localhost:5000`

## Usage

1. **Homepage**: View information about the system and its benefits
2. **Symptom Checker**: Select symptoms you're experiencing
3. **Prediction Results**: View AI-predicted disease with confidence score
4. **Disclaimer**: Always consult healthcare professionals for actual diagnosis

## Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Features**: 8 symptom inputs (Fever, Cough, Headache, etc.)
- **Target**: Disease prediction
- **Training Data**: Symptom-disease dataset with binary symptom indicators

## Important Notes

- **Educational Purpose Only**: This system is NOT a substitute for professional medical advice
- **No Medical Diagnosis**: Predictions are based on patterns in training data only
- **Privacy**: No user data is stored or transmitted
- **Disclaimer**: Always consult qualified healthcare providers for health concerns

## Customization

- **Dataset**: Modify `dataset.csv` to add more diseases or symptoms
- **Model**: Adjust parameters in `train_model.py` for different ML algorithms
- **UI**: Update templates and styles for different themes or layouts

## License

This project is for educational purposes. Please ensure compliance with medical data privacy regulations when deploying similar systems.

## Contributing

Feel free to contribute improvements, bug fixes, or additional features!