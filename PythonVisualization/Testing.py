from BRInfo import BRInfo
from ParsingFunctions import parse_directory_name, parse_decomposition, parse_Edges


BRobject = BRInfo()

first_midpoint_slice = BRobject.surface.midpoint_slices[0]

print first_midpoint_slice.inputfilename
print '\n\n\n'
print first_midpoint_slice.num_variables 
print '\n\n\n'

print first_midpoint_slice.dimension 
print '\n\n\n'

print first_midpoint_slice.pi 
print '\n\n\n'

print first_midpoint_slice.num_patches 
print '\n\n\n'

print first_midpoint_slice.patch 
print '\n\n\n'

print first_midpoint_slice.radius 
print '\n\n\n'

print first_midpoint_slice.center 
print '\n\n\n'

print first_midpoint_slice.num_edges 
print '\n\n\n'

print first_midpoint_slice.edges 
print '\n\n\n'




