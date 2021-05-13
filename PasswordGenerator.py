from tkinter import *
from tkinter import font as f
from PIL import *
from PIL import ImageTk, Image
from WindowSettings import Window
import random


def main():
	MWn = Window(root)
	app = PasswordGenerator(MWn.win(500, 220, 0, 0))
	root.mainloop()

class PasswordGenerator(Window):
	def __init__(self, master):
		self.master = master
		self.master.title('PASSWORD GENERATOR')

		Font1 = f.Font(family="Garamond", size=20)
		Font2 = f.Font(family="Garamond", size=12, weight=f.BOLD)
		Font3 = f.Font(family="Garamond", size=12)
		Font4 = f.Font(family="Garamond", size=10)

		Color1 = StringVar()
		Color2 = StringVar()
		Color1.set('azure1')
		Color2.set('#A9BC9F')

		def generate():
			self.Text.config(state=NORMAL)
			self.Text.delete(0, END)

			x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
			y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			z = ['°', '!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿', '¡', '|', '+', '}', '{', '*', '[', ']', '_', '-', '.', ',', ':', ';', '^', '~', '<', '>', '¬']
			password = p1 = ""
			l1 = []

			for i in range(3):
				a = b = c = d = ""
				x1 = random.sample(x, k=random.randrange(2, 4))
				y1 = random.sample(y, k=random.randrange(2, 4))
				y2 = random.sample(y, k=random.randrange(2, 4))
				z1 = random.sample(z, k=random.randrange(2, 4))

				for j in x1:
					a += str(j)

				for k in y1:
					b += str(k)

				for l in y2:
					c += str(l.upper())

				for m in z1:
					d += str(m)

				password += (a + b + c + d)			
			
			for letter in password:
				l1.append(letter)

			random.shuffle(l1)

			for letters in l1:
				p1 += letters

			self.Text.insert(INSERT, p1)
			self.master.clipboard_append(self.Text.get())
			self.master.update()
			self.Text.config(state=DISABLED)
			self.Copy.config(state=NORMAL)
			self.Message.destroy()
			self.Image.destroy()

		def copy():
			self.master.clipboard_clear()
			self.master.clipboard_append(self.Text.get())
			self.master.update()
			self.Message = Label(self.MainFrame, bg=Color2.get(), text='Successfully copied to the clipboard', font=Font4, fg='white')
			self.Image = Label(image=self.Img)
			self.Message.place(width=200, height=15, x=150, y=78)
			self.Image.place(width=20, height=20, x=340, y=75)

		def clean():
			self.Text.config(state=NORMAL)
			self.Text.delete(0, END)
			self.Text.config(state=DISABLED)
			self.Copy.config(state=DISABLED)
			self.Message.destroy()
			self.Image.destroy()

		self.MainFrame = Frame(self.master, bg=Color2.get())
		self.MainFrame.pack(fill=BOTH)

		self.Label = Label(self.MainFrame, bg=Color2.get(), text='PASSWORD GENERATOR', font=Font1, fg='#B42929')
		self.Label.pack(pady=(30, 0))

		self.Text = Entry(self.MainFrame, font=Font3, width=40, state=DISABLED)
		self.Text.pack(pady=30) 

		self.Wall = Label(self.MainFrame, bg=Color2.get())
		self.Wall.pack(side=LEFT, padx=(85, 0), pady=(0, 52))

		self.Button = Button(self.MainFrame, bg=Color1.get(), text='GENERATE', font=Font2, command=generate)
		self.Button.place(width=120, height=40, x= 80, y= 150)

		self.Copy = Button(self.MainFrame, bg=Color1.get(), text='COPY', 
			font=Font2, command=copy, state=DISABLED)
		self.Copy.place(width=100, height=40, x= 210, y= 150)

		self.Clean = Button(self.MainFrame, bg=Color1.get(), text='CLEAN', font=Font2, command=clean)
		self.Clean.place(width=100, height=40, x= 320, y= 150)

		self.Message = Label(self.MainFrame, bg=Color2.get(), text='Successfully copied to the clipboard', font=Font4, fg='white')
		self.Img = ImageTk.PhotoImage(Image.open('check.png'))
		self.Image = Label(image=self.Img)
		
if __name__ == '__main__':
	root = Tk()
	main()
