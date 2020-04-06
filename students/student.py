import csv

class Student:
    def __init__(self,name,address,email,dob,phone,guardian):
        self._name     = name 
        self._address  = address
        self._email  = email
        self._dob      = dob 
        self._phone    = phone 
        self._guardian = guardian 

    def getName(self):
        return self._name 

    def getAddress(self):
        return self._address 

    def getEmail(self):
        return self._email

    def getDOB(self):
        return self._dob 
    
    def getPhone(self):
        return self._phone 

    def getGuardian(self):
        return self._guardian


class StudentProfile(Student):
    studentList = []
    def __init__(self):
        with open('students.csv','r') as sl:
            data = sl.read()
            print('Welcome')

    def addStudent(self,name,adddress,email,dob,phone,guardian):
        newStudent = Student(name,adddress,email,dob,phone,guardian)
        self.studentList.append(newStudent)
        print('New Student Record Added')

    def saveStudent(self):
        with open('students.csv', 'w') as ss:
            for i in self.studentList:
                ss.write(i.getName() + ',' + i.getAddress() + ',' + i.getEmail() +  ',' + i.getDOB() + ',' + i.getPhone() + ',' + i.getGuardian() + '\n')


        

        

    


