import csv
import sqlite3

class Subject(object):
    """Class for subjects """
    subject_list = []
    def __init__(self,code,name,description=''):
        #Init method to initialise code,name,description at instance formation
        if not isinstance(code,str):
            raise("Code must contain words only.")        
        self._code        = code
        if not isinstance(name,str):
            raise("Name must contain words only")
        self._name        = name
        if not isinstance(description,str):
           raise("Description must be words only")
        self._description = description
        Subject.subject_list.append(self)

