import os
import datetime
from mongoengine import connect, Document, StringField, DateTimeField
uri = os.getenv('MLAB_URI')
connect(host=uri)

class Notebook(Document):
    '''
    This collection defines how our notes document will look
    '''
    title = StringField(max_length=100, required=True)
    notes = StringField(max_length=500, required=True)
    date_modified = DateTimeField(default=datetime.datetime.now)
