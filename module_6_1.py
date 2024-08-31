class Animal:
	alive = True
	fed = False
	def __init__(self, name):
		self.name = name	
	def eat (self, food): 
		self.food = food
		if isinstance (food, Fruit):
			print (f'{self.name} съел {food.name}')
			self.fed = True
		else:
			print (f'{self.name} не стал есть {food.name}')
			self.alive = False
				
class Mammal (Animal):
	alive = True
	fed = False
	def __init__ (self, name):
		super().__init__ (name)
	def eat (self, food):
		super().eat (food)
	
class Predator (Animal):
	def __init__ (self, name):
		super().__init__ (name)
	def eat (self, food):
		super().eat (food)
				
class Plant:
	edible = False
	def __init__(self, name):
		self.name = name
		
class Flower (Plant):
	def __init__ (self, name):
		super().__init__ (name)
	
class Fruit (Plant):
	edible = True
	def __init__ (self, name):
		super().__init__ (name)
	
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(f'Животное первое: {a1.name}')
print(f'Растение первое: {p1.name}')
print(f'{a1.name} живой: {a1.alive}')
print(f'{a1.name} сытый: {a1.fed}')
a1.eat(p1)
print(f'{a1.name} живой: {a1.alive}')
print ()
print(f'Животное второе: {a2.name}')
print(f'Растение второе: {p2.name}')
print(f'{a2.name} живой: {a2.alive}')
print(f'{a2.name} сытый: {a2.fed}')
a2.eat(p2)
print(f'{a2.name} сытый: {a2.fed}')

print ()
a3 = Predator ('Лев')
p3 = Fruit ('Ананас')
print(f'Животное третье: {a3.name}')
print(f'Растение третье: {p3.name}')
print(f'{a3.name} живой: {a3.alive}')
print(f'{a3.name} сытый: {a3.fed}')
a3.eat(p3)
print(f'{a3.name} живой: {a3.alive}')
print(f'{a3.name} сытый: {a3.fed}')

print ()
a4 = Mammal ('Панда')
p4 = Flower ('Ромашка')
print(f'Животное четвертое: {a4.name}')
print(f'Растение четвертое: {p4.name}')
print(f'{a4.name} живой: {a4.alive}')
print(f'{a4.name} сытый: {a4.fed}')
a4.eat(p4)
print(f'{a4.name} живой: {a4.alive}')
print(f'{a4.name} сытый: {a4.fed}')