import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):		#继承TestCase类
	"""测试name_function.py"""
	def test_first_last_name(self):		#测试方法名必须以 test_ 开发，这样运行unittest.main()方法时才会自动运行
		"""能够正确地处理像Janis Joplin这样的姓名吗？"""
		formatted_name = get_formatted_name("janis","joplin")
		self.assertEqual(formatted_name,"Janis Joplin")

unittest.main()
