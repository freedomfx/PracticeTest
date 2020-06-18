# _*_ coding:UTF-8 _*_

from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *

class BaseDetail(Toplevel):

	def __init__(self):
		super(BaseDetail, self).__init__()
		self.geometry('600x600+700+150')
		self.resizable(0,0)
		self.iconbitmap('../file/weierlite.ico')
		self['bg'] = 'lightgray'

		#准备一个Style
		self.Style01 = Style()
		self.Style01.configure("Title.TLabel",font=('微软雅黑',22,'bold'),foreground='Navy',background='lightblue')
		self.Style01.configure('TPanedwindow',background='SpringGreen')
		self.Style01.configure('Base.TButton',font=('宋体',14,'bold'),foreground='BlueViolet')
		Style_button ='Base.TButton'

		#加载top_banner
		self.login_image = PhotoImage(file="../file/timg.png")
		self.Label_image = Label(self,image=self.login_image)
		self.Label_image.place(x=0,y=0)

		#加载一个标题
		self.Label_title = Label(self,text='学生明细',style='Title.TLabel')
		self.Label_title.place(x=20, y=30)

		#添加一个pane
		self.Pane_detail = Panedwindow(self,width=588,height=420)
		self.Pane_detail.place(x=6,y=110)

		#添加保存按钮
		self.Button_save = Button(self,text='保存',width=8,style=Style_button,command=self.commit)
		self.Button_save.place(x=350,y=555)

		#添加关闭按钮
		self.Button_exit = Button(self,text='关闭',width=8,style=Style_button,command=self.close_gui)
		self.Button_exit.place(x=470,y=555)

	def close_gui(self):
		self.destroy()

	def commit(self):
		pass



if __name__ == '__main__':
	detail = BaseDetail()
	detail.mainloop()
