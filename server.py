from flask import Flask, jsonify, request

app = Flask(__name__)

@app.after_request
def add_header(response):

    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

@app.route('/v1/bands')
def bands():
    '''
    Returns a list of bands.
    '''

    blackDog = {
        'title': 'Black Dog',
        'band': 'Led Zeppelin',
        'rating': 3,
    }

    yellowLedbetter = {
        'title': 'Yellow Ledbetter',
        'band': 'Pearl Jam',
        'rating': 4,
    }

    pretender = {
        'title': 'The Pretender',
        'band': 'Foo Fighters',
        'rating': 2,
    }

    daughter = {
        'title': 'Daughter',
        'band': 'Pearl Jam',
        'rating': 5,
    }

    bands = [
        {
          'id': 'led-zeppelin',
          'name': 'Led Zeppelin',
          'songs': [blackDog],
        },
        {
          'id': 'pearl-jam',
          'name': 'Pearl Jam',
          'songs': [yellowLedbetter, daughter],
        },
        {
          'id': 'foo-fighters',
          'name': 'Foo Fighters',
          'songs': [pretender],
        },
    ]

    return jsonify(success=True, bands=bands)

app.run(host='0.0.0.0')
