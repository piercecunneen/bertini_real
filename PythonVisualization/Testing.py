from BRInfo import BRInfo
from ParsingFunctions import parse_directory_name


X = BRInfo()
directory = parse_directory_name('Dir_Name')
X.find_directory(directory[0])
print X.gather_vertices()
for i in X.vertices:
    print i
    print ' '
    print ' '