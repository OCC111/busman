class Car():
	def __init__(self,color):
		self.color = color

	def run(self):
		print("------run------")

class BenChi(Car):
	def __init__(self,color):
		self.color = color
		super().__init__(self,color)
	def run(self):
		print("---benchi---run")

class Factory():
	def create(self):
		pass

class CarFactory(Factory):
	def create(self,typeName):
		if typeName == "白色"：
			benchi = BenChi().create()
		



