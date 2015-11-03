
def parse_directory_name(directory_name):
    """ Parses file that contains the directory name, the MPtype, and the dimension
     Returns a list [directory, MPtype, dimension]
     """
    with open(directory_name, 'r') as f:
        directory = f.readline().replace('\n', '')
        MPtype = f.readline().replace('\n', '')
        dimension = f.readline().replace('\n', '')
    return [directory, MPtype, dimension]


