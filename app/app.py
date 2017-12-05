from flask import Flask, jsonify, request

from app.core import DataStore
from app.core import Model

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: return a front end page that can call /demo or /label
    return ''

@app.route('/demo')
def demo():
    """ Endpoint to see the model's performance on a random test set example. """
    tweet, label = DataStore.get_random_test()
    return_json = Model.predict([tweet])[0]
    return_json['true'] = int(label)
    return jsonify(return_json)

@app.route('/label', methods=['POST'])
def predict():
    """ Applies the model to the 'text' entry of the payload. """
    content = request.json
    return jsonify(Model.predict([content['text']])[0])


if __name__ == '__main__':
    app.run()
