def build_profile(first, last, **user_info):		#把前两个参数之外的所有参数放在一个字典里
	"""创建一个字典， 其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile


user_profile = build_profile('albert', 'einstein',
			location='princeton',
			field='physics')

print(user_profile)
