# _*_ coding:UTF-8 _*_
"""
主要实现读取文件的内容，并写入文件
"""

import os

class File():
	def __init__(self):

		#记录学生信息的文件路径
		self.student_path = '../file/students.txt'
		#记录教师信息的文件路径
		self.teacher_path = '../file/teachers.txt'

		#定义存储所有学生list
		self.list_student_all = []
		#定义存储所有教师list
		self.list_teacher_all = []

		#加载数据
		self.read_from_file()

	def read_from_file(self):

		#=====================读取学生信息=====================
		try:
			with open(self.student_path,mode='r',encoding='utf-8') as fd_student:
				#逐行读取
				current_line = fd_student.readline()
				#判断是否有数据
				while current_line:
					#分割成数组
					student_list = current_line.split(',')
					#直接添加
					self.list_student_all.append(student_list)
					#读取下一行
					current_line = fd_student.readline()
		except Exception as e:
			raise e

		#=====================读取教师信息=====================
		try:
			with open(self.teacher_path, mode='r',encoding='utf-8') as fd_teacher:
				# 逐行读取
				current_line = fd_teacher.readline()
				# 判断是否有数据
				while current_line:
					# 分割成数组
					teacher_list = current_line.split(',')
					# 直接添加
					self.list_teacher_all.append(teacher_list)
					# 读取下一行
					current_line = fd_teacher.readline()

		except Exception as e:
			raise e

	def write_to_file(self):
		#===============把学生信息写入文件===========
		#写入到文件
		try:
			with open(self.student_path,mode='w',encoding='UTF-8') as fd_student:
				fd_student.write('')
			with open(self.student_path,mode='a',encoding='UTF-8') as fd_student:
				for item in self.list_student_all:
					temp = ",".join(item)
					temp = temp.replace('\n','')+'\n'
					fd_student.write(temp)
		except Exception as e:
			raise e

		# ===============把教师信息写入文件===========
		# 写入到文件
		try:
			with open(self.teacher_path, mode='w', encoding='UTF-8') as fd_teacher:
				fd_teacher.write('')
			with open(self.teacher_path, mode='a', encoding='UTF-8') as fd_teacher:
				for item in self.list_teacher_all:
					temp = ",".join(item)
					temp = temp.replace('\n', '') + '\n'
					fd_teacher.write(temp)
		except Exception as e:
			raise e


if __name__ == '__main__':
	file = File()

