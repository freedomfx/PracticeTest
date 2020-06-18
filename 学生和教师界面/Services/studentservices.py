# _*_ coding:UTF-8 _*_
"""
实现学生操作的功能，继承Services和Check
"""
from check import *
from services import *

class StudentServices(Services,Check):
	def __init__(self,list_all,student_current):
		super(StudentServices, self).__init__()
		self.list_all = list_all
		self.student_current = student_current

	def check(self):
		"""
		校验输入是否有效
		:return:
		#如果返回1，符合要求
		#如果返回2，学号不符合要求
		#如果返回3，姓名不符合要求
		#如果返回4，手机号码不符合要求
		#如果返回5，邮箱地址不符合要求
		"""
		return_number = 0
		if not self.check_sno(self.student_current.sno):
			return_number = 2
		elif not self.check_name(self.student_current.name):
			return_number = 3
		elif not self.check_mobile(self.student_current.mobile):
			return_number = 4
		elif not self.check_email(self.student_current.email):
			return_number = 5
		else:
			return_number = 1

		return return_number


	def add(self):
		"""
		添加学生
		:return:
		"""
		#处理一下Student
		current_student_list = []
		current_student_list.append((self.student_current.sno))
		current_student_list.append((self.student_current.name))
		current_student_list.append((self.student_current.gender))
		current_student_list.append((self.student_current.Birthday))
		current_student_list.append((self.student_current.mobile))
		current_student_list.append((self.student_current.email))
		current_student_list.append((self.student_current.profession))
		current_student_list.append((self.student_current.study_time))

		#当前学生添加到集合中
		self.list_all.append(current_student_list)

	def update(self):
		"""
		修改
		:return:
		"""
		#主要通过循环遍历list，修改信息
		for index in range(len(self.list_all)):
			if self.list_all[index][0] == self.student_current.sno:
				self.list_all[index][1] = self.student_current.name
				self.list_all[index][2] = self.student_current.gender
				self.list_all[index][3] = self.student_current.Birthday
				self.list_all[index][4] = self.student_current.mobile
				self.list_all[index][5] = self.student_current.email
				self.list_all[index][6] = self.student_current.profession
				self.list_all[index][7] = self.student_current.study_time

	def delete(self):
		"""
		删除学生
		:return:
		"""

		#主要通过循环遍历list，删除某条信息
		for index in range(len(self.list_all)):
			if self.list_all[index][0] == self.student_current.sno:
				self.list_all.pop(index)