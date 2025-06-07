from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_features = [float(request.form.get(f)) for f in [
            'age', 'sex', 'cp', 'trestbps', 'chol',
            'fbs', 'restecg', 'thalach', 'exang',
            'oldpeak', 'slope', 'ca', 'thal'
        ]]
        final_input = np.array([input_features])
        prediction = model.predict(final_input)[0]
        result = "🔴 High risk detected: Please consult a cardiologist." if prediction == 1 else "🟢 No significant risk detected: Keep up the healthy lifestyle!"
    except Exception as e:
        result = f"Error: {e}"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
