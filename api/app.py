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
    return "true"

@app.route('/api', methods=['GET'])
def get_prediction():
    feature1 = float(request.args.get('f1'))
    feature2 = float(request.args.get('f2'))
    feature3 = float(request.args.get('f3'))
    loaded_model = pickle.load(open('some_model.pkl', 'rb'))
    prediction = loaded_model.predict([[feature1, feature2, feature3]])
    return str(prediction)

# if __name__ == '__main__':
#     # if os.environ['ENVIRONMENT'] == 'production':
#     #     app.run(port=80,host='0.0.0.0')
#     # if os.environ['ENVIRONMENT'] == 'local':
#     app.run(debug=debug, port=5000,host='0.0.0.0')
