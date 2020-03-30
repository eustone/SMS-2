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
        #accesing class attribute & appending it with the instance
        Subject.subject_list.append(self)

    def save_subject(self):
        with open('test.csv', 'w') as w:
            for k in self.subject_list:
                w.write(k._code + ',' + k._name + ',' + k._description + '\n' )


