import pygame, pickle, os, math

bg = pygame.image.load('BeijingStreetMap.png')
infected = pygame.image.load('redDot.png')
healthy = pygame.image.load('whiteDot.png')

area = 1

def healthCheck(val):
	if val:
		return infected
	else:
		return healthy

for filename in os.listdir(os.getcwd()):
	with open(filename, 'rb') as f:
		data = pickle.load(f)
		data = {i:data[i] for i in sorted(data)}
		uid = [i for i in list(data)]
		infectedBool = [i for i in list(data)[i].values()[0]]
		location = []
		for i in list(data):
			location = location.append(data[i][1:])

		blitList = []
		for i in range(len(list(data)[i])):
			blitList = blitList.append(infected[_], list(data.values())[1:2], area)
		pygame.Surface.blits(blitList)

#bottom right 39.725749, 116.844279
#top left 40.193113, 115.796458
pi = 3.141592
def longlatFind(long1, lat1, long2, lat2):
	r = 6378.137 #earth rad
	dLat = lat2*pi / 180-lat1 * pi /180
	dLong = long2*pi /180 - long1*pi / 180
	a = sin(dLat/2) * sin(dLat/2) + cos(lat1*pi/180) * cos(lat2*pi/180) * sin(dLong/2) * sin(dLong/2)
	c = 2*atan2(sqrt(a), sqrt(1-a))
	d = r * c
	return d*1000 #meters and pain

os.chdir()
