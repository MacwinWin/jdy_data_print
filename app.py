#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 09/27/20 14:03:09
# @File   : app.py

import hashlib
import threading
import json
from pygments import highlight, lexers, formatters
from flask import Flask, request

app = Flask(__name__)

class Handle:
    def __init__(self):
        pass

    def handle(self, payload):
        if payload['op'] == 'data_create':
            colorful_json = self._colorful_json(payload)
            print(colorful_json)
        if payload['op'] == 'data_update':
            colorful_json = self._colorful_json(payload)
            print(colorful_json)
        if payload['op'] == 'data_remove':
            colorful_json = self._colorful_json(payload)
            print(colorful_json)
        if payload['op'] == 'data_recover':
            colorful_json = self._colorful_json(payload)
            print(colorful_json)
        if payload['op'] == 'form_update':
            colorful_json = self._colorful_json(payload)
            print(colorful_json)
        if payload['op'] == 'data_test':
            print('data_test')
    
    def _colorful_json(self, payload):
        formatted_json = json.dumps(payload, indent=4, ensure_ascii=False, sort_keys=True)
        colorful_json = highlight(formatted_json, lexers.JsonLexer(), formatters.TerminalFormatter())
        return colorful_json

    def get_signature(self, nonce, payload, secret, timestamp):
        content = ':'.join([nonce, payload, secret, timestamp]).encode('utf-8')
        m = hashlib.sha1()
        m.update(content)
        #print(content, m.hexdigest())
        return m.hexdigest()
    
@app.route('/', methods=['POST'])
def callback():
    handle = Handle()
    payload = request.data.decode('utf-8')
    #print(payload)
    nonce = request.args['nonce']
    timestamp = request.args['timestamp']
    print('\n' + '\x1b[94m' + str(request.headers) + '\x1b[39;49;00m', end='')
    if request.headers['x-jdy-signature'] != handle.get_signature(nonce, payload, 'test', timestamp):
        return 'fail', 401
    threading.Thread(target=handle.handle, args=(json.loads(payload), )).start()
    return 'success'