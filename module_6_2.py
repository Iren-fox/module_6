class Vehicle:
	__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
	def __init__ (self, owner, __model,__color, __engine_power):
		self.owner = owner #владелец транспорта. (владелец может меняться)
		self.__model = __model #модель (марка) транспорта. (мы не можем менять название модели)
		self.__engine_power = __engine_power #мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
		self.__color = __color #название цвета. (мы не можем менять цвет автомобиля своими руками)
	def get_model (self): #возвращает строку: "Модель: <название модели транспорта>"
		print (f'Модель: {self.__model}')
	
	def get_horsepower (self): #возвращает строку: "Мощность двигателя: <мощность>"
		print (f'Мощность двигателя: {self.__engine_power}')
		
	def get_color (self): #возвращает строку: "Цвет: <цвет транспорта>"
		print (f'Цвет: {self.__color}')
		#self.set_color()
		
	def print_info (self): #распечатывает результаты get_model, get_horsepower, get_color; а так же владельца
		self.get_model()
		self.get_horsepower()
		self.get_color()
		print (f'Владелец: {self.owner}')
			
	def set_color (self, new_color):
		if new_color.lower() in (item.lower() for item in self.__COLOR_VARIANTS):
			print (f'Новый цвет: {new_color}')
			self.__color = new_color
		else:
			print (f'Нельзя сменить цвет на {new_color}')
					
				
class Sedan (Vehicle):
	__PASSENGERS_LIMIT = 5 #в седан может поместиться только 5 пассажиров
	
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

print ('Изначальные свойства:')
vehicle1.print_info()
print ()

print ('Меняем свойства:')
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
print ()
print ('Проверяем что поменялось:')
vehicle1.print_info()
	