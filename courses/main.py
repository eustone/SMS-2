from subjects import Subject
import csv,sqlite3

connect = sqlite3()
class Course:

    course_list = []

    def __init__(self,title = '',department=''):
        self._title = title
        self._department = department
        Course.course_list.append(self)

    def get_course_title(self):
        return self._title

    def get_department(self):
        return self._department

    def show_courses(self):
        with open('courses.csv', 'r') as sc:
            data = sc.read()
            print(data)

    def search_course(self,filter):
        with open('courses.csv','r') as searchwrapper:
            print(type(dir(searchwrapper)))
            for i in searchwrapper:
                if filter in i:
                    print("Course: {}".format(i))

    def save_course(self):
        with open('courses.csv','w') as wc:
            for i in Course.course_list:
                wc.writelines(i.get_course_title() + '; ' +  ' ' + i.get_department() + '\n')

    

