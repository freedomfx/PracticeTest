# _*_ coding:UTF-8 _*_
import re

class Check():
	def check_sno(self,sno):
		"""
		校验学号是否95开头的6位数字
		:param sno:要校验的学号
		:return:
		"""
		pattern = re.compile(r"^95\d{3}$")
		match_result = pattern.match(sno)
		if match_result is None:
			return False
		else:
			return True

	def check_name(self,name:str):
		"""
		校验姓名是否10个字以内
		:param name:要校验的姓名
		:return:
		"""
		#校验长度是否小于10

		if len(name) <= 10 and len(name) >= 2:
			#判断是否是中文
			for item in name:
				if item < '\u4E00' or item >'\u9FA5':
					return False

			#返回True
			return True

		else:
			return False


	def check_gender(self,gender):
		"""
		判断性别是否填入的男或女
		:param gender:要校验的性别
		:return:
		"""
		if gender.strip() in ['男','女']:
			return True
		else:
			return False

	def check_mobile(self,mobile):
		"""
		判断手机号码是否符合要求
		:param mobile:要校验的手机号码
		:return:
		"""
		pattern = re.compile(r'^[1][34578]\d{9}$')
		match_result = pattern.match(mobile)

		if match_result is not None:
			return True
		else:
			return False

	def check_email(self,email):
		"""
		判断邮箱地址是否符合要求
		:param email:要检验的邮箱地址
		:return:
		"""
		pattern = re.compile(r'\w{1,}[@]\w{1,}[.]\w{1,}')
		match_result = pattern.match(email)
		if match_result is not None:
			return True
		else:
			return False




