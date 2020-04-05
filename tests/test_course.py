from StudentManagementSystem.courses.main import Course
import pytest

class TestCourse:
    coursetest = Course('MS in Global Leadership','School of Business')
    assert coursetest.show_courses()


