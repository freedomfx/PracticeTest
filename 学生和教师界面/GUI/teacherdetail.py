# _*_ coding:UTF-8 _*_
"""
实现教师明细的GUI 由BaseDetail派生而来
"""
from basedetail import *
import sys,os
class TeacherDetail(BaseDetail):
	def __init__(self):
		super(TeacherDetail, self).__init__()

		#修改title
		self.Label_title['text'] = '教师明细信息'
		#修改style
		self.Style01.configure('Detail.TLabel',font=('微软雅黑',14,'bold'),foreground='Navy',background='SpringGreen')
		self.Style01.configure('TRadiobutton',font=('微软雅黑',12,'bold'),foreground='navy',background='SpringGreen')
		#添加TeacherDetail内容
		#=======教师编号========
		self.Label_tid = Label(self.Pane_detail,text='教师编号：',style='Detail.TLabel')
		self.Label_tid.place(x=100,y=20)
		self.Entry_tid = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=10)
		self.Entry_tid.place(x=210,y=21)

		#=======姓名========
		self.Label_name = Label(self.Pane_detail,text='姓名：',style='Detail.TLabel')
		self.Label_name.place(x=140,y=65)
		self.Entry_name = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=10)
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
		self.Entry_Birthday = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=10)
		self.Entry_Birthday.place(x=210,y=157)

		#=======手机号码========
		self.Label_mobile = Label(self.Pane_detail,text='手机号码：',style='Detail.TLabel')
		self.Label_mobile.place(x=100,y=200)
		self.Entry_mobile = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_mobile.place(x=210,y=202)

		#=======邮件地址========
		self.Label_email = Label(self.Pane_detail,text='邮件地址：',style='Detail.TLabel')
		self.Label_email.place(x=100,y=245)
		self.Entry_email = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_email.place(x=210,y=247)

		#=======职称=========
		self.Label_title = Label(self.Pane_detail,text='职称：',style='Detail.TLabel')
		self.Label_title.place(x=140,y=290)
		self.Entry_title = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_title.place(x=210,y=292)

		#=======毕业院校=========
		self.Label_college = Label(self.Pane_detail,text='毕业院校：',style='Detail.TLabel')
		self.Label_college.place(x=100,y=335)
		self.Entry_college = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_college.place(x=210,y=337)

		#=======入职时间=========
		self.Label_work_time = Label(self.Pane_detail,text='入职时间：',style='Detail.TLabel')
		self.Label_work_time.place(x=100,y=380)
		self.Entry_work_time = Entry(self.Pane_detail,font=('微软雅黑',12,'bold'),width=16)
		self.Entry_work_time.place(x=210,y=382)

if __name__ == '__main__':
	teacherdetail = TeacherDetail()
	teacherdetail.mainloop()