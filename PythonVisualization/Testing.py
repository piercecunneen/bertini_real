from BRInfo import BRInfo
from ParsingFunctions import parse_directory_name, parse_decomposition, parse_Edges


X = BRInfo()
directory = parse_directory_name('Dir_Name')
X.find_directory(directory[0])
X.gather_vertices()
X.dimension = directory[2]
d = X.gather_surface(X.directory)
for i in d:
	print i
