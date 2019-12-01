cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

name = 'liu'

print("==============================I\'m  cutline ===========================")

if name != 'wang':
    print('is not me')
    
print("==============================or ===========================")

age_0 = 22
age_1 = 18

if age_0 >= 21 or age_1 >= 21 :
    print('yes,i do');
age_0 = 18

if age_0 >= 21 or age_1 >= 21:
    print('yes,i do')

print("==============================and===========================")


age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print('yes,i do')
age_1 = 22

if age_0 >= 21 and age_1 >= 21:
    print('yes,i do')


print("==============================in && not in===========================")
    
firstname = 'wang'
list = ['zhao','qian','sun','li','zhou']

if firstname in list:
    print(firstname + ' is in the top 5')
if firstname not in list:
    print(firstname + ' is not in the top 5')


print("==============================if-else && if-elif-else-===========================")


hundredNames = ['zhao','qian','sun','li','zhou','wu']
fifth = hundredNames[4]
if fifth == 'zhou':
    print("fifth name is 'zhou'")
elif fifth == 'wu':
    print("fifth name is 'wu'")
elif fifth == 'li':
    print("fifth name is 'li'")
else:
    print("I don't know")
    
print("==============================condition test===========================")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("==============================list condition test===========================")

list_e = []
if list_e:
    print("I\'m not empty")
else:
    print("I\'m empty truly")



