from BRInfo import BRInfo
from findConstantVars import find_constant_vars
import sys

class BR_Plotter(object):

	def __init__(self, command_line_arguments):
		self.br_object = BRInfo()
		self.window = [20,20,640,640]
		self.figures = []
		self.axes = []
		self.handles = []
		self.legend = []
		self.filename = None
		self.panels = []
		self.buttons = []
		self.switches = []
		self.checkboxes = []

		self.scene = []
		self.dimension = self.br_object.dimension
		self.indices = []
		self.options = {}
		self.is_bounded = []
		self.fv = []
		self.set_default_options()
		if command_line_arguments:
			self.set_options(command_line_arguments)
		self.get_indices()
	def set_default_options(self):
		""" Sets the default options for the BR_Plotter
		Called automatically upon creation of BR_Plotter instance"""

		self.options['use custom projection'] = False
		self.options['markersize'] = 10
		self.options['sample alpha'] = 1
		self.options['face alpha'] = 1
		self.options['edge alpha'] = .4
		self.options['legend font'] = 12
		self.options['label font'] = 16
		self.options['axis font']  = 20
		self.options['line thickness'] = 3
		self.options['autosave'] = True
		self.options['labels'] = True
		self.options['monocolor'] = False
		self.options['render vertices'] = True
		self.options['render curves'] = True
		self.options['render faces'] = True
		self.options['color map'] = "parula"
		self.options['linestyle'] = 'solid'
	
	def set_options(self, command_line_arguments):
		""" changes certain default options based on command line input
		Options:
		 options: 
		'autosave'          - bool [true]
		'vertices', 'vert'  - bool [true]
		'filename', 'file'   - string [BRinfo*.mat]
		'proj'              - handle to function.  no default
		'mono', 'monocolor' - color or RGB triple.  not on by default
		'labels'            - bool [true]
  		'colormap'          - handle to colormap generating function [@jet]
  		'linestyle'         - string, sets all curves to have this style. 
                            no default, curves have style by type.
		'curves', 'curve'   - bool [true]
		'faces'             - bool [true]
		"""
		counter = 0
		num_arguments = len(command_line_arguments)
		if num_arguments == 1:
			### Special exception if only one option (with no argument) entered on command line
			print "Improper command line arguments"
			sys.exit()

		while counter < (num_arguments-1):
			option = command_line_arguments[counter]
			if option == '-autosave':
				counter += 1
				argument = command_line_arguments[counter]
				if argument == 'yes' or argument == 'y' or argument == 'true' or argument == '1':
					# Do autosave
					self.options['autosave'] = True
				elif argument == 'no' or argument == 'n' or argument == 'false' or argument == '0':
					# Don't autosave
					self.options['autosave'] = False
				else:
					print "Improper argument %s for autosave" %argument
					sys.exit()


			elif option == '-curves' or option == '-curve':
				counter += 1
				argument = command_line_arguments[counter]
				if argument == 'yes' or argument == 'y' or argument == 'true' or argument == '1':
					# Do autosave
					self.options['render curves'] = True
				elif argument == 'no' or argument == 'n' or argument == 'false' or argument == 'none' or argument == '0':
					# Don't autosave
					self.options['render curves'] = False
				else:
					print "Improper argument %s for render curves" %argument
					sys.exit()


			elif option == '-proj':
				### Complete this later 
				pass


			elif option == '-mono' or option == '-monocolor':
				""" Need to alter for when user enters RGB triple!!!


				"""

				self.options['monocolor'] = True
				counter += 1
				argument = command_line_arguments[counter]

				if argument == 'r':
					self.options['monocolor option'] = [1, 0, 0]
				elif argument == 'g':
					self.options['monocolor option'] = [0, 1, 0]
				elif argument == 'b':
					self.options['monocolor option'] = [0, 0, 1]
				elif argument == 'm':
					self.options['monocolor option'] = [1, 0, 1]
				elif argument == 'c':
					self.options['monocolor option'] = [0, 1, 1]
				elif argument == 'y':
					self.options['monocolor option'] = [1, 1, 0]
				elif argument == 'k':
					self.options['monocolor option'] = [0, 0, 0]
				else:
					print "input color string must be one of r g b m c y k.  you can also specify a 1x3 RGB color vector"
					sys.exit()


			elif option == '-label' or option == '-labels':
				counter += 1
				argument = command_line_arguments[counter]
				if argument == 'yes' or argument == 'y' or argument =='1' or argument == 'true':
					self.options['labels'] = True
				elif argument == 'no' or argument == 'n' or argument == 'false' or argument == 'none' or argument == '0':
					self.options['labels'] = False
				else:
					print "Improper argument %s for labels" %argument
					sys.exit()

			elif option == '-colormap':
				### Complete this later
				pass


			elif option == '-faces':
				counter += 1
				argument = command_line_arguments[counter]
				if argument == 'y' or argument == 'yes' or argument == 'true' or argument == '1':
					self.options['render faces'] = True
				elif argument == 'n' or argument == 'no' or argument == 'none' or argument == 'false' or argument == '0':
					self.options['render faces'] = False
				else:
					print "Improper argument %s for faces" %argument
					sys.exit()


			elif option == '-vertices' or option == '-vert':
				counter += 1
				argument = command_line_arguments[counter]
				if argument == 'yes' or argument == 'y' or argument == 'true' or argument == '1':
					# Do autosave
					self.options['render vertices'] = True
				elif argument == 'no' or argument == 'n' or argument == 'false' or argument == 'none' or argument == '0':
					# Don't autosave
					self.options['render vertices'] = False
				else:
					print "Improper argument %s for vertices" %argument
					sys.exit()


			elif option == '-linestyle':
				counter += 1
				argument = command_line_arguments[counter]

				if argument == 'solid':
					self.options['linestyle'] = 'solid'
				elif argument == 'dashed':
					self.options['linestyle'] = 'dashed'
				elif argument == 'dotted':
					self.options['linestyle'] = 'dotted'
				elif argument == 'dashdot':
					self.options['linestyle'] = 'dashdot'
				else:
					print "Improper argument %s for linestyle" %argument
					sys.exit()


			elif option == '-filename' or option == '-file':
				counter += 1
				if command_line_arguments[counter][0] == '-':
					print "Error, filename argument must be filename and cannot start with '-'"
					sys.exit()
				else:
					self.filename = command_line_arguments[counter]


			else:
				print "Unexpected option %s" %option
				sys.exit()
			counter += 1


	def get_indices(self):
		"""set up the plotting indices -- which data to plot"""

		if self.br_object.dimension == 1:
			# Curve, not a Surface!!!
			if self.br_object.sampler_data == []:
				number_of_vertices = len(self.br_object.vertices)
				temporary_data = [ [] for i in xrange(number_of_vertices)]
				for ii in xrange(number_of_vertices):
					num_variables = self.br_object.curve.num_variables
					temporary_data[ii] = self.br_object.vertices[ii]['point'][0:num_variables-1]	
			else:
				# sampler_data exists
				counter = 0
				temporary_data = [[] for i in xrange(br_object.curve.num_variables - 1)]
				for ii in xrange(self.br_object.curve.num_edges):
					for jj in xrange(self.br_object.curve.sampler_data.sample_sizes[ii]):
						sample_data = self.br_object.curve.sampler_data.samples[jj]
						temporary_data[counter] = self.br_object.vertices[sample_data + 1]['point']
						counter += 1

		else:
			# Surface, not a Curve!!!
			num_points = min(1000, len(self.br_object.vertices))

			temporary_data = [ [] for i in xrange(num_points)]

			for ii in xrange(num_points):
				num_variables = self.br_object.surface.num_variables
				temporary_data[ii] = self.br_object.vertices[ii]['point'][:num_variables-1]

		indices_of_nonconst_cols = find_constant_vars(temporary_data)
		if len(indices_of_nonconst_cols) >= 4:
			pass # Where get_user_indicies should go
		else:
			if self.dimension == 1:
				self.indices = indices_of_nonconst_cols
			else:
				if len(indices_of_nonconst_cols) == 3:
					self.indices = indices_of_nonconst_cols
				else:
					pass


		

