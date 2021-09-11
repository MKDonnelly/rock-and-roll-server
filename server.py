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

    bands = [
        {
          'id': 'led-zeppelin',
          'name': 'Led Zeppelin',
        },
        {
          'id': 'pearl-jam',
          'name': 'Pearl Jam',
        },
        {
          'id': 'foo-fighters',
          'name': 'Foo Fighters',
        },
    ]

    return jsonify(success=True, bands=bands)


@app.route('/v1/songs')
def songs():
    '''
    Returns a list of songs.
    '''

    songs = [
        {
            'title': 'Black Dog',
            'band': 'led-zeppelin',
            'rating': 3,
        },
        {
            'title': 'Yellow Ledbetter',
            'band': 'pearl-jam',
            'rating': 4,
        },
        {
            'title': 'The Pretender',
            'band': 'foo-fighters',
            'rating': 2,
        },
        {
            'title': 'Daughter',
            'band': 'pearl-jam',
            'rating': 5,
        }
    ]

    return jsonify(success=True, songs=songs)


app.run(host='0.0.0.0')
