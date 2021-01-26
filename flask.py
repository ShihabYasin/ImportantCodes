# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response, g
from config import logger  # , global_var etc.
from cStringIO import StringIO
from your_module import write_wav_file, some_function

app = Flask (__name__)


@app.route ('/api_route/<params>/', methods=['POST'])
def send_wav_file_as_attachment(params):
    buffer = StringIO ()
    write_wav_file (buffer)  # TODO: write file in buffer
    response = make_response (buffer.getvalue ())
    buffer.close ()
    response.headers['Content-Type'] = 'audio/wav'
    response.headers['Content-Disposition'] = 'attachment; filename=sound.wav'
    return response


@app.before_request
def before_request_callback():
    method, path = request.method, request.path
    ''' logic '''


@app.after_request
def after_request_callback(response):  # response will catch return values from any @app.route(..) that were called
    response_value = response.get_data ()
    ''' do some cleanup task if need'''
    return response


@app.route ('/api_route/<params>/', methods=['POST'])
def send_json_server(params):
    if not request.is_json:
        logger.error ('ERROR 400: Missing JSON in request')
        return jsonify ({'msg': 'Missing JSON in request'}), 400
    json_dict = request.json
    ''' other codes '''
    input_text = json_dict['__field__name__']
    ''' other codes '''
    return_value = '__dummy__'

    return jsonify ({'return_value': 'Hello_World'})


if __name__ == "__main__":
    app.run (host='0.0.0.0', debug=True, port=9341)
