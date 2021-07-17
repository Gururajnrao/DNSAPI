#/usr/bin/python
import os
import subprocess
import flask
from flask import Flask, jsonify, request
import re

## Creating a Flask app
app=Flask(__name__)

@app.route('/<domain>',methods=['GET'])
def api_test(domain):
    if(request.method == 'GET'):
      data = "nslookup"+" "+str(domain)
      output = subprocess.Popen(data,shell=True,stdout=subprocess.PIPE)
      stdout=str(output.communicate())

      x=re.search("Non-authoritative answer:\\\\nName:\\\\t(\w+.\w+)\\\\nAddress:\s(((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))",stdout)
      return jsonify({'data': x.group(2)})


#driver function
if __name__=='__main__':
    app.run(debug=True)


