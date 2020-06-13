# _*_ coding:UTF-8 _*_

from tkinter import *
from tkinter.messagebox import *
import random

class Array:
	# 所有的3*3的图形
	list_all = [
		[[0, 1, 0], [1, 1, 1], [0, 0, 0]],
		[[0, 0, 0], [1, 1, 0], [0, 1, 1]],
		[[0, 0, 0], [0, 1, 1], [1, 1, 0]],
		[[1, 1, 0], [0, 1, 0], [0, 1, 0]],
		[[0, 1, 1], [0, 1, 0], [0, 1, 0]],
	]
	# 所有的颜色
	color_all = ['green', 'yellow', 'red', 'skyblue', 'hotPink']

	def __init__(self):
		# self.list01 = [[1,2,3],[4,5,6],[7,8,9]]
		self.current_block = []
		self.current_color = ''

		#自动获取颜色
		self.get_block()

	def print(self):
		for row in range(len(self.current_block)):
			for col in range(len(self.current_block[row])):
				print(self.current_block[row][col],end='\t')

			#换行
			print()

	def right_rotate(self):
		"""
		对集合进行顺时针旋转
		:return:
		"""
		temp_list = []
		for row in range(len(self.current_block)):
			temp_row = []
			for col in range(len(self.current_block[row])-1,-1,-1):
				temp_row.append(self.current_block[col][row])
			temp_list.append(temp_row)

		self.current_block = temp_list

	def left_rotate(self):
		"""
		对集合进行逆时针旋转
		:return:
		"""
		temp_list = []
		for row in range(len(self.current_block)-1,-1,-1):
			temp_row = []
			for col in range(len(self.current_block[row])):
				temp_row.append(self.current_block[col][row])
			temp_list.append(temp_row)

		self.current_block = temp_list

	def get_block(self):
		max_number = len(Array.list_all)
		get_number = random.randint(0,max_number-1)

		#赋值
		self.current_block = Array.list_all[get_number]
		self.current_color = Array.color_all[get_number]


class Tetris(Array):
	def __init__(self):
		super(Tetris, self).__init__()

		#修改List
		# self.list01 = [[1,1,0],[0,1,1],[0,0,0]]

		#绘制图形
		self.setup_UI()

		#响应键盘的方法
		self.frame.bind('<KeyPress>',self.rotate)

	def setup_UI(self):
		self.frame = Tk()
		self.frame.title('俄罗斯方块')
		self.frame.geometry('400x700+200+100')

		self.cv = Canvas(self.frame,bg='navy',width=300,height=600)
		self.cv.place(x=50,y=30)

		self.show_pic()

	def show_pic(self):
		"""
		在画布中画出相应的图形
		:return:
		"""
		for row in range(len(self.current_block)):
			for col in range(len(self.current_block[row])):
				if self.current_block[row][col] == 1:
					self.cv.create_rectangle(90+30*col,90+30*row,90+30*col+30,90+30*row+30,fill=self.current_color,outline='')

				else:
					self.cv.create_rectangle(90 + 30 * col, 90 + 30 * row, 90 + 30 * col + 30, 90 + 30 * row + 30,
											 fill='navy', outline='')

	def rotate(self,event):
		#使用keycode进行判断按下哪个键
		# if event.keycode == 76:
		# 	showinfo('系统消息','你按了左键')
		#
		# elif event.keycode == 82:
		# 	showinfo('系统消息','你按了右键')
		#keycode 上键 38，下键 40，左键 37，右键 39


		#使用keysym判断哪个键被按下
		if event.keysym in ('L','l'):
			#逆时针旋转
			self.left_rotate()
			self.show_pic()

		elif event.keysym in ('R','r'):
			#顺时针旋转
			self.right_rotate()
			self.show_pic()

		elif event.keycode == 38:
			#向上移动
			for index in range(1,10):
				self.cv.move(index,0,-30)

		elif event.keycode == 40:
			#向下移动
			for index in range(1, 10):
				self.cv.move(index, 0, +30)

		elif event.keycode == 37:
			#向左移动
			for index in range(1, 10):
				self.cv.move(index,-30,0)

		elif event.keycode == 39:
			#向右移动
			for index in range(1, 10):
				self.cv.move(index,+30,0)


	def show(self):
		self.frame.mainloop()


class Canvas_Demo(Tk):
	def __init__(self):
		super().__init__()
		self.title('Canvas绘图')
		self.geometry('800x600+300+100')

		#准备Canvas画板
		cv = Canvas(self,bg='white',width=700,height=500)
		cv.create_line(30,70,80,400,fill='red')
		cv.place(x=50,y=50)


if __name__ == '__main__':
	# window = Tetris()
	# zx = Array()
	# zx.print()
	# print('=====顺时针====')
	# zx.right_rotate()
	# zx.print()
	# print('=====逆时针====')
	# zx.left_rotate()
	# zx.print()

	window = Tetris()
	window.show()