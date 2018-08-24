import time

class Hotel():
	def __init__(self,name):
		self.name = name
		self.list = []
		self.money = 0

	def inhome(self,person):
		person.time = int(time.time())
		person.islive = True
		self.list.append(person)
	def outhome(self,name):
		for person in self.list:
			if person.name == name:
				person.islive = False
				endtime = int(time.time())
				diff_money = (endtime - person.time)*10
				print("花了%0.2f"%diff_money)
				self.money += diff_money
				break
	def tongji(self):
		count = 0
		for person in self.list:
			if not person.islive:
				count+=1
		print("今天入住%d人,离店%d,收入:%d"%(len(self.list),count,self.money))	

class Person():
	def __init__(self,name):
		self.name = name
	def setcard(self,card):
		self.card = card


qt = Hotel("7天酒店")

while True:
	user = int(input("请输入程序序号\n1.入住\n2.离店\n3.统计\n4.退出\n-------------------\n输入:"))
	if user == 1:
		name = input("请输入入住的姓名:")
		card = int(input("请输入身份证号:"))
		lz = Person(name)
		lz.setcard(card)
		qt.inhome(lz)
	elif user == 2:
		name = input("输入姓名")
		qt.outhome(name)
	elif user == 3:
		pass
	elif user == 4:
		print("退出中...")
		time.sleep(2)
		break
print(qt)
