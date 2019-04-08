"""
this script represents a machine learning API
"""

import os
import pickle
from flask import Flask
from flask import request
from sklearn import linear_model


# creating and saving some model
reg_model = linear_model.LinearRegression()
reg_model.fit([[1., 1., 5.], [2., 2., 5.], [3., 3., 1.]], [0., 0., 1.])
pickle.dump(reg_model, open('some_model.pkl', 'wb'))

debug = os.environ.get('DEBUG', False)
app = Flask(__name__)

@app.route('/')
def index():
    """
        main api route
    """
    return "true"

@app.route('/api', methods=['GET'])
def get_prediction():
    """
        prediction api route
    """
    feature1 = float(request.args.get('f1'))
    feature2 = float(request.args.get('f2'))
    feature3 = float(request.args.get('f3'))
    loaded_model = pickle.load(open('some_model.pkl', 'rb'))
    prediction = loaded_model.predict([[feature1, feature2, feature3]])
    return str(prediction)
