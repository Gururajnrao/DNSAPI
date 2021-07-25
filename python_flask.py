#/usr/bin/python
import os
import logging
import flask
import sys
from flask import Flask, jsonify, request
import re
import socket
from socket import gaierror

## Creating a Flask app

class dnsapi (object):
    """
        Class to host the API to get domain name and give IPs as response
    """
  def __init__(self):
      self.logger = logging.getLogger("DNSAPI")
      if not self.logger.hasHandlers():
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.app=Flask(__name__)
  
  @self.app.route('/<domain>',methods=['GET']) 
  def route(self,domain):
      if(request.method == 'GET'):
        try:  
          self.x=socket.gethostbyname_ex(domain)
          return jsonify({'ipaddress': self.x[2]})
          self.logger.info("IP address is retrieved")
        except gaierror:
          self.logger.info("Invalid domain")
          return jsonify({'ipaddress': "Non existent domain"})

  def run(self):
    self.app.run(debug=True)  

#driver function
if __name__=='__main__':
   a = dnsapi()
   a.run()


