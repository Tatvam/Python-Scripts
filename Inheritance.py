class Parent():
	def __init__(self,last_name,eye_color):
		self.last_name=last_name
		self.eye_color=eye_color

	def show_info(self):
		print("last name "+self.last_name)
		print("eye color "+self.eye_color)


class Child(Parent):
	def __init__(self,last_name,eye_color,number_toys):
		Parent.__init__(self,last_name,eye_color)
		self.number_toys=number_toys


P1=Parent("Dadheech","black")
print(P1.last_name)
P1.show_info()


C1=Child("Dadheech","blue",5)
print(C1.eye_color,C1.number_toys)
C1.show_info()