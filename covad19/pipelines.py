# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class MongoPipeline(object):
    collection_name = 'covad-19'

#
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost', #the location of the database
            27017 # The port number of the database
        )
        db = self.conn['Covad_19'] # Create a database
        self.collection = db['covad_table'] #Create a table to store the data

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
