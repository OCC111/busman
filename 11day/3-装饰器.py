def w1(fun):
	def inner():
		print("验证登录")
		fun()
	return inner


@w1
def pay():
	print("支付中，，，")

pay()
