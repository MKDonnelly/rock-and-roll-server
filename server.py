from flask import Flask, jsonify, request

app = Flask(__name__)

@app.after_request
def add_header(response):

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route('/v1/bands')
def bands_route():
    '''
    Returns a list of bands.
    '''

    bands = [
        {'name': 'Led Zeppelin'},
        {'name': 'Pearl Jam'},
        {'name': 'Foo Fighters'},
    ]

    return jsonify(success=True, bands=bands)

app.run(host='0.0.0.0')
