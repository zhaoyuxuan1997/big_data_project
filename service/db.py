#!/usr/bin/env python3
#coding:utf8
from pymongo import MongoClient


uri = 'mongodb://172.50.0.8:27017/'
client = MongoClient(uri)
db = client['covid']


class DB:
    def __init__(self):
        self.db = db

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def find_one(self, collection, data=None):
        return self.db[collection].find_one(data)
