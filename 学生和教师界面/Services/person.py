# _*_ coding:UTF-8 _*_
"""
实体类：
Person:name,gender,birthday,mobile,email
Student(Person):sno,profession,study_time
Teacher(Person):tid,title,college,work_time
"""

class Person:
	def __init__(self,name,gender,Birthday,mobile,email):

		self.name = name
		self.gender = gender
		self.Birthday = Birthday
		self.mobile = mobile
		self.email = email


class Student(Person):
	def __init__(self,sno,name,gender,Birthday,mobile,email,profession,study_time):
		super(Student, self).__init__(name,gender,Birthday,mobile,email)
		self.sno = sno
		self.profession = profession
		self.study_time = study_time

class Teacher(Person):
	def __init__(self,tid,name,gender,Birthday,mobile,email,title,college,work_time):
		super(Teacher, self).__init__(name,gender,Birthday,mobile,email)
		self.tid = tid
		self.title = title
		self.college = college
		self.work_time = work_time
