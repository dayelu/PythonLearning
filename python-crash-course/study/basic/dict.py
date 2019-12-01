dict_a = {'name' : 'liu','age' : 22,'sex' : 'male'}
print(dict_a)
print('==========================================')
print(dict_a['name'])
print('================add a key-value=======================')
dict_a['weight'] = 100
print(dict_a)
print(dict_a['weight'])
print('================add empty key-value=======================')
dict_b = {}
dict_b = {'job' : 'ant coder','salary' : '1K'}
print(dict_b)
print('before modified is:' + dict_b['job'])

dict_b['job'] ='banzhuan'
print('after is:' + dict_b['job'])

del dict_b['salary']    #删除一个键值对

print(dict_b)
#print(dict_b['salary'])            打印不存在的键值对会报错

print('================class key-value=======================')


favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print(favorite_languages);

print('==============字典遍历===================')

print(" int the 'favorite_languages.items()','items()' function return :" )
print(favorite_languages.items())

print('=====================按顺序遍历结果===================')

for key, value in sorted(favorite_languages.items()):
    print('\n' + key + ' : ' + value)

print('====================遍历键======================')
fl_key = favorite_languages.keys()
print(fl_key)
for key in favorite_languages.keys():
    if key == 'jen':
        print(key.title())
    else:
        print(key)
print('====================完全一样的效果======================')
for key in favorite_languages:
    if key == 'jen':
        print(key.title())
    else:
        print(key)

print('====================遍历值======================')
for value in sorted(favorite_languages.values()):
    print(value)

    
print('====================set集合======================')
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print('====================字典列表======================')

aliens = []     # 创建一个用于存储外星人的空列表

# 创建30个绿色的外星人
for alien_number in range (0,30):
    
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}

    aliens.append(new_alien)

for alien in aliens[0:3]:
    
    if alien['color'] == 'green':
        
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
    
print("...")

#print()方法似乎只能打印字符串类型的变量
print("Total number of aliens: " + str(len(aliens)))
    

