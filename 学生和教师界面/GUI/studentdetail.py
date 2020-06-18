# _*_ coding:UTF-8 _*_
"""
实现学生明细的GUI 由BaseDetail派生而来
"""
from basedetail import *
import sys,os
from studentservices import *
from person import *

class StudentDetail(BaseDetail):
	def __init__(self,flag:int,current_student='',list_student_all=''):
		super(StudentDetail, self).__init__()
		#修改title
		self.Label_title['text'] = '学生明细信息'
		self.userinfo = 0
		#接收值
		self.flag = flag
		self.current_student = current_student
		self.list_student_all = list_student_all
		#修改style
		self.Style01.configure('Detail.TLabel',font=('微软雅黑',14,'bold'),foreground='Navy',background='SpringGreen')
		self.Style01.configure('TRadiobutton', font=('微软雅黑', 12, 'bold'), foreground='navy', background='SpringGreen')

		#调用student_detail元素加载
		self.setup_student_detail()

		#根据flag初始化窗口
		self.load_gui_by_flag()


	def setup_student_detail(self):
		#添加StudentDetail内容
		#=======学号========
		self.Label_sno = Label(self.Pane_detail,text='学号：',style='Detail.TLabel')
		self.Label_sno.place(x=140,y=20)
		self.var_sno = StringVar()
		self.Entry_sno = Entry(self.Pane_detail,textvariable = self.var_sno,font=('微软雅黑',12,'bold'),width=10)
		self.Entry_sno.place(x=210,y=21)

		#=======姓名========
		self.Label_name = Label(self.Pane_detail,text='姓名：',style='Detail.TLabel')
		self.Label_name.place(x=140,y=65)
		self.var_name = StringVar()
		self.Entry_name = Entry(self.Pane_detail,textvariable=self.var_name,font=('微软雅黑',12,'bold'),width=10)
		self.Entry_name.place(x=210,y=66)

		#=======性别========
		self.Label_gender = Label(self.Pane_detail,text='性别：',style='Detail.TLabel')
		self.Label_gender.place(x=140,y=110)
		self.var_gender = IntVar()
		self.Radio_man = Radiobutton(self.Pane_detail,text='男',variable = self.var_gender,value=1)
		self.Radio_man.place(x=220,y=112)
		self.Radio_woman = Radiobutton(self.Pane_detail,text='女',variable = self.var_gender,value=2)
		self.Radio_woman.place(x=270,y=112)

		#=======出生日期=======
		self.Label_Birthday = Label(self.Pane_detail,text='出生日期：',style='Detail.TLabel')
		self.Label_Birthday.place(x=100,y=155)
		self.var_Birthday = StringVar()
		self.Entry_Birthday = Entry(self.Pane_detail,textvariable=self.var_Birthday,font=('微软雅黑',12,'bold'),width=10)
		self.Entry_Birthday.place(x=210,y=157)

		#=======手机号码========
		self.Label_mobile = Label(self.Pane_detail,text='手机号码：',style='Detail.TLabel')
		self.Label_mobile.place(x=100,y=200)
		self.var_mobile = StringVar()
		self.Entry_mobile = Entry(self.Pane_detail,textvariable=self.var_mobile,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_mobile.place(x=210,y=202)

		#=======邮件地址========
		self.Label_email = Label(self.Pane_detail,text='邮件地址：',style='Detail.TLabel')
		self.Label_email.place(x=100,y=245)
		self.var_email = StringVar()
		self.Entry_email = Entry(self.Pane_detail,textvariable=self.var_email,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_email.place(x=210,y=247)

		#=======所学专业=========
		self.Label_profession = Label(self.Pane_detail,text='所学专业：',style='Detail.TLabel')
		self.Label_profession.place(x=100,y=290)
		self.var_profession = StringVar()
		self.Entry_profession = Entry(self.Pane_detail,textvariable=self.var_profession,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_profession.place(x=210,y=292)

		#=======入学时间=========
		self.Label_study_time = Label(self.Pane_detail,text='入学时间：',style='Detail.TLabel')
		self.Label_study_time.place(x=100,y=335)
		self.var_study_time = StringVar()
		self.Entry_study_time = Entry(self.Pane_detail,textvariable=self.var_study_time,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_study_time.place(x=210,y=337)

	def load_gui_by_flag(self):
		"""
		根据flag的值加载不同的GUI状态
		:return:
		"""
		if self.flag == 1:
			#1.查看窗口状态
			self.Label_title['text'] = '==查看学生明细=='
			#2.隐藏保存按钮
			self.Button_save.place_forget()
			#3.填充数据
			self.var_sno.set(self.current_student[0])
			self.var_name.set(self.current_student[1])
			if '男' in self.current_student[2]:
				self.var_gender.set(1)
			else:
				self.var_gender.set(2)
			self.var_Birthday.set(self.current_student[3])
			self.var_mobile.set(self.current_student[4])
			self.var_email.set(self.current_student[5])
			self.var_profession.set(self.current_student[6])
			self.var_study_time.set(self.current_student[7])

			#禁用entry
			self.Entry_sno['state'] = DISABLED
			self.Entry_name['state'] = DISABLED
			self.Radio_man['state'] = DISABLED
			self.Radio_woman['state'] = DISABLED
			self.Entry_Birthday['state'] = DISABLED
			self.Entry_mobile['state'] = DISABLED
			self.Entry_email['state'] = DISABLED
			self.Entry_profession['state'] = DISABLED
			self.Entry_study_time['state'] = DISABLED


		elif self.flag == 2:
			#修改窗口状态
			self.Label_title['text'] = '==修改学生明细=='
			#填充数据
			self.var_sno.set(self.current_student[0])
			self.var_name.set(self.current_student[1])
			if '男' in self.current_student[2]:
				self.var_gender.set(1)
			else:
				self.var_gender.set(2)
			self.var_Birthday.set(self.current_student[3])
			self.var_mobile.set(self.current_student[4])
			self.var_email.set(self.current_student[5])
			self.var_profession.set(self.current_student[6])
			self.var_study_time.set(self.current_student[7])

			#禁用entry
			self.Entry_sno['state'] = DISABLED

		elif self.flag == 3:
			#添加窗口状态
			self.Label_title['text'] = '==添加学生明细=='

	def commit(self):
		"""
		点击保存按钮响应的事件
		:return:
		"""
		# showinfo('系统消息', '你点击了保存按钮!')
		super().commit()
		if self.flag == 3:

			#1.封装当前行的学生信息
			current_student = self.get_current_student()
			current_studentservices = StudentServices(self.list_student_all,current_student)

			#2.校验学生
			return_number = current_studentservices.check()
			if return_number == 2 :
				showinfo('系统消息','学号不符合要求')
			elif return_number == 3:
				showinfo('系统消息', '姓名不符合要求')
			elif return_number == 4:
				showinfo('系统消息', '手机号码不符合要求')
			elif return_number == 5:
				showinfo('系统消息', '邮箱地址不符合要求')
			# elif return_number == 1:
			# 	showinfo('系统消息', '恭喜您所有都符合要求')

				#3.添加功能
			if return_number == 1:
				current_studentservices.add()

				#4.提示 添加成功
				showinfo('系统消息','学员信息添加成功')

			#5.反馈信号给主窗体
			self.userinfo = 1

			#6.关闭
			self.destroy()

		elif self.flag == 2:
			# 1.封装当前行的学生信息
			current_student = self.get_current_student()
			current_studentservices = StudentServices(self.list_student_all, current_student)

			# 2.校验学生
			return_number = current_studentservices.check()
			if return_number == 2:
				showinfo('系统消息', '学号不符合要求')
			elif return_number == 3:
				showinfo('系统消息', '姓名不符合要求')
			elif return_number == 4:
				showinfo('系统消息', '手机号码不符合要求')
			elif return_number == 5:
				showinfo('系统消息', '邮箱地址不符合要求')
			# elif return_number == 1:
			# 	showinfo('系统消息', '恭喜您所有都符合要求')

			# 3.添加功能
			if return_number == 1:
				current_studentservices.update()

				# 4.提示 添加成功
				showinfo('系统消息', '学员信息修改成功')

			# 5.反馈信号给主窗体
			self.userinfo = 1

			# 6.关闭
			self.destroy()

	def get_current_student(self):
		"""
		将当前的信息封装到student类
		:return:
		"""
		sno = self.var_sno.get()
		name = self.var_name.get()
		gender = ''
		if self.var_gender.get() == 1 :
			gender = '男'
		elif self.var_gender.get() ==2 :
			gender = '女'

		Birthday = self.var_Birthday.get()
		mobile = self.var_mobile.get()
		email = self.var_email.get()
		profession = self.var_profession.get()
		study_time = self.var_study_time.get()

		#封装
		current_student = Student(sno,name,gender,Birthday,mobile,email,profession,study_time)

		#返回
		return current_student



# if __name__ == '__main__':
# 	studentdetail = StudentDetail(3)
# 	studentdetail.mainloop()