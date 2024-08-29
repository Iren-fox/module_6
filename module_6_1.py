class Animal:
	alive = True #живой
	fed = False #сытый
	def eat (self, food): #food - принимает объекты классов растений
		self.food = food
		if isinstance (food, Fruit):
			print (f'{self.name} съел {food.name}')
		else:
			print (f'{self.name} не стал есть {food.name}')
			alive = False
			
class Mammal (Animal):
	def __init__(self, name):
		self.name = name
		super().eat()
		
class Predator (Animal):
	def __init__(self, name):
		self.name = name
		#self.eat (food)
		
class Plant:
	edible = False
	#name - название растения
	
class Flower (Plant):
	def __init__(self, name):
		self.name = name
	
class Fruit (Plant):
	edible = True
	def __init__(self, name):
		self.name = name
	
plant1 = Fruit ('Груша')
animal1 = Mammal ('Жираф')
animal1.eat (plant1)
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
