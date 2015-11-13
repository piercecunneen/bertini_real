from BR_Plotter import BR_Plotter
import sys
from findConstantVars import find_constant_vars
from SurfacePlotter import Surface_Plotter
import matplotlib.pyplot as plt

#BRobject = BR_Plotter(sys.argv[1:])



S = Surface_Plotter(sys.argv[1:])

S.sphere.label("Label Example")

# Options = BRobject.options

# for k in Options:
# 	print k, Options[k]




