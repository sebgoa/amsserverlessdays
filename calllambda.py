#!/usr/bin/env python3


from flask import Flask
from flask import request

import os
import boto3
import json

app = Flask(__name__)

regionName = os.getenv('regionName', default='us-east-1')
functionName = os.getenv('functionName', default='message-dumper')

client = boto3.client('lambda', region_name=regionName)

#    for f in client.list_functions()['Functions']:
#        print(f['FunctionName'])
#        res = json.loads(response['Payload'].read())
#        print(res['body']) 

@app.route('/', methods=['POST', 'GET'])
def call_lambda():
    cevent = json.dumps(request.get_json())
    response = client.invoke(FunctionName=functionName,Payload=cevent)
    res = json.loads(response['Payload'].read())
    return res['body'] 

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)