
import urllib2
import sys
import os  
import pymongo

def getServerStatus():
    from os import environ
    host = environ.get('MONGO_HOST', '127.0.0.1')
    port = int(environ.get('MONGO_PORT', '27017'))
    user = environ.get('MONGO_USER', '') 
    password = environ.get('MONGO_PASSWORD', '') 

    c = pymongo.MongoClient(host, port)
    if user != '' and password != '': 
        c.admin.authenticate(user, password)
    return c.admin.command('serverStatus', workingSet=True)

