import csv

class Subject:
    '''Class Subject to describe all subjects '''
    #class attribute
    subject_list = []
    
    def __init__(self,code,name,description=''):
        '''Initializes Subject code,name & 
        description is optonal'''
        self._code = code
        self._name = name
        self._description = description
        Subject.subject_list.append(self)
    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email 
    
    def get_description(self):
        return self._description 


    def save_subject(self):
        #This array will hold the list of subjects in it.
        with open('subjects.csv','w') as f:
            #Read in the subjects table
            for k in self.subject_list:
                f.write(k.get_code() + ',' + k.get_name() + ',' + k.get_description() + '\n')


