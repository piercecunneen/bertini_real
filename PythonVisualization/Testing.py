from BR_Plotter import BR_Plotter
import sys


BRobject = BR_Plotter(sys.argv[1:])



Options = BRobject.options

for k in Options:
	print k, Options[k]




