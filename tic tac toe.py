# import pygame
# import time

# pygame.init()
# game_window=pygame.display.set_mode((400,500))
# pygame.display.set_caption('Game Of Binary Digits')
# exit_game

# import random
# from tkinter import *

# root=Tk()
# root.geometry("700x450")

# l1=Label(root,text='',font=("times",200))

# def roll():
# 	number=['\u2680','\u2861','\u2682','\u2683','\u2684','\u2685']
# 	l1.config(text=f'{random.choice(number)}{random.choice(number)}')
# 	l1.pack()

# b1=Button(root,text='lets roll...', command=roll)
# b1.place(x=330,y=0)
# root.mainloop()

import pygame
from pygame.locals import *
pygame.init()
BD='x'
white=(255,255,255)
a=pygame.display.set_mode((500,650))
pygame.display.set_caption('Tic Tac Toe')
Ab=pygame.image.load(r'D:\MY DOCS\background3.jpg')
Tb=pygame.transform.scale(Ab,(500,650))
l=(57,255,20)
A1=pygame.image.load(r'D:\MY DOCS\one.jpg')
A0=pygame.image.load(r'D:\MY DOCS\zero.jpeg')
T1=pygame.transform.scale(A1,(100,100))
T0=pygame.transform.scale(A0,(100,100))
e=False
g=False
TTT=[[None]*3,[None]*3,[None]*3]
while e==False:
	a.fill(white)
	a.blit(Tb, (0, 0))
	pygame.draw.line(a,l,(500/3,0),(500/3,500),10)
	pygame.draw.line(a,l,((500/3)*2,0),((500/3)*2,500),10)
	pygame.draw.line(a,l,(0,500/3),(500,500/3),10)
	pygame.draw.line(a,l,(0,(500/3)*2),(500,(500/3)*2),10)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			e=True
		elif event.type==pygame.MOUSEBUTTONDOWN:
			x,y=pygame.mouse.get_pos()
			if x<500/3:
				col=1
				
			elif x<(500/3)*2:
				col=2
				
			elif x<500:
				col=3
				
			else:
				col=None

			if y<500/3:
				row=1
				
			elif y<(500/3)*2:
				row=2
				
			elif y<500:
				row=3
				
			else:
				row=None
			print(row,col)

			if (TTT[row-1][col-1]) is None:
				if row==1:
					posx = 30
				if row==2:
					posx = width/3 + 30
				if row==3:
					posx = width/3*2 + 30
				if col==1:
					posy = 30
				if col==2:
					posy = height/3 + 30
				if col==3:
					posy = height/3*2 + 30


				TTT[row-1][col-1]=BD
				if (BD=='x'):
					a.blit(T1,(posy,posx))
					BD='o'	
				else:
					a.blit(T0,(posy,posx))
					BD='x'
				pygame.display.update()
			print(posx,posy)
			print(TTT)
			for i in range(0,3):
				if (TTT[i][0]==TTT[i][1]==TTT[i][2]) and (TTT[i][0] is not None):
					print('winner')
					break
				elif (TTT[0][i]==TTT[1][i]==TTT[2][i]) and (TTT[0][i] is not None):
					print('win')
					break
			if ((TTT[0][0] == TTT[1][1] == TTT[2][2]) and (TTT[0][0] is not None)) or ((TTT[0][2] == TTT[1][1] == TTT[2][0]) and (TTT[0][2] is not None)):
				print('win diag')
				break
			else:
				print('Draw')
				break







pygame.quit()
quit()		

