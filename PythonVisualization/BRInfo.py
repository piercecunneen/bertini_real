import os
import ParsingFunctions
from Dehomonogize import dehomonogize
from Surface import Surface, Curve
class BRInfo(object):
    def __init__(self):
        self.filenames = []
        self.num_vertices = 0
        self.vertices = []
        self.directory_info = ParsingFunctions.parse_directory_name()
        self.find_directory(self.directory_info[0])
        self.dimension = int(self.directory_info[2])
        
        # gather vertices
        self.gather_vertices()
        if self.dimension == 1:
            # polynomial is a curve
            self.gather_curve(self.directory)
        elif self.dimension == 2:
            # polynomial is a surface
            self.gather_surface(self.directory)

        print "Done gathering decomposition"
    def find_directory(self,directory_path):
        directories = directory_path.split('/')
        if len(directories) > 1:
            self.directory = directories[-1]
        else:
            self.directory = directory_path
    def gather_vertices(self):
        vertex_file_name = "V.vertex"
        if os.path.isfile("%s/V_samp.vertex" %self.directory):
            vertex_file_name = "V_samp.vertex"
            
        # open vertex file and read data from file in read mode
        with open("%s/%s" %(self.directory, vertex_file_name), 'r') as f:
            # read first line and get number of vertices, number of projections, 
            # number of natural vars,and number of file names
            line = f.readline().split(' ')
            self.num_vertices = int(line[0])
            num_projections = int(line[1])
            num_natural_vars = int(line[2])
            num_filenames = int(line[3].replace('\n', '')) 
            
            # Skips data not used
            for i in xrange(0, (num_projections * num_natural_vars)):
                skip_this_line = f.readline()
                while skip_this_line == '\n':
                        skip_this_line = f.readline()
            skip_line = f.readline()
            if line == '\n':
                skip_line = f.readline()
            
            
            # Gets file names and stores them in self.filenames
            for ii in xrange(num_filenames):
                skip_line = f.readline()
                self.filenames.append(f.readline().replace('\n', ''))
           
            self.vertices = [ {} for i in range(self.num_vertices)]
            
            for ii in xrange(self.num_vertices):
                line = f.readline()
                
                while line == '\n':
                    line = f.readline()
                number_of_variables = int(line)
                self.vertices[ii]['point'] = []
                temporary_point = []
                for jj in xrange(number_of_variables):
                    complex_num = f.readline().split(' ')
                    real_part = float(complex_num[0])
                    imaginary_part = float(complex_num[1])
                    
                    temporary_point.append(complex(real_part, imaginary_part))
                
                x = dehomonogize(temporary_point[0:num_natural_vars])
                self.vertices[ii]['point'] = x
                line = f.readline()
                
                while line == '\n':
                    line = f.readline().replace('\n', '')
                    
                    
                num_projection_values = int(line)
                self.vertices[ii]['projection_value'] = []
                for ll in xrange(num_projection_values):
                    complex_num = f.readline().split(' ')
                    real_part = float(complex_num[0])
                    imaginary_part = float(complex_num[1])
                    self.vertices[ii]['projection_value'].append(complex(real_part, imaginary_part))
               
                line = f.readline().replace('\n', '')
               
                while line == '\n':
                    line = f.readline()
                
                self.vertices[ii]['input_filename_index'] = float(line.replace('\n', ''))
                line = f.readline()
                
                while line == '\n':
                    line = f.readline()
                
                self.vertices[ii]['type'] = float(line.replace('\n',''))
        return 


    def gather_surface(self, directory):
        # creates new surface
        self.surface = Surface(directory)

        
    def gather_curve(self, directory):
        self.curve =  Curve(directory)     






