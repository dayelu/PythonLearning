import os

#经测九百张图重命名完成耗时0.7s

for current_folder,sub_folders,filenames in os.walk(".\\imgs\\"):

	for filename in filenames:

		file_name = current_folder[7:]+"_"+filename[3:]
		old_name = os.path.join(current_folder,filename)
		new_name = os.path.join(current_folder,file_name)
		
		os.rename(old_name,new_name)

print("重命名完成")