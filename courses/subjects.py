import csv

class Subject:
    '''Class Subject to describe all subjects '''
    #class attribute
    subject_list = []
    
    def __init__(self,code='',name='',description=''):
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

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description 

    def new_subject(self,code,name,description=''):
        new_subj = Subject(code,name,description)
        Subject.subject_list.append(new_subj)
        self.save_subject()
        print('Subject has been added')

    def save_subject(self):
        #This array will hold the list of subjects in it.
        with open("subjects.csv",'w') as f:
            #Read in the subjects table
            for k in self.subject_list:
                f.write(k.get_code() + ',' + k.get_name() + ',' + k.get_description() + '\n')

    def check_all_subjects(self):
        '''List all saved subjects from database'''
        with open('subjects.csv', 'r') as r:
            data = r.read()
            print(data)

    def search_subject(self,filter):
        for i in Subject.subject_list:
            if filter in i.get_code() or filter in i.get_name():
                print('Subject Code: {} Subject Name: {}'.format(i.get_code(),i.get_name()))

