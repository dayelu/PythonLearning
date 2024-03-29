import pygame

class Ship(object):
	"""初始化飞船并设置其初始位置"""
	def __init__(self, screen):
		self.screen = screen

		#加载飞船图像并获取其外界矩形
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘飞船放在并木底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitime(self):
		"""在指定位置绘制飞船"""
		self.screen.blit(self.image,self.rect)

