
import sys
def distinct(file):
	"""del the same"""
	try:
		with open(file,"rU") as f_obj:
			
			lines = f_obj.readlines()

		return set(lines)

	except Exception as e:
		print(e)



def write_into_file(file,array):
	try:


		with open(file,"w") as f_obj:
			
			for url in array:

				f_obj.write(url)

		return "complete!"
	except Exception as e:
		print(e)



file = "video_urls.txt"

array = distinct(file)

file = "video_urls_unique.txt"
file = "video_urls_unique_error.txt"

print(write_into_file(file,array))