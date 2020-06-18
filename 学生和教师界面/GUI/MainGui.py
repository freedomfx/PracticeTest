# _*_ coding:UTF-8 _*_

from tkinter import *
from tkinter.ttk import *
from fileoperator import *
from tkinter.messagebox import *
from studentdetail import *

class MainGui(Tk):
	def __init__(self):
		super().__init__()
		self.title('学生教师信息管理')
		self.geometry("1400x600+100+100")
		self.resizable(0,0)

		#实例化File类---把学生和教师信息读取到系统
		self.file_info = File()
		self.student_all = self.file_info.list_student_all
		self.teacher_all = self.file_info.list_teacher_all

		self.student_current = []
		self.flag = 0 #通过flag判断什么操作

		#定义一个Style
		self.Style01 = Style()
		self.Style01.configure('TLabel',font =("微软雅黑",14,"bold"),foreground='Navy')

		#学生和教师的标签
		self.Label_student = Label(self,text='学生信息列表：')
		self.Label_student.place(x=40,y=60)

		self.Label_teacher = Label(self,text='教师信息列表：')
		self.Label_teacher.place(x=740,y=60)

		#添加学生表格
		self.student_gui()

		#添加教师表格
		self.teacher_gui()

		#自动加载学生和教师信息到表格
		self.load_student_treeview()
		self.load_teacher_treeview()

		#双击表格某一行触发的事情
		self.Tree_student.bind('<Double-1>',self.view_student)

		#把窗体关闭按钮的行为转化为方法
		self.protocol("WM_DELETE_WINDOWS",self.close_windows)

	def student_gui(self):
		#添加Treeview控件
		self.Tree_student = Treeview(self,columns = ('sno','name','gender','profession','mobile','email'),
									 show = 'headings',height=20)

		#设置每一列的对齐方式
		self.Tree_student.column('sno',width=80,anchor='center')
		self.Tree_student.column('name',width=80,anchor='center')
		self.Tree_student.column('gender',width=60,anchor='center')
		self.Tree_student.column('profession',width=120,anchor='center')
		self.Tree_student.column('mobile',width=150,anchor='center')
		self.Tree_student.column('email',width=150,anchor='center')

		#设置每一列的标题
		self.Tree_student.heading('sno',text='学号')
		self.Tree_student.heading('name',text='姓名')
		self.Tree_student.heading('gender',text='性别')
		self.Tree_student.heading('profession',text='专业')
		self.Tree_student.heading('mobile',text='手机号码')
		self.Tree_student.heading('email',text='邮箱地址')

		#展示表格
		self.Tree_student.place(x=35,y=95)

		#添加按钮
		self.Button_add_student = Button(self,text='添加',width=10,command=self.add_student)
		self.Button_add_student.place(x=400,y=550)

		#修改按钮
		self.Button_update_student = Button(self,text='修改',width=10,command=self.update_student)
		self.Button_update_student.place(x=500,y=550)

		#删除按钮
		self.Button_delete_student = Button(self,text='删除',width=10,command=self.delete_student)
		self.Button_delete_student.place(x=600,y=550)

	def teacher_gui(self):
		self.Tree_teacher = Treeview(self,columns=('tid','name','gender','title','college','mobile'),
									 show = 'headings',height=20)

		#设置每一列的对齐方式
		self.Tree_teacher.column('tid',width=80,anchor='center')
		self.Tree_teacher.column('name',width=80,anchor='center')
		self.Tree_teacher.column('gender',width=60,anchor='center')
		self.Tree_teacher.column('title',width=120,anchor='center')
		self.Tree_teacher.column('college',width=150,anchor='center')
		self.Tree_teacher.column('mobile',width=150,anchor='center')

		#设置每一列的标题
		self.Tree_teacher.heading('tid',text='教师编号')
		self.Tree_teacher.heading('name',text='姓名')
		self.Tree_teacher.heading('gender',text='性别')
		self.Tree_teacher.heading('title',text='职称')
		self.Tree_teacher.heading('college',text='毕业院校')
		self.Tree_teacher.heading('mobile',text='手机号码')

		#展示表格
		self.Tree_teacher.place(x=720,y=95)

		#添加按钮
		self.Button_add_teacher = Button(self,text='添加',width=10)
		self.Button_add_teacher.place(x=1085,y=550)

		#修改按钮
		self.Button_update_teacher = Button(self,text='修改',width=10)
		self.Button_update_teacher.place(x=1185,y=550)

		#删除按钮
		self.Button_delete_teacher = Button(self,text='删除',width=10)
		self.Button_delete_teacher.place(x=1285,y=550)

	def load_student_treeview(self):
		"""

		:return:
		"""
		#1.先把当前TreeView内容清空
		for index in self.Tree_student.get_children():
			self.Tree_student.delete(index)

		#2.加载list中数据
		if len(self.student_all) == 0:
			showinfo('系统消息','没有任何学生信息加载到表格！！！！！！')

		else:
			for index in range(len(self.student_all)):
				self.Tree_student.insert('',index,values=
				(self.student_all[index][0],self.student_all[index][1],self.student_all[index][2],
				 self.student_all[index][6],self.student_all[index][4],self.student_all[index][5],)
										 )

	def load_teacher_treeview(self):
		"""

		:return:
		"""
		#1.先把当前TreeView内容清空
		for index in self.Tree_teacher.get_children():
			self.Tree_teacher.delete(index)

		#2.加载list中数据
		if len(self.teacher_all) == 0:
			showinfo('系统消息','没有任何教师信息加载到表格！！！！！！')

		else:
			for index in range(len(self.teacher_all)):
				self.Tree_teacher.insert('',index,values=
				(self.teacher_all[index][0],self.teacher_all[index][1],self.teacher_all[index][2],
				 self.teacher_all[index][6],self.teacher_all[index][7],self.teacher_all[index][5],)
										 )

	def view_student(self,event):
		'''
		双击某一行加载明细信息
		:return:
		'''
		#获取点击的当前行
		item = self.Tree_student.selection()[0]#获得双击行的
		current_student = self.Tree_student.item(item,'values') #根据ID取出values
		for item in self.student_all:
			if current_student[0] == item[0]:
				self.student_current = item
		#修改flag值
		self.flag = 1


		#以查看的方法加载
		detail = StudentDetail(self.flag,self.student_current,self.student_all)


	def add_student(self):
		"""
		添加学生信息
		:return:
		"""
		#修改flag值
		self.flag=3

		#加载添加的页面
		detail = StudentDetail(self.flag,self.student_all,self.student_current)
		self.wait_window(detail)
		#接收返回的值
		get_return_number = detail.userinfo

		#如果值为1，刷新
		if get_return_number == 1:
			self.load_student_treeview()


	def update_student(self):
		"""
		修改学生信息
		:return:
		"""
		# 获取当前行的信息
		item = self.Tree_student.selection()[0]# 获得双击行的
		current_student = self.Tree_student.item(item, 'values')  # 根据ID取出values
		for item in self.student_all:
			if current_student[0] == item[0]:
				self.student_current = item
		# 修改flag值
		self.flag = 2

		# 加载添加的页面
		detail = StudentDetail(self.flag,self.student_current,self.student_all)
		self.wait_window(detail)
		# 接收返回的值
		get_return_number = detail.userinfo

		# 如果值为1，刷新
		if get_return_number == 1:
			self.load_student_treeview()

	def delete_student(self):
		"""
		删除学生信息
		:return:
		"""
		# 获取当前行的信息
		item = self.Tree_student.selection()[0]  # 获得双击行的
		current_student = self.Tree_student.item(item, 'values')  # 根据ID取出values
		student_object=''
		for item in self.student_all:
			if current_student[0] == item[0]:
				#封装到Student类
				student_object = Student(item[0],item[1],item[2],item[3],
										 item[4],item[5],item[6],item[7],)

		#实例化StudentServices
		current_student_services = StudentServices(self.student_all,student_object)

		#询问是否删除
		choose = askyesno('删除确认','确认要删除学生信息【学号：' + student_object.sno + '  姓名：' + student_object.name
						  + '】信息吗？')

		if choose:
			#执行删除操作
			current_student_services.delete()
			#提醒删除成功
			showinfo('系统消息', '学生信息删除成功!')

			#更新表格
			self.load_student_treeview()
		else:
			return

	def close_windows(self):

		choose = askyesno('关闭前的提醒','关闭窗体前是否要将修改写入到文件？')
		if choose:
			try:
				self.file_info.write_to_file()
				showinfo('系统提示','所有的修改已经写入到文件！')
			except Exception as e:
				showinfo('系统消息',e)
if __name__ == '__main__':
	main = MainGui()
	main.mainloop()
