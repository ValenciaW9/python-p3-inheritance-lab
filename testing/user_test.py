#!/usr/bin/env python3

from user import User
from teacher import Teacher

class TestUser:

    def test_teacher_initialization(self):
        my_teacher = Teacher("My", "Teacher")
        assert (my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher")