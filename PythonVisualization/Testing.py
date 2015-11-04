from BRInfo import BRInfo
from ParsingFunctions import parse_directory_name, parse_decomposition


X = BRInfo()
directory = parse_directory_name('Dir_Name')
X.find_directory(directory[0])
X.gather_vertices()
X.dimension = directory[2]



for i in X.gather_surface():
	print i['midpoint'], i['middle slice index'], i['top'], i['bottom'], i['system top'], i['system bottom'], i['num left'], i['left'], i['num right'], i['right']
	print ' '
	print ' ' 

