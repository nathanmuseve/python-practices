def person():
    print("Nathan Museve")
person()  

def person1(names):
    print(f"My name is: {names}")

person1("Ian")

def person2(name, age):
    print(f"I am {name} and i am {age} years old")
person2("Alice", 45)

#*args
def person3(*details):
  name = "joan"
  age = 45
  loaction = "Nairobi"
  data = f"My name is {name} and i am {age} years old and i live in {loaction}"
  print(data)
  return data
person3()
def person4(*data):
  name = "Jennifer"
  age = 25
  year = 2000
  weight = "45kg"
  height = "5feet"
  color = "brown"
  loaction = "Nakuru"
  data = f"My name is {name} and i am {age} years old and i left {loaction} {year} while i was {weight} and {height} in {color} color."
  print(data)
  return data
person4()

#**kwargs 
def person5(**details):
# {  
#  "fname":"kalio",
#   "lname": "Mbithe",
#   "familyname": "kituko",
#   "age":23 
# }
  data = f"My name is {details[0]} {details[2]} {details[1]} and i am {details[4]}."
  print(data)
  return data
person5()
  