from controller import *
import controller as ctlr

import time
import random
import json

from main import *
import main as mn

from tkinter import * 
import tkinter as tk 

from tkinter.messagebox import *
import tkinter.messagebox as mb

from tkinter.ttk import * 
import tkinter.ttk as ttk

from PIL import ImageTk, Image 

class View(tk.Frame):
	def __init__(self,parent,*args):
		super().__init__()

		def _clear_another_win():
			for i in parent.winfo_children():
					parent.destroy()
					parent.quit()
					if hasattr(parent,"win"):
						parent.win.destroy()
						parent.win.quit()
					else:
						print("no")

		def _back_to_main_menu():
			self.win.destroy()
			app = mn.App(parent)
			app.mainloop()
			


		def _onecard():
			_clear_another_win()
			self.win = tk.Tk()
			
			def shuffle():
				counter = 0
				for i in self.win.winfo_children():
					counter += 1
					if counter > 3:
						i.destroy()
				card_creator()
			self.bgcolor = "#404040"
			self.win.geometry("1200x600+100+50")
			self.win.configure(bg=self.bgcolor)
			self.win.title("One Card Check")
			self.win.attributes("-fullscreen",-1)
			self.back = tk.Button(self.win,text="<< Back to Main Menu",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"),command=_back_to_main_menu)
			self.back.grid(row=0,column=0,pady=10,padx=30)
			
			button = tk.Button(self.win,text="Shuffle cards",fg="cyan",bg="#404040",command=shuffle)
			button.grid(row=3,column=0,pady=0,padx=30,sticky="nesw")
			
			title = tk.Label(self.win,text="One Card Check",bg=self.bgcolor,fg="cyan")
			title.grid(row=3,column=1,pady=10,padx=10)

			"""self.tarot_back_img = ImageTk.PhotoImage(Image.open('tarot_back.jpg'))
			self.tarot_back = Label(self.win,i=self.tarot_back_img,border="5")
			self.tarot_back.grid(row=4,column=0,rowspan=4,pady=10,padx=30)"""

			#button = tk.Button(self.win,text="Click to choose card",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"))
			#button.grid(row=5,column=0,pady=10,padx=30)
			
			self.img = (Image.open("tarot_back.jpg"))
			self.resize_img = self.img.resize((100,200),Image.ANTIALIAS)
			self.new_img = ImageTk.PhotoImage(self.resize_img)
			
			self.canvasDict = {}
			self.canvasDict2 = {}
			self.canvasDict3 = {}
			
			def card_delay():
				for i in range(7):
					self.canvasDict["canvas{}".format(i)].grid(row=4,column=1+i,padx=10,pady=3)	
			def card_delay2():
				for i in range(8):
					self.canvasDict2["canvas{}".format(i)].grid(row=5,column=1+i,padx=10,pady=3)
			def card_delay3():
				for i in range(7):
					self.canvasDict3["canvas{}".format(i)].grid(row=6,column=1+i,padx=10,pady=3)


			self.choosecard_list = ["Fool","empress","hermit","chariot","temperance"]




			def chooseCard(event):
				for i in range(7):
					self.canvasDict["canvas{}".format(i)].destroy()
					self.canvasDict3["canvas{}".format(i)].destroy()
					self.canvasDict2["canvas{}".format(i)].destroy()
					self.canvasDict2["canvas{}".format(i+1)].destroy()
				x = random.randrange(0,5) #0 include but 5 not include
				self.imagecard = (Image.open("Tarot/{}.jpg".format(self.choosecard_list[0])))
				self.imagecard_resize = self.imagecard.resize((150,280),Image.ANTIALIAS)
				self.imagecard_new = ImageTk.PhotoImage(self.imagecard_resize)
				self.choosecard_name = self.choosecard_list[0]
				self.data = json.load(open("Onecard/{}.json".format(self.choosecard_list[0])))
				self.textdata = self.data[0]
				namelb = tk.Label(self.win,text="The card name is the '{}'.".format(self.choosecard_name)+self.textdata["onecard"],fg="lightblue",bg="#404040",font=('Terminal',12,'bold'))
				namelb.grid(row=4,rowspan=4,column=1,padx=30,pady=30,sticky="nesw")

				
				#print(self.textdata["onecard"])

				self.canvasCard = Canvas(self.win,width=150,height=280)
				self.canvasCard.create_image(0,0,anchor=NW,image=self.imagecard_new)
				self.canvasCard.grid(row=4,rowspan=4,pady=30,padx=30)
				
				
		
			def card_creator():
				#self.canvas.grid(row=4,column=2+self.i,padx=10,pady=3)
				for i in range(7):
					self.canvasDict["canvas{}".format(i)] = Canvas(self.win,width=100,height=200)
					self.canvasDict["canvas{}".format(i)].create_image(0,0,anchor=NW,image=self.new_img) 
					self.canvasDict["canvas{}".format(i)].bind("<Button-1>",chooseCard)
					self.win.after(1000,card_delay)		
				for i in range(8):
					self.canvasDict2["canvas{}".format(i)] = Canvas(self.win,width=100,height=200)
					self.canvasDict2["canvas{}".format(i)].create_image(0,0,anchor=NW,image=self.new_img)
					self.canvasDict2["canvas{}".format(i)].bind("<Button-1>",chooseCard) 
					self.win.after(2000,card_delay2)		
				for i in range(7):
					self.canvasDict3["canvas{}".format(i)] = Canvas(self.win,width=100,height=200)
					self.canvasDict3["canvas{}".format(i)].create_image(0,0,anchor=NW,image=self.new_img)
					self.canvasDict3["canvas{}".format(i)].bind("<Button-1>",chooseCard) 
					self.win.after(3000,card_delay3)
			
			
			card_creator()

			


			

			


			

			self.win.mainloop()


		def _character():
			_clear_another_win()
			self.win = tk.Tk()
			self.bgcolor = "#404040"
			self.win.geometry("1200x600+100+50")
			self.win.configure(bg=self.bgcolor)
			self.win.title("character")
			self.win.attributes("-fullscreen",-1)
			self.back = tk.Button(self.win,text="Back to Main Menu",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"),command=_back_to_main_menu)
			self.back.grid(row=0,column=0,pady=10,padx=30)

			button = tk.Label(self.win,text="Character",bg=self.bgcolor,fg="cyan")
			button.grid(row=3,column=0,pady=10,padx=30)


			self.win.mainloop()

		def _past():
			_clear_another_win()
			self.win = tk.Tk()
			self.bgcolor = "#404040"
			self.win.geometry("1200x600+100+50")
			self.win.configure(bg=self.bgcolor)
			self.win.title("Past")
			self.win.attributes("-fullscreen",-1)
			self.back = tk.Button(self.win,text="Back to Main Menu",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"),command=_back_to_main_menu)
			self.back.grid(row=0,column=0,pady=10,padx=30)

			button = tk.Label(self.win,text="Past",bg=self.bgcolor,fg="cyan")
			button.grid(row=3,column=0,pady=10,padx=30)


			self.win.mainloop()

		def _love():
			_clear_another_win()
			self.win = tk.Tk()
			self.bgcolor = "#404040"
			self.win.geometry("1200x600+100+50")
			self.win.configure(bg=self.bgcolor)
			self.win.title("Love")
			self.win.attributes("-fullscreen",-1)
			self.back = tk.Button(self.win,text="Back to Main Menu",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"),command=_back_to_main_menu)
			self.back.grid(row=0,column=0,pady=10,padx=30)

			button = tk.Label(self.win,text="Love",bg=self.bgcolor,fg="cyan")
			button.grid(row=3,column=0,pady=10,padx=30)


			self.win.mainloop()

		def _education():
			_clear_another_win()
			self.win = tk.Tk()
			self.bgcolor = "#404040"
			self.win.geometry("1200x600+100+50")
			self.win.configure(bg=self.bgcolor)
			self.win.title("Education")
			self.win.attributes("-fullscreen",-1)
			self.back = tk.Button(self.win,text="Back to Main Menu",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"),command=_back_to_main_menu)
			self.back.grid(row=0,column=0,pady=10,padx=30)

			button = tk.Label(self.win,text="Education",bg=self.bgcolor,fg="cyan")
			button.grid(row=3,column=0,pady=10,padx=30)


			self.win.mainloop()

		def _carrer():
			_clear_another_win()
			self.win = tk.Tk()
			self.bgcolor = "#404040"
			self.win.geometry("1200x600+100+50")
			self.win.configure(bg=self.bgcolor)
			self.win.title("Carrer")
			self.win.attributes("-fullscreen",-1)
			self.back = tk.Button(self.win,text="Back to Main Menu",bg=self.bgcolor,fg="cyan",font=("Terminal",12,"bold"),command=_back_to_main_menu)
			self.back.grid(row=0,column=0,pady=10,padx=30)

			button = tk.Label(self.win,text="Carrer",bg=self.bgcolor,fg="cyan")
			button.grid(row=3,column=0,pady=10,padx=30)


			self.win.mainloop()


		def _exit():
			if ctlr.Controller._exit():
				for i in parent.winfo_children():
					parent.destroy()
					parent.quit()
					if hasattr(parent,"win"):
						parent.win.destroy()
						parent.win.quit()
				else:
					print("no")

		def _menu():
			self.bgimg = ImageTk.PhotoImage(Image.open('tarot.jpg'))
			self.hdlb = tk.Label(self,text="Tarot Fourtue Teller",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'))
			self.bgimglb = Label(self,i=self.bgimg,border="5")

			self.hdlb.grid(row=0,column=0,pady=10,padx=30)
			self.bgimglb.grid(row=1,column=0,rowspan=20,pady=10,padx=0)

			#button group
			
			self.onecard = tk.Button(self,text="One Card Check",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_onecard)
			self.onecard.grid(row=1,column=1,pady=10,padx=10,sticky="nesw")

			self.character = tk.Button(self,text="Thin har ba lo lu sar lal?",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_character)
			self.character.grid(row=2,column=1,pady=10,padx=10,sticky="nesw")


			self.past = tk.Button(self,text="Thin Bal theik ka lar tha lal?",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_past)
			self.past.grid(row=3,column=1,pady=10,padx=10,sticky="nesw")
			

			self.love = tk.Button(self,text="Think a chick yay ?",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_love)
			self.love.grid(row=4,column=1,pady=10,padx=10,sticky="nesw")

			
			self.education = tk.Button(self,text="Think pyinyar yay?",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_education)
			self.education.grid(row=5,column=1,pady=10,padx=10,sticky="nesw")

			self.carrer = tk.Button(self,text="Think a lot a kai ?",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_carrer)
			self.carrer.grid(row=6,column=1,pady=10,padx=10,sticky="nesw")

			
			self.exit = tk.Button(self,text="Exit",bg=parent.bgcolor,fg="cyan",font=('Terminal',12,'bold'),command=_exit)
			self.exit.grid(row=7,column=1,pady=10,padx=10,sticky="nesw")


			self.fgcolor = "cyan"
			self.configure(bg=parent.bgcolor)

		_menu()
		
		
		

if __name__ == "__main__":
	view = View()
	view.mainloop()

