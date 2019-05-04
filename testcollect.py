
import os
import shutil

dstpath = '/Users/shangzhiqiang/Desktop/test'

def addenroll(enroll, live):
	if os.path.isdir(enroll) and os.path.isdir(live):
		name_left = os.path.join(live, 'image_left_0' + '.txt')
		name_right = os.path.join(live, 'image_right_0' + '.txt')
		if os.path.isfile(name_left) and os.path.isfile(name_right):
			print('success')
			enrollleft = os.path.join(enroll, 'image_left_0' + '.txt')
			enrollright = os.path.join(enroll, 'image_right_0' + '.txt')
			shutil.copyfile(name_left, enrollleft)
			shutil.copyfile(name_right, enrollright)


	pass



def integration(typepath):
	i = 0
	typepath_right = os.path.join(typepath, 'right')
	typepath_left  = os.path.join(typepath, 'left')
	if os.path.isdir(typepath_left) and os.path.isdir(typepath_right):
		nameleftlist = os.listdir(typepath_left)
		for nameleft in nameleftlist:
			if nameleft.endswith('.txt'):
				nameright = nameleft.replace('left', 'right')
				nameleftpath = os.path.join(typepath_left, nameleft)
				namerightpath = os.path.join(typepath_right, nameright)
				if os.path.isfile(nameleftpath) and os.path.isfile(namerightpath):
					new_left_path = os.path.join(typepath, 'image_left_'+str(i) + '.txt')
					new_right_path = os.path.join(typepath, 'image_right_'+str(i) + '.txt')
					shutil.copyfile(nameleftpath, new_left_path)
					shutil.copyfile(namerightpath, new_right_path)

					jpgleft = nameleft.replace('.txt', '.jpg')
					jpgright = jpgleft.replace('left', 'right')
					jpgleftpath = os.path.join(typepath_left, jpgleft)
					jpgrightpath = os.path.join(typepath_right, jpgright)
					if os.path.isfile(jpgleftpath) and os.path.isfile(jpgrightpath):
						new_left_path = os.path.join(typepath, 'image_left_'+str(i)+'.sh')
						new_right_path = os.path.join(typepath, 'image_right_'+str(i)+'.sh')
						shutil.copyfile(jpgleftpath, new_left_path)
						shutil.copyfile(jpgrightpath, new_right_path)
					i += 1
		shutil.rmtree(typepath_left)
		shutil.rmtree(typepath_right)
	pass

def changeDir(pernamepath):
	pernamepath_live = os.path.join(pernamepath, 'live')
	pernamepath_hack = os.path.join(pernamepath, 'hack')
	pernamepath_enroll = os.path.join(pernamepath, 'enroll')
	if 	not os.path.isdir(pernamepath_enroll):	
		os.makedirs(pernamepath_enroll)
	if os.path.isdir(pernamepath_live) and os.path.isdir(pernamepath_hack):
		integration(pernamepath_live)
		integration(pernamepath_hack)
		addenroll(pernamepath_enroll, pernamepath_live)
	pass


def listimage(listdir):
	for name in listdir:
		absname = os.path.join(dstpath, name)
		if os.path.isdir(absname):
			changeDir(absname)
	pass


def listTestDir(path):
	os.chdir(path)
	folder_list = os.listdir(path)
	listimage(folder_list)
	pass

listTestDir(dstpath)
