import ParsingFunctions
import os
class Surface(object):
	def __init__(self):
		self.inputfilename = None
		self.num_variables = 0
		self.dimension
		self.pi = []
		self.num_patches = 0
		self.patch = {}
		self.radius = 0
		self.center_size = 0
		self.center = []
		self.num_faces = 0
		self.num_edges = 0
		self.num_midpoint_slices = 0
		self.num_critical_slices = 0
		self.singular_curve_multiplicities = []
		self.faces = {}    # stores all data from F.faces file
		self.midpoint_curves = []
		self.critical_point_slices = []
		self.critical_curve = []
		self.sphere_curve = []
		self.singular_curves = []
		self.sinfular_names = []
		self.sampler_data = {}   # store all surface_sampler data
		self.input = None

		# automatically parse data files to gather curve data
		self.parse_decomp(self.directory)
		self.parse_surf(self.directory)
		self.gather_faces(self.directory)
		self.gather_curves()
		self.read_input()
	def parse_decomp(self, directory):
		decomposition_data = ParsingFunctions.parse_decomposition(directory)
		self.inputfilename = decomposition_data['input file name']
		self.pi = decomposition_data['Pi info'] 
		self.patch = decomposition_data['Patch_Vectors']
		self.radius = decomposition_data["radius"]
		self.center = decomposition_data["center"]
	def parse_surf(self, directory):
		surf_data = ParsingFunctions.parse_Surf(directory)
		self.num_faces = surf_data[0]
		self.num_edges = surf_data[1]
		self.num_midpoint_slices = surf_data[2]
		self.num_critical_point_slices = surf_data[3]
		self.singular_curve_multiplicites = surf_data[4]

	def gather_faces(self, directory):
		self.faces = ParsingFunctions.parse_Faces(directory)
	def gather_curves():
		pass
	def read_input(self, directory):
		filename = directory + '/' + self.inputfilename
		if not os.path.isfile(filename):
			print "Could not find input file in current directory: %s" %(directory)
		else:
			with open(filename, 'r') as f:
				self.input = f.readline()









class Curve(Surface):
	def __init__(self, directory):
		self.num_edges = 0
		self.edges = []
		self.directory = directory
		self.input = None
		self.inputfilename = None
		self.num_variables = 0
		self.dimension = 0
		self.pi = []
		self.num_patches = []
		self.patch  = {}
		self.radius
		self.center_size = 0
		self.center = []
		self.sampler_data = {}

		# automatically parse data files to gather curve data
		self.parse_decomp(self.directory)
		self.parse_edge(self.directory)
		self.parse_curve_sampler(self.directory)
		self.read_input(seld.directory)

	
	def parse_edge(self, directory):
		edge_data = ParsingFunctions.parse_Edge(directory)
		self.num_edges = edge_data['number of edges']
		self.edges = edge_data['edges']

	def parse_curve_sampler(self.directory):
		pass
	







