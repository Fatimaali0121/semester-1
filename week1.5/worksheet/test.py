from rect import Rectangle

R = Rectangle(5,5)
print(R.area())
print(R.perimeter())
print(R.is_square())
print(R.width)
print(R.height)



from datetime import date
from person import Person

person1 = Person("Alan John Smith", date(2006, 11, 6))

print("Name:", person1.name)
print("Birth:", person1.birth)
print("Initials:", person1.initials())
print("Is birthday:", person1.is_birthday())