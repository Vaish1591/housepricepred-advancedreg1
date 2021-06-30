import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model9.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    float_features = [float(x) for x in request.form.values()]
    final_features = np.array([float_features])
    
    prediction = model.predict(final_features)

    
    output = round(prediction[0], 5)

    return render_template('index.html', prediction_text='House price estimated should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

