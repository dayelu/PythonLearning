import os
from PIL import Image   #Pillow库的模块名是PIL，与python的Python Image Library向后兼容所以不是from Pillow ....

class ImgOperate():
	"""图像处理的几个例子"""
	def __init__(self):
	# def __init__(self, catIm):

		self.catIm = Image.open("zophie.png")	#生成图片对象
		
	def save_as(self):
		"""图片另存为其他格式"""
		try:
			catIm = self.catIm
			print(catIm.size)
			width,height = catIm.size
			print("图片宽为："+str(width)+"，高为："+str(height))
			print("图片格式为："+catIm.format)
			print("图片格式描述："+catIm.format_description)
			catIm.save("zophie.jpg")
			print(os.listdir("./"))
		except Exception as e:
			print(e)

	def paint(self,size,file_name,color=0,color_model="RGBA"):
		"""简单地绘图"""
		try:

			im = Image.new(color_model,size,color)
			im.save(file_name)

		except Exception as e:
			print(e)


	def copy_paste(self):
		"""图片的剪切与复制粘贴"""
		try:
			catIm = self.catIm
			cropedIm = catIm.crop((335,345,565,560))
			cropedIm.save("cropped.png")

			catCopyIm = catIm.copy()

			faceIm = catIm.crop((335,345,565,560))

			print(faceIm.size)

			catCopyIm.paste(faceIm,(0,0))
			catCopyIm.paste(faceIm,(400,500))

			catCopyIm.save("pasted.png")
			print("复制完成")
		except Exception as e:
			print(e)

	def paste_fill(self):
		try:
			catIm = self.catIm
			faceIm = catIm.crop((335,345,565,560))
			catImWidth,catImHeight = catIm.size
			faceImWidth,faceImHeight = faceIm.size

			catCopyTwo = catIm.copy()

			for left in range(0,catImWidth,faceImWidth):
				for top in range(0,catImHeight,faceImHeight):
					print(left,top)
					catCopyTwo.paste(faceIm,(left,top))
			catCopyTwo.save("tiled.png")
			print("copy完成")
		
		except Exception as e:
			print(e)


obj = ImgOperate()


size1 = (100,200)
file_name1 = "purpleImage.png"
color1 = "purple"

size2 = (20,20)
file_name2 = "transparentImage.png"

obj.save_as()

obj.paint(size2,file_name2)
obj.copy_paste()
obj.paste_fill()
