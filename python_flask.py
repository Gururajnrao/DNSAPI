#/usr/bin/python
import os
import subprocess
import flask
from flask import Flask, jsonify, request
import re
import socket
from socket import gaierror

## Creating a Flask app
app=Flask(__name__)

@app.route('/<domain>',methods=['GET'])
def api_test(domain):
    if(request.method == 'GET'):
      try:  
        x=socket.gethostbyname_ex(domain)
        return jsonify({'ipaddress': x[2]})
      except gaierror:
        return jsonify({'ipaddress': "Non existent domain"})
        

#driver function
if __name__=='__main__':
    app.run(debug=True)


