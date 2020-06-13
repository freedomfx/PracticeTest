# _*_ coding:UTF-8 _*_

from tkinter import *
from tkinter.ttk import *

class MainGui(Tk):
	def __init__(self):
		super().__init__()
		self.title('学生教师信息管理')
		self.geometry("1400x600+100+100")
		self.resizable(0,0)

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
		self.Button_add_student = Button(self,text='添加',width=10)
		self.Button_add_student.place(x=400,y=550)

		#修改按钮
		self.Button_update_student = Button(self,text='修改',width=10)
		self.Button_update_student.place(x=500,y=550)

		#删除按钮
		self.Button_delete_student = Button(self,text='删除',width=10)
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


if __name__ == '__main__':
	main = MainGui()
	main.mainloop()
